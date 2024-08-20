from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Travel
from .serializers import TravelSerializer
@api_view(['GET'])
def get_routes(request):
    routes=[
        'GET/api'
        'GET/api/travels'
        'GET/api/travel/:id'

    ]
    return Response(routes)
@api_view(['GET'])
def get_travels(request):
    travels=Travel.objects.all()
    serializer=TravelSerializer(travels,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_travel(request,id):
    travel = Travel.objects.get(id=id)
    serializer = TravelSerializer(travel, many=False)
    return Response(serializer.data)