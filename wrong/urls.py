from django.conf.urls import url
from . import views


app_name = 'wrong'

urlpatterns = [
    # Occurrence Index View
    url(r'^wrong/$', views.index, name='wrong-list'),

    # Occurrence/wrong/add/
    url(r'^wrong/add/$', views.CreateOccurrence.as_view(), name='wrong-create'),

    # Occurrence/wrong/2/
    url(r'^wrong/(?P<pk>[0-9]+)/$', views.WrongDetail.as_view(), name='wrong-detail'),

    # Occurrence/wrong/2/ Update View
    url(r'^wrong/(?P<pk>[0-9]+)/update$', views.WrongUpdate.as_view(), name='wrong-update'),

    # Occurrence/wrong/delete
    url(r'^wrong/(?P<pk>[0-9]+)/delete/$', views.WrongDelete.as_view(), name='wrong-delete'),

    # # Percentage of Time Wrong
    # url(r'^count/$', views.percentage_view(), name='wrong-counter'),
]

