from django.conf.urls import patterns, url
from encuestas import views

urlpatterns = patterns('',
    # ex: /encuestas/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /encuestas/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /encuestas/5/results/
    url(r'^(?P<pk>\d+)/result/$', views.ResultsView.as_view(), name='result'),
    # ex: /encuestas/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)