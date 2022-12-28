from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings
from django.apps import AppConfig


# Create your models here.

# Defines custom manager class that inherits from BaseUserManager, creates and saves instances for custom user model


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    age = models.PositiveIntegerField()
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


# class Course(db.Model, UserMixin):
#     idcourses = db.Column(db.Integer, primary_key=True)
#     courseTitle = db.Column(db.String(25))
#     courseDes = db.Column(db.String(300))
#     courseLink = db.Column(db.String(150))
#     courseFeedback = db.Column(db.String(150))
#     courseTime = db.Column(db.String(30))
#     startDate = db.Column(db.String(15))
#     endDate = db.Column(db.String(15))
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user'))
#     employees = db.relationship('employeeCourse')
#     questions = db.relationship('Question')
#     answers = db.relationship('Answer')

# models the junction-table for employees and courses


# class employeeCourse(db.Model, UserMixin):
#     employee_id = db.Column(db.Integer, db.ForeignKey(
#         'user.id', name='fk_employee'), primary_key=True)
#     course_id = db.Column(db.Integer, db.ForeignKey(
#         'course.idcourses', name='fk_course'), primary_key=True)
#     manager_id = db.Column(db.Integer, db.ForeignKey(
#         'user.id', name='fk_course1'), primary_key=True)
#     answer = db.Column(db.String(150))
#     feedback = db.Column(db.String(150))
#     progress = db.Column(db.Float(11))
# models the quesions table


# class Question(db.Model, UserMixin):
#     questionId = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(500))
#     maxPoints = db.Column(db.Integer)
#     link = db.Column(db.String(150))
#     course_id = db.Column(db.Integer, db.ForeignKey(
#         'course.idcourses', name='fk_course2'), primary_key=True)
#     answers = db.relationship('Answer')

# models the junction-table for employee courses and questions


# class Answer(db.Model, UserMixin):
#     answer = db.Column(db.String(150))
#     points = db.Column(db.Integer)
#     feedback = db.Column(db.String(150))
#     employee_id = db.Column(db.Integer, db.ForeignKey(
#         'user.id', name='fk_employee1'), primary_key=True)
#     course_id = db.Column(db.Integer, db.ForeignKey(
#         'course.idcourses', name='fk_course1'), primary_key=True)
#     question_id = db.Column(db.Integer, db.ForeignKey(
#         'question.questionId', name='fk_question'), primary_key=True)


# models the users table
