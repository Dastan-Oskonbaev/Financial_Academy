from django.utils import timezone

from django.db import models

from django.utils.translation import gettext_lazy as _
from django.urls import reverse



class Contact(models.Model):
    email = models.EmailField(
        _('Email'),
        max_length=50,
        null=True,
        blank=True,
    )
    instagram = models.URLField(
        _('Instagram'),
        max_length=100,
        null=True,
        blank=True,
    )
    tiktok = models.URLField(
        _('TikTok'),
        max_length=255,
        null=True,
        blank=True,
    )
    whatsapp = models.URLField(
        _('WhatsApp'),
        max_length=100,
        null=True,
        blank=True,
    )
    telegram = models.URLField(
        _('Telegram'),
        max_length=100,
        null=True,
        blank=True,
    )
    phone_number = models.CharField(
        _('Номер тел.'),
        max_length=20,
        null=True,
        blank=True,
    )
    address = models.URLField(
        _('Адрес'),
        max_length=100,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')

    def __str__(self):
        return self.email


class Teacher(models.Model):
    full_name = models.CharField(
        _('ФИО'),
        max_length=100,
    )
    experience = models.TextField(
        _('Опыт'),
        null=True,
        blank=True,
    )
    achievements = models.TextField(
        _('Награды'),
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        _('Фото'),
        upload_to='teachers/',
    )
    courses = models.ManyToManyField(
        'Course',
        verbose_name=_('Курсы'),
        related_name='teachers',
    )

    class Meta:
        verbose_name = _('Преподаватель')
        verbose_name_plural = _('Преподаватели')

    def __str__(self):
        return self.full_name


class TeachersImages(models.Model):
    images = models.ImageField(
        _('Изображения'),
        upload_to='teachers_images/',
    )
    teacher = models.ForeignKey(
        'Teacher',
        verbose_name=_('Преподаватель'),
        related_name='images',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('Изображения преподавателя')
        verbose_name_plural = _('Изображения преподавателей')

    def __str__(self):
        return self.teacher.full_name


class Course(models.Model):
    name = models.CharField(
        _('Название'),
        max_length=100
    )
    photo = models.ImageField(
        _('Фото'),
        upload_to='courses/',
    )
    description = models.TextField(
        _('Описание'),
    )
    duration = models.CharField(
        _('Длительность (в неделях)'),
        max_length=100,
        null=True,
        blank=True,
    )
    number_of_exercises = models.CharField(
        _('Количество уроков'),
        max_length=100,
        null=True,
        blank=True,
    )
    number_of_students = models.CharField(
        _('Количество студентов'),
        max_length=100,
        null=True,
        blank=True,
    )
    price = models.CharField(
        _('Цена'),
        max_length=100,
        null=True,
        blank=True,
    )
    visiting_days = models.CharField(
        _('Дни занятий (Пн, Ср, Пт)'),
        max_length=100,
        null=True,
        blank=True,
    )
    visiting_time = models.CharField(
        _('Время занятий (12:00-13:00)'),
        max_length=100,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        _('Отображаемость'),
        default=True,
    )

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])

    class Meta:
        verbose_name = _('Курс')
        verbose_name_plural = _('Курсы')

    def __str__(self):
        return self.name


class CourseImages(models.Model):
    images = models.ImageField(
        _('Изображения'),
        upload_to='courses/',
    )
    course = models.ForeignKey(
        'Course',
        verbose_name=_('Курс'),
        related_name='images',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('Изображения курса')
        verbose_name_plural = _('Изображения курсов')

    def __str__(self):
        return self.course.name


class News(models.Model):
    title = models.CharField(
        _('Заголовок'),
        max_length=100,
    )
    description = models.TextField(
        _('Описание'),
    )

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')

    def __str__(self):
        return self.title


class NewsImages(models.Model):
    images = models.ImageField(
        _('Изображения'),
        upload_to='news/',
    )
    news = models.ForeignKey(
        'News',
        verbose_name=_('Новость'),
        related_name='images',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('Изображения новости')
        verbose_name_plural = _('Изображения новостей')

    def __str__(self):
        return self.news.title


class Request(models.Model):
    full_name = models.CharField(
        _('ФИО'),
        max_length=255,
    )
    phone_number = models.CharField(
        _('Номер тел.'),
        max_length=255,
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_('Курс'),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = _('Заявка')
        verbose_name_plural = _('Заявки')


class AboutUs(models.Model):
    image = models.ImageField(
        _('Картинка'),
        upload_to='about/'
    )
    title = models.CharField(
        _('Заголовок'),
        max_length=255,
    )
    description = models.TextField(
        _('Описание'),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('О нас')
        verbose_name_plural = _('О нас')


class OurServices(models.Model):
    image = models.ImageField(
        _('Картинка'),
        upload_to='our_services/'
    )
    title = models.CharField(
        _('Заголовок'),
        max_length=255,
    )
    description = models.TextField(
        _('Описание'),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Наши услуги')
        verbose_name_plural = _('Наши услуги')

