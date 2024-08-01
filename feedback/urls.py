from django.urls import path
from . import views             # импортим с текущего уровня вложенности модуль views

urlpatterns = [
    path('', views.hello, name='hello'),    
    path('create/', views.create_feedback, name='feedback'),
    path('list/', views.feedback_list, name='feedback_list'),
]



