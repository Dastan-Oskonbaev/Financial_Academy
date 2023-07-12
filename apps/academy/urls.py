from django.urls import path

from apps.academy.views import IndexView, TeacherDetailView, CourseDetailView, NewsDetailView, NewsListView, TeacherListView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('teacher/<int:teacher_id>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('course/<int:course_id>/', CourseDetailView.as_view(), name='course_detail'),
    path('news/<int:news_id>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('teacher/', TeacherListView.as_view(), name='teacher_list'),
]
