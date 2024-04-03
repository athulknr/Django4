from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_employer= models.BooleanField('Is employer', default=False)
    is_employee= models.BooleanField('Is employee', default=False)

class JobPosting(models.Model):
    description = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[("Female", "Female"), ("Male", "Male")])

    def __str__(self):
        return self.description
class Job(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    long_description = models.TextField(blank=True, null=True)

    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title
    

class Application(models.Model):
    job = models.ForeignKey(
        'Job',  # Assuming the 'Job' model is defined in the same app or you can provide the full import path.
        related_name='applications',
        on_delete=models.CASCADE
    )
    content = models.TextField()
    experience = models.TextField()
    created_by = models.ForeignKey(
        User,
        related_name='applications_created',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
