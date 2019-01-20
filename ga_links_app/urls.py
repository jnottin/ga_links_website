from django.urls import path
from . import views

urlpatterns = [
    path('', views.galesson_list),
    path('lesson/<int:id>', views.lesson_detail, name = 'lesson_detail')
]