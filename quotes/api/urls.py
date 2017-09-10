from django.conf.urls import url
from .views import (
    QuotesListAPIView,
    QuotesCreateAPIView,
    QuotesDetailView
)

app_name = 'quotes'

urlpatterns = [
    url(r'^$', QuotesListAPIView.as_view(), name='api-list'),  # api/wrong
    url(r'^create/$', QuotesCreateAPIView.as_view(), name='api-create'),  # api/create
    url(r'^(?P<pk>[0-9]+)/$', QuotesDetailView.as_view(), name='api-detail')
]

