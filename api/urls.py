from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudyCenterFilter.as_view(), name="product-list")
]