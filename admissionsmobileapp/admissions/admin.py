from django.contrib import admin
from admissions.models import *
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
class MajorInline(admin.StackedInline):
    model = Major
    fk_name = 'faculty'


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'

    introduction = forms.CharField(widget=CKEditorUploadingWidget)
    program = forms.CharField(widget=CKEditorUploadingWidget)


class FacultyAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "website", "introduction", "program", "created_date", "updated_date", "active"]
    search_fields = ["name", "created_date"]
    list_filter = ["name"]
    inlines = (MajorInline, )
    form = FacultyForm
    readonly_fields = ["img"]

    def img(self, faculty):
        return mark_safe("<img src='/static/{url}' width=120/>".format(url=faculty.image.name))


class MarkInline(admin.TabularInline):
    model = Major.years.through


class MajorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "code", "faculty", "created_date", "updated_date", "active"]
    search_fields = ["name", "created_date", "code", "faculty__name"]
    list_filter = ["name", "code", "faculty__name"]
    inlines = (MarkInline, )


class InformationInLine(admin.StackedInline):
    model = Information
    fk_name = "infosection"


class InformationForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = '__all__'

    description = forms.CharField(widget=CKEditorUploadingWidget)


class InformationAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "infosection", "created_date", "updated_date"]
    search_fields = ["id", "infosection__name"]
    list_filter = ["infosection__name"]
    readonly_fields = ["img"]
    form = InformationForm

    def img(self, information):
        return mark_safe("<img src='/static/{url}' width=120/>".format(url=information.image.name))


class InformationSectionAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    list_filter = ["name"]
    inlines = (InformationInLine, )

class YearAdmin(admin.ModelAdmin):
    list_display = ["id", "year"]
    search_fields = ["year"]
    list_filter = ["year"]


class CommentsAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "time", "info", "user", "created_date", "updated_date"]


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "time", "livestream", "user", "created_date", "updated_date"]


class MarkAdmin(admin.ModelAdmin):
    list_display = ["id", "major", "year"]
    search_fields = ["major__name", "year__year"]
    list_filter = ["major__name", "year__year"]


class BannerImageAdmin(admin.ModelAdmin):
    list_display = ["id", "image"]
    readonly_fields = ["img"]

    def img(self, banner):
        return mark_safe("<img src='/static/{url}' width=120/>".format(url=banner.image.name))


class UniversityInfoAdmin(admin.ModelAdmin):
    list_display = ["introduction"]


class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "username", "email", "is_active", "isCandidate", "isAdviser"]
    readonly_fields = ["img"]

    def img(self, user):
        return mark_safe("<img src='/static/{url}' width=120/>".format(url=user.avatar.name))

class LivestreamAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "announce", "time"]


class AdmissionsAppAdminSite(admin.AdminSite):
    site_header = "Hệ thống hỗ trợ tuyển sinh"

admin_site = AdmissionsAppAdminSite("myapp")

admin_site.register(Faculty, FacultyAdmin)
admin_site.register(Major, MajorAdmin)
admin_site.register(Year, YearAdmin)
admin_site.register(InformationSection, InformationSectionAdmin)
admin_site.register(Information, InformationAdmin)
admin_site.register(Comments, CommentsAdmin)
admin_site.register(Questions, QuestionsAdmin)
admin_site.register(Mark, MarkAdmin)
admin_site.register(BannerImage, BannerImageAdmin)
admin_site.register(UniversityInfo, UniversityInfoAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Livestream, LivestreamAdmin)