from django.contrib import admin
from .models import (
    Contact,
    Teacher,
    TeacherImage,
    Course,
    ProfessionalAdvantage,
    News,
    NewsImage,
    Request,
    OurService,
    Review,
    Advantage,
    CompanyHead,
    OutsourcingService,
    CourseSkill,
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "phone_number", "is_displayed")
    list_filter = ("is_displayed",)
    search_fields = ("email", "phone_number")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("full_name", "role", "is_displayed")
    list_filter = ("is_displayed",)
    search_fields = ("full_name", "role")


class CourseSkillInline(admin.TabularInline):
    model = Course.skills.through
    extra = 1
    verbose_name = "Skill"
    verbose_name_plural = "Skills"


class ProfessionalAdvantageInline(admin.TabularInline):
    model = Course.professional_advantages.through
    extra = 1
    verbose_name = "Professional Advantage"
    verbose_name_plural = "Professional Advantages"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "duration", "number_of_exercises", "price", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    filter_horizontal = ("professional_advantages", "skills")
    # inlines = [CourseSkillInline, ProfessionalAdvantageInline]


@admin.register(CourseSkill)
class CourseSkillAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(ProfessionalAdvantage)
class ProfessionalAdvantageAdmin(admin.ModelAdmin):
    list_display = ("title", "preview_body")


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)
    inlines = [NewsImageInline]


# @admin.register(NewsImage)
# class NewsImageAdmin(admin.ModelAdmin):
#     list_display = ("news", "images")


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "email")
    search_fields = ("full_name", "phone_number", "email")


@admin.register(OurService)
class OurServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_displayed")
    list_filter = ("is_active", "is_displayed")
    search_fields = ("title",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "is_displayed")
    list_filter = ("is_displayed",)
    search_fields = ("author",)


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ("title", "preview_body", "is_displayed")
    list_filter = ("is_displayed",)
    search_fields = ("title",)


@admin.register(CompanyHead)
class CompanyHeadAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)


@admin.register(OutsourcingService)
class OutsourcingServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "is_displayed")
    list_filter = ("is_displayed",)
    search_fields = ("title",)


admin.site.site_header = "Административная панель"
admin.site.site_title = "Административная панель"
admin.site.index_title = "Добро пожаловать в админку"
