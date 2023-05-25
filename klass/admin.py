from django.contrib import admin
from .models import Subject, Teacher, Klass, Student

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'adress', 'subject', 'created_at')
    search_fields = ('firstname', 'lastname', 'email', 'phone', 'adress', 'subject__name')
    list_filter = ('subject', 'created_at')

@admin.register(Klass)
class KlassAdmin(admin.ModelAdmin):
    list_display = ('number', 'teacher')
    search_fields = ('number', 'teacher__firstname', 'teacher__lastname')
    list_filter = ('teacher',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'adress', 'teacher')
    search_fields = ('firstname', 'lastname', 'email', 'phone', 'adress', 'teacher__firstname', 'teacher__lastname')
    list_filter = ('teacher',)