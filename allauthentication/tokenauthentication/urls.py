from django.urls import path
from .views import PostList,register,login
urlpatterns = [
    path('registration/',register,name='register'),
    path('login/', login, name='login'),
    path('postdetails/',PostList.as_view()),
]
