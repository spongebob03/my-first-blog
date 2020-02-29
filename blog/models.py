from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # instance method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # magic method
    # if you call Post instance, you can see Post instance's title
    # and you can see it in Django-admin
    def __str__(self):
        return self.title