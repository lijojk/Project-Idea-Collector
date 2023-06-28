from django.db import models
from django.contrib.auth.models import User

# creating project_Type choice
PROJECT_CHOICES = (
    ("Mini Project", "Mini Project"),
    ("Main Project", "Main Project"),
    ("Live Project", "Live Project"),
)


# creating super_model class
class ModelSuper(models.Model):
    cr_date = models.DateTimeField(auto_now_add=True, editable=False)
    cr_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    class Meta:
        abstract = True


# creating Course model
class Course(ModelSuper):
    courses = models.CharField(max_length=150)

    def __str__(self):
        return self.courses

    class Meta:
        verbose_name_plural = "Course"


#  creating Technology model
class Technology(ModelSuper):
    is_active = models.BooleanField(default=True)
    technology = models.CharField(max_length=50)

    def __str__(self):
        return self.technology

    class Meta:
        verbose_name_plural = "Technology"


# creating Project_ideas model
class ProjectIdeas(ModelSuper):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # ---dropdown
    project_Type = models.CharField(
        max_length=20,
        choices=PROJECT_CHOICES,
        default='1'
    )  # ---dropdown
    description = models.TextField()
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)  # ---dropdown
    project_Title = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Project Idea"
