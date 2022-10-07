from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from .serializers import StudyCenterSerializer
from center.models import Center
from django.shortcuts import render
from rest_framework import filters
from rest_framework import generics
from django.core.paginator import Paginator



@api_view(['GET'])
def getStudyCenter(request):
    centers = Center.objects.all()
    serializers = StudyCenterSerializer(Center, many=True)
    return Response(serializers.data) 

class StudyCenterFilter(generics.ListAPIView):
    queryset = Center.objects.all()
    serializer_class = StudyCenterSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['search']
    