from django.urls import path
from . import views
 
urlpatterns = [
    path('Import_csv/', views.importCSV,name="Import_csv"),  
     
]