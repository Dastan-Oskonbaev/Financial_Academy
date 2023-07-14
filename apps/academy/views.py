from datetime import date

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from apps.academy.models import Teacher, Course, Contact, News, TeachersImages, AboutUs, OurServices
from .forms import RequestForm
from .sender import send_whatsapp_notification


class IndexView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        courses = Course.objects.all()
        contact = Contact.objects.all()
        about = AboutUs.objects.first()
        services = OurServices.objects.first()
        news = News.objects.all()


        form = RequestForm()
        description = about.description.split("/")
        service = services.description.split("/")


        context = {
            'title': 'Главная страница',
            'teachers': teachers,
            'courses': courses,
            'contact': contact,
            'form': form,
            'about': about,
            'services': services,
            'description': description,
            'service': service,
        }
        if len(news) >= 2:
            context['first_item'] = news[0]
            context['second_item'] = news[1]

        return render(request, 'academy/index.html', context)

    def post(self, request):
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()

            data = form.cleaned_data
            message = f'''Новая форма была заполнена:
ФИО: {data['full_name']}
Номер тел.: {data['phone_number']}
Курсы: {data['course']}
Дата: {date.today()}'''
            send_whatsapp_notification(message)

            return redirect('index')

        return render(request, 'academy/index.html')


class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        contact = Contact.objects.all()
        form = RequestForm()
        context = {
            'title': f'{teacher.full_name} - преподаватель',
            'teacher': teacher,
            'teachers_images': TeachersImages.objects.all(),
            'contact': contact,
            'form': form,
        }
        return render(request, 'academy/teacher_detail.html', context)


class CourseDetailView(View):
    def get(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        contact = Contact.objects.all()
        teacher = Teacher.objects.all()
        form = RequestForm()
        context = {
            'title': f'{course.name} - курс',
            'course': course,
            'contact': contact,
            'form': form,
            'teacher': teacher,
        }
        return render(request, 'academy/course_detail.html', context)


class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        contact = Contact.objects.all()
        form = RequestForm()
        context = {
            'title': 'Список преподавателей',
            'teachers': teachers,
            'contact': contact,
            'form': form,
        }
        return render(request, 'academy/teacher_list.html', context)


class NewsListView(View):
    def get(self, request):
        news = News.objects.all()
        contact = Contact.objects.all()
        form = RequestForm()
        context = {
            'title': 'Список новостей',
            'news': news,
            'contact': contact,
            'form': form,
        }
        return render(request, 'academy/news_list.html', context)
