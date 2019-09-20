from django.conf.urls import url

from . import views
from django.views.generic import RedirectView


urlpatterns = [

    # url(r'^$', RedirectView.as_view(url='news/', permanent=False)),

    url(r'^news/$', views.AllNewsView.as_view(), name='all-news'),
    # url(r'^news/(?P<pk>\d+)/$', views.DetailNewsView, name='new-detail'),
    # url(r'^about/$', views.AboutView, name='about-page'),
    # url(r'^legal/$', views.LegalsView, name='legal'),
    # url(r'^contact/$', views.ContactsView, name='contact'),
    # url(r'^clubs/$', views.AllClubsView, name='all-clubs'),
    # url(r'^clubs/(?P<pk>\d+)/$', views.DetailClubsView, name='club-detail'),
    # url(r'^training_course/(?P<pk>\d+)/$', views.DetailTrainingCoursesView, name='training-course-detail'),
    # url(r'^events/$', views.AllEventsView, name='all-events'),
    # url(r'^events/(?P<pk>\d+)/$', views.DetailEventsView, name='event-detail'),

]
