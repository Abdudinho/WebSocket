from rest_framework.fields import IntegerField
from rest_framework.serializers import ModelSerializer

from apps.models import Category, Student, Ball


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "id", "title"

class StudentModelSerializer(ModelSerializer):
    ball = IntegerField(read_only=True)
    class Meta:
        model = Student
        fields = 'id', 'photo', 'fullname', 'ball'

class BallModelSerializer(ModelSerializer):
    class Meta:
        model = Ball
        fields = 'id', 'coin', 'student'