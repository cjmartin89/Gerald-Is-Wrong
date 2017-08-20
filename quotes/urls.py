from django.conf.urls import url
from . import views

app_name = 'quotes'

urlpatterns = [
    # Occurrence Index View
    url(r'^quotes/$', views.QuoteView.as_view(), name='quote-list'),

    # Occurrence/wrong/add/
    url(r'^quotes/add/$', views.CreateQuote.as_view(), name='quote-create'),

    # Occurrence/wrong/2/
    url(r'^quotes/(?P<pk>[0-9]+)/$', views.QuoteDetail.as_view(), name='quote-detail'),

    # Occurrence/wrong/2/ Update View
    url(r'^quote/(?P<pk>[0-9]+)/$', views.QuoteUpdate.as_view(), name='quote-update'),

    # Occurrence/wrong/delete
    url(r'^quote/(?P<pk>[0-9]+)/delete/$', views.QuoteDelete.as_view(), name='quote-delete'),

]
