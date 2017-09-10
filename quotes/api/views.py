from django.utils.decorators import method_decorator
from rest_framework import generics
from .serializers import QuotesModelSerializer
from quotes.models import Quotes
from django.views.decorators.csrf import csrf_exempt


class QuotesListAPIView(generics.ListAPIView):
    serializer_class = QuotesModelSerializer

    def get_queryset(self):
        return Quotes.objects.all()


class QuotesCreateAPIView(generics.CreateAPIView):
    serializer_class = QuotesModelSerializer


@method_decorator(csrf_exempt, name='dispatch')
class QuotesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuotesModelSerializer

    def get_queryset(self):
        return Quotes.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
