from django.contrib import admin
from .models import Answers

# Register your models here.


class AnswersAdmin(admin.ModelAdmin):
    """ Customize admin change list and forms. """

    # modify change list
    list_display = ("question", "author", "vote", "date")

    # modify the form for adding new answers
    fieldsets = [
        ("Question Info", {"fields": ["question", "question_link"]}),
        ("Author Info", {"fields": ["author", "author_link"]}),
        ("Answer Info", {"fields": ["vote", "summary_img", "summary_text", "answer"]}),
        ("Date Info", {"fields": ["date"]}),
    ]

    # allows for sorting by date added
    list_filter = ["date"]

    # show 25 answers per page
    list_per_page = 25

admin.site.register(Answers, AnswersAdmin)
