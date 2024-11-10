from rest_framework import serializers
from .models import Category, Course, Lesson


class BaseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, course):
        request = self.context.get('request')
        if request and course.image:
            return request.build_absolute_uri('/static/%s' % course.image)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class LessonSerializer(BaseSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'image', 'course_id']


class CourseSerializer(BaseSerializer):
    class Meta:
        model = Course
        fields = ['id', 'subject', 'image', 'category_id', 'image']
