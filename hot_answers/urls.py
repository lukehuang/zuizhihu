from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^full/(?P<pk>[0-9]+)/$', views.AnswerView.as_view(), name="answer"),
    url(r'^about/$', views.about, name='about'),
]
