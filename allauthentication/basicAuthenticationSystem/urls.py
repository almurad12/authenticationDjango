from django.urls import path
from .views import MydetailsList
urlpatterns = [
    path('mydetails/',MydetailsList.as_view()),
    
]
