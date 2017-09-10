from rest_framework import serializers
from quotes.models import Quotes


class QuotesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = [
            'pk', 'Quote', 'Person', 'DateTime'
        ]
