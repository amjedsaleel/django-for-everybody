from django.db import models

# Create your models here.


class Person(models.Model):
    email = models.EmailField(max_length=128, unique=True)
    name = models.TextField(max_length=30, null=True)
    courses = models.ManyToManyField('Course', through='Membership')

    def __str__(self):
        return self.email


class Course(models.Model):
    title = models.CharField(max_length=50, unique=True)
    members = models.ManyToManyField('Person', through='Membership')

    def __str__(self):
        return self.title


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    LEARNER = 1
    IA = 1000
    GSI = 2000
    INSTRUCTOR = 5000
    ADMIN = 10000

    MEMBER_CHOICES = (
        (LEARNER, 'Learner'),
        (IA, 'Instructional Assistant'),
        (GSI, 'Grad Student Instructor'),
        (INSTRUCTOR, 'Instructor'),
        (ADMIN, 'Administrator'),
    )
    role = models.TextField(choices=MEMBER_CHOICES, default='LEARNER')

    def __str__(self):
        return "Person " + str(self.person.id) + " <--> Course " + str(self.course.id)
