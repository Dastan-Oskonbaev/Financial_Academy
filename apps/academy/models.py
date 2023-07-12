from django.utils import timezone

from django.db import models

from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    email = models.EmailField(
        _('email'),
        max_length=50,
    )
    instagram = models.URLField(
        _('instagram'),
        max_length=100,
    )
    whatsapp = models.URLField(
        _('whatsapp'),
        max_length=100,
    )
    telegram = models.URLField(
        _('telegram'),
        max_length=100,
    )
    phone_number = models.CharField(
        _('phone number'),
        max_length=20,
    )
    address = models.URLField(
        _('address'),
        max_length=100,
    )

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')

    def __str__(self):
        return self.email


class Teacher(models.Model):
    full_name = models.CharField(
        _('full name'),
        max_length=100,
    )
    experience = models.TextField(
        _('experience'),
        max_length=500
    )
    achievements = models.TextField(
        _('achievements'),
        max_length=500
    )
    photo = models.ImageField(
        _('photo'),
        upload_to='teachers/',
    )
    courses = models.ManyToManyField(
        'Course',
        verbose_name=_('courses'),
        related_name='teachers',
    )

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')

    def __str__(self):
        return self.full_name


class TeachersImages(models.Model):
    images = models.ImageField(
        _('images'),
        upload_to='teachers_images/',
    )
    teacher = models.ForeignKey(
        'Teacher',
        verbose_name=_('teacher'),
        related_name='images',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('Teacher image')
        verbose_name_plural = _('Teacher images')

    def __str__(self):
        return self.teacher.full_name


class Course(models.Model):
    name = models.CharField(
        _('name'),
        max_length=100
    )
    description = models.TextField(
        _('description'),
        max_length=500
    )
    duration = models.PositiveIntegerField(
        _('duration'),
    )
    number_of_exercises = models.PositiveIntegerField(
        _('number of exercises'),
    )
    number_of_students = models.PositiveIntegerField(
        _('number of students'),
    )
    price = models.PositiveIntegerField(
        _('price'),
    )
    visiting_days = models.CharField(
        _('visiting days'),
        max_length=100,
    )
    visiting_time = models.CharField(
        _('visiting time'),
        max_length=100,
    )
    is_active = models.BooleanField(
        default=False
    )


    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    def __str__(self):
        return self.name


class CourseImages(models.Model):
    images = models.ImageField(
        _('images'),
        upload_to='courses/',
    )
    course = models.ForeignKey(
        'Course',
        verbose_name=_('course'),
        related_name='images',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('Course image')
        verbose_name_plural = _('Course images')

    def __str__(self):
        return self.course.name


class News(models.Model):
    title = models.CharField(
        _('title'),
        max_length=100,
    )
    description = models.TextField(
        _('description'),
        max_length=500,
    )
    date = models.DateField(
        _('Date'),
        default=timezone.now(),
    )

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    def __str__(self):
        return self.title


class NewsImages(models.Model):
    images = models.ImageField(
        _('images'),
        upload_to='news/',
    )
    news = models.ForeignKey(
        'News',
        verbose_name=_('news'),
        related_name='images',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('News image')
        verbose_name_plural = _('News images')

    def __str__(self):
        return self.news.title


class Request(models.Model):
    full_name = models.CharField(
        _('Full name'),
        max_length=255,
    )
    phone_number = models.CharField(
        _('Phone number'),
        max_length=255,
    )
    course = models.ForeignKey(
        Course,
        verbose_name=_('Course'),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = _('Request')
        verbose_name_plural = _('Requests')


class Stocks(models.Model):
    title = models.CharField(
        _('title'),
        max_length=100,
    )
    description = models.TextField(
        _('description'),
        max_length=500,
    )
    date = models.DateField(
        _('Date'),
        default=timezone.now(),
    )

    class Meta:
        verbose_name = _('Stock')
        verbose_name_plural = _('Stocks')

    def __str__(self):
        return self.title


class StocksImages(models.Model):
    images = models.ImageField(
        _('images'),
        upload_to='stocks/',
    )
    stocks = models.ForeignKey(
        'Stocks',
        verbose_name=_('Stocks'),
        related_name='images',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('Stock image')
        verbose_name_plural = _('Stocks images')

    def __str__(self):
        return self.stocks.title
