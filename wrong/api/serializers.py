from rest_framework import serializers
from wrong.models import Occurrence


class WrongModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = [
            'pk', 'TimeWrong', 'Subject', 'Details', 'DateTime'
        ]
