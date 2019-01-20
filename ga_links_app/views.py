from django.shortcuts import render
from .models import GaLesson

# Create your views here.
def galesson_list(request):
    lessons = GaLesson.objects.all()
    return render(request, 'lessons.html', {'lessons': lessons})

def lesson_detail(request, id):
    lesson = GaLesson.objects.get(id = id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})