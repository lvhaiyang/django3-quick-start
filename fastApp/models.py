from django.db import models


class Table1(models.Model):
    age = models.IntegerField(default=0)
    name = models.CharField(max_length=200)


