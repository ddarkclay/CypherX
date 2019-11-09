from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100, default="")
    category = models.CharField(max_length=50, default="")
    subject = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=1000, default="")
    pub_date = models.DateField()
    author = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="courses/images", default="")

    def __str__(self):
        return self.subject
