from django.conf.urls import url
from .views import (
    OccurrenceListAPIView,
    OccurrenceCreateAPIView,
    OccurrenceDetailView
)

app_name = 'wrong'

urlpatterns = [
    url(r'^$', OccurrenceListAPIView.as_view(), name='api-list'),  # api/wrong
    url(r'^create/$', OccurrenceCreateAPIView.as_view(), name='api-create'),  # api/create
    url(r'^(?P<pk>[0-9]+)/$', OccurrenceDetailView.as_view(), name='api-detail')
]

