import datetime
from django.views import generic
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from .models import Answers


# Create your views here.
class IndexView(generic.ListView):
    """
    Index page will display a list of the answers in the database.
    Includes question, author, and vote.
    """

    template_name = "hot_answers/index.html"
    context_object_name = "answers"

    def get_queryset(self):
        answer_list = Answers.objects.order_by('-date', '-answer_id')

        # filter by date as requested
        now = timezone.now()

        # convert "now" to the user's time zone if possible
        if timezone.is_aware(now):
            now = timezone.localtime(now)

        today = now.date()
        tomorrow = today + datetime.timedelta(days=1)
        last_week = today - datetime.timedelta(days=7)
        this_month = today.replace(day=1)
        this_year = today.replace(month=1, day=1)

        if today.month == 12:
            next_month = today.replace(year=today.year + 1, month=1, day=1)
        else:
            next_month = today.replace(month=today.month + 1, day=1)

        next_year = today.replace(year=today.year + 1, month=1, day=1)

        self.range = self.request.GET.get("range", "all")

        if self.range == "today":
            answer_list = answer_list.filter(date__gte=today,
                                             date__lt=tomorrow)

        elif self.range == "week":
            answer_list = answer_list.filter(date__gte=last_week,
                                             date__lt=tomorrow)

        elif self.range == "month":
            answer_list = answer_list.filter(date__gte=this_month,
                                             date__lt=next_month)

        elif self.range == "year":
            answer_list = answer_list.filter(date__gte=this_year,
                                             date__lt=next_year)

        # whether order by vote
        self.order_by = self.request.GET.get("order_by", "date")

        if self.order_by == "vote":
            answer_list = answer_list.order_by('-vote', '-answer_id')

        # use Django's Paginator to display 6 answers per page
        paginator = Paginator(answer_list, 6)

        page = self.request.GET.get("page", 1)

        try:
            answers = paginator.page(page)
        except PageNotAnInteger:
            answers = paginator.page(1)
        except EmptyPage:
            answers = paginator.page(paginator.num_pages)

        return answers

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # add time filter and order_by info
        context["range"] = self.range
        context["order_by"] = self.order_by

        return context


class AnswerView(generic.DetailView):
    """
    An answer page will show all the details of a particular answer.
    Includes question, a link to the question on zhihu.com, author,
    author's zhihu page, vote, and answer text.
    If the requested answer doesn't exist, raise a Http404 exception.
    """

    model = Answers
    template_name = "hot_answers/answer.html"
    context_object_name = "answer"


def about(request):
    """ About page. """
    return render(request, "hot_answers/about.html")
