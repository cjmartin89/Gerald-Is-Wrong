from rest_framework import generics
from .serializers import WrongModelSerializer
from wrong.models import Occurrence


class OccurrenceListAPIView(generics.ListAPIView):
    serializer_class = WrongModelSerializer

    def get_queryset(self):
        return Occurrence.objects.all()


class OccurrenceCreateAPIView(generics.CreateAPIView):
    serializer_class = WrongModelSerializer


class OccurrenceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WrongModelSerializer

    def get_queryset(self):
        return Occurrence.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




