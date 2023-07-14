from django.utils import timezone

from django.db import models

from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    email = models.EmailField(
        _('Email'),
        max_length=50,
    )
    instagram = models.URLField(
        _('Instagram'),
        max_length=100,
    )
    tiktok = models.URLField(
        _('TikTok'),
        max_length=255,
    )
    whatsapp = models.URLField(
        _('WhatsApp'),
        max_length=100,
    )
    telegram = models.URLField(
        _('Telegram'),
        max_length=100,
    )
    phone_number = models.CharField(
        _('Номер тел.'),
        max_length=20,
    )
    address = models.URLField(
        _('Адрес'),
        max_length=100,
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
        max_length=500
    )
    achievements = models.TextField(
        _('Награды'),
        max_length=500
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
    description = models.TextField(
        _('Описание'),
        max_length=500
    )
    duration = models.PositiveIntegerField(
        _('Длительность (в неделях)'),
    )
    number_of_exercises = models.PositiveIntegerField(
        _('Количество уроков'),
    )
    number_of_students = models.PositiveIntegerField(
        _('Количество студентов'),
    )
    price = models.PositiveIntegerField(
        _('Цена'),
    )
    visiting_days = models.CharField(
        _('Дни занятий (Пн, Ср, Пт)'),
        max_length=100,
    )
    visiting_time = models.CharField(
        _('Время занятий (12:00-13:00)'),
        max_length=100,
    )
    is_active = models.BooleanField(
        _('Отображаемость'),
        default=True,
    )

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
        max_length=500,
    )
    date = models.DateField(
        _('Дата'),
        default=timezone.now(),
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


class Stocks(models.Model):
    title = models.CharField(
        _('Заголовок'),
        max_length=100,
    )
    description = models.TextField(
        _('Описание'),
        max_length=500,
    )
    date = models.DateField(
        _('Дата'),
        default=timezone.now(),
    )

    class Meta:
        verbose_name = _('Акция')
        verbose_name_plural = _('Акции')

    def __str__(self):
        return self.title


class StocksImages(models.Model):
    images = models.ImageField(
        _('Изображения'),
        upload_to='stocks/',
    )
    stocks = models.ForeignKey(
        'Stocks',
        verbose_name=_('Акция'),
        related_name='images',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('Изображения акции')
        verbose_name_plural = _('Изображения акции')

    def __str__(self):
        return self.stocks.title


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
