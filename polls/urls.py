from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('create/',views.create,name='create'),
    path('vote/<int:question_id>/',views.vote,name='vote'),
    path('result/<int:question_id>/',views.result,name='result'),

]