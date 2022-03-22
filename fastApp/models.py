from django.db import models


class Person(models.Model):
    age = models.IntegerField(default=0)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'person'

