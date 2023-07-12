from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from apps.academy.models import Teacher, Course, Contact, News, TeachersImages, Stocks
from .forms import RequestForm


class IndexView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        courses = Course.objects.all()
        contact = Contact.objects.all()
        stocks = Stocks.objects.all()
        stocks = stocks[::-1]
        stock_item_first = stocks[0]
        stock_item_second = stocks[1]
        form = RequestForm()
        context = {'title': 'Главная страница',
                   'teachers': teachers,
                   'courses': courses,
                   'contact': contact,
                   'form': form,
                   'stocks': stocks,
                   'stock_item_first': stock_item_first,
                   'stock_item_second': stock_item_second,
                   }
        return render(request, 'academy/index.html', context)

    def post(self, request):
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
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
        form = RequestForm()
        context = {
            'title': f'{course.name} - курс',
            'course': course,
            'contact': contact,
            'form': form,
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
        stocks = Stocks.objects.all()
        context = {
            'title': 'Список новостей',
            'news': news,
            'contact': contact,
            'form': form,
            'stocks': stocks,
        }
        return render(request, 'academy/news_list.html', context)
