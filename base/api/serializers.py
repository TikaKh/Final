from rest_framework.serializers import ModelSerializer
from ..models import Travel

class TravelSerializer(ModelSerializer):
    class Meta:
        model=Travel
        fields='__all__'