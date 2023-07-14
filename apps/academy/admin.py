from django.contrib import admin

from apps.academy.models import TeachersImages, CourseImages, NewsImages, Teacher, Course, News, Contact, Request, \
     AboutUs, OurServices


class TeachersImagesInline(admin.TabularInline):
    model = TeachersImages
    extra = 1


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [TeachersImagesInline]
    save_on_top = True
    list_display = ('full_name', 'experience', 'achievements', )


class CourseImagesInline(admin.TabularInline):
    model = CourseImages
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseImagesInline]
    save_on_top = True
    list_display = ('name', 'description', 'price', 'duration', 'visiting_time', 'visiting_days', 'is_active')


class NewsImagesInline(admin.TabularInline):
    model = NewsImages
    extra = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImagesInline]
    save_on_top = True
    list_display = ('title', 'description',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'instagram', 'tiktok', 'telegram', 'whatsapp', 'phone_number', 'address')
    save_on_top = True


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'course')
    readonly_fields = ('full_name', 'phone_number', 'course')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)


@admin.register(OurServices)
class OurServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title',)
