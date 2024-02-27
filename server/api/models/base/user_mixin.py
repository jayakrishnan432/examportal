from django.db import models


class Role(models.IntegerChoices):
    ADMIN = 0, 'ADMIN'
    STUDENT = 1, 'STUDENT'


class UserMixin(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    role = models.IntegerField(default=Role.STUDENT, choices=Role.choices)
