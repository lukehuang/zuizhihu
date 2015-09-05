from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.
def home(request):
    """
    Redicect to zhihu answers when domain name is used.
    """
    return HttpResponseRedirect(reverse("hot_answers:index"))
