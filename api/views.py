from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from api import serializers
from .serializers import StudyCenterSerializer
from center.models import Center


@api_view(['GET'])
def getStudyCenter(request):
    centers = Center.objects.all()
    serializers = StudyCenterSerializer(centers, many=True)
    return Response(serializers.data)  