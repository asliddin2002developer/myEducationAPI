from django.urls import path
from . import views
 
urlpatterns = [
    path('importCSV/', views.importCSV,name="Import_csv"),     
]