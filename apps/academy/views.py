from django.shortcuts import render, get_object_or_404
from django.views import View

from apps.academy.models import Teacher, Course, Contact


class IndexView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        courses = Course.objects.all()
        contact = Contact.objects.all()
        context = {'title': 'Главная страница'
                   , 'teachers': teachers
                   , 'courses': courses
                   , 'contact': contact
                   }
        return render(request, 'academy/index.html', context)


class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        context = {
            'title': f'{teacher.full_name} - преподаватель',
            'teacher': teacher,
        }
        return render(request, 'academy/teacher_detail.html', context)


class CourseDetailView(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        context = {
            'title': f'{course.name} - курс',
            'course': course,
        }
        return render(request, 'academy/course_detail.html', context)

