from django.db import models

# Create your models here.
class Zone(models.Model):
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=10)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}({self.code})"

class Lodge(models.Model):
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    price = models.IntegerField(default=60000)
    zone = models.ForeignKey(Zone, on_delete="models.CASCADE")

    def __str__(self):
        return f"{self.name} in {self.zone}"
