from django.db import models

# Create your models here.

class course(models.Model):
    courseCode = models.CharField(max_length=10)
    courseName = models.CharField(max_length=40)
    courseCredits = models.IntegerField()

    def __str__(self):
        return str(self.courseCode) + " " + str(self.courseName) + " " + str(self.courseCredits)


class student(models.Model):
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    sem = models.IntegerField()
    courses = models.ManyToManyField(course, related_name='student_set')

    def __str__(self):
        return str(self.usn) + str(self.name) + str(self.sem)
