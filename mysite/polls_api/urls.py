from django.urls import path
from .views import *

urlpatterns = [
    path('question/', QuestionList.as_view(), name='question_list'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='question_detail'),
]