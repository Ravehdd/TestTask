
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    start_time = models.DateTimeField(null=False, blank=True)
    price = models.IntegerField(null=False)
    max_users = models.IntegerField(null=False)
    min_users = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=255, null=False)
    video_link = models.URLField(null=False, max_length=512)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255, null=False)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    count_members = models.IntegerField(default=0)


class GroupUsers(models.Model):
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class Access(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_allowed = models.BooleanField(default=False)