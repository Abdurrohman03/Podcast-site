from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
