from django.contrib import admin
from courses.models import Category, Course, Lesson


class LessonAdmin():
    pass


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
