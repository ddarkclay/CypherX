from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=30)
    msg = models.CharField(max_length=500)

    def __str__(self):
        return self.name