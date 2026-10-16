from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from apps.models import Category, Ball, Student
from apps.serializers import CategoryModelSerializer, StudentModelSerializer


@receiver(post_save, sender=Category)
def order_saved(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    categories = Category.objects.all()
    data = CategoryModelSerializer(instance=categories , many=True).data
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            "type": "notify_message",  # -> maps to notify_message() in consumer
            "message": data,
        },
    )


@receiver(post_save, sender=Student)
def student_saved(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    students = Student.objects.all().annotate(ball=Coalesce(Sum("balls__coin"), Value(0)))
    data = StudentModelSerializer(instance=students , many=True).data
    async_to_sync(channel_layer.group_send)(
        "dashboard",
        {
            "type": "notify_message",
            "message": data,
        },
    )

@receiver(post_save, sender=Ball)
def score_saved(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    students = Student.objects.all().annotate(ball=Coalesce(Sum("balls__coin"), Value(0)))
    data = StudentModelSerializer(instance=students , many=True).data
    async_to_sync(channel_layer.group_send)(
        "dashboard",
        {
            "type": "notify_message",
            "message": data,
        },
    )