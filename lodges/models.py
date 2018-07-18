from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Zone(models.Model):
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name}({self.code})"

class Lodge(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    zone = models.ForeignKey(Zone, on_delete="models.CASCADE")

    def __str__(self):
        return f"{self.name} in {self.zone}"
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete="models.CASCADE")

    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    department = models.CharField(max_length=70)
    faculty = models.CharField(max_length=70)
    level = models.CharField(max_length=70)
    gender = models.CharField(max_length=20)
    study = models.CharField(max_length=70)
    kin_name = models.CharField(max_length=70)
    kin_phone = models.CharField(max_length=70)
    self_description = models.CharField(max_length=700)
    health_issues = models.CharField(max_length=300)
    lodge = models.ForeignKey(Lodge, blank=True, null=True, on_delete="models.CASCADE")

    def __str__(self):
        return f"{self.full_name}"
