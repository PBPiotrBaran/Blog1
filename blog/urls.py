from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #<int:pk> - ta część jest trudniejsza. Oznacza ona, że Django spodziewa się liczby całkowitej i przekaże jej wartość do widoku jako zmienną pk
    path('PB/', views.PB, name='PB'),
]