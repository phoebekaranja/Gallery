from django.db import models
import datetime as dt

# Create your models here.



class Photographer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_photography(self):
        self.save()
class location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        save.self()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,location,update):
         updated = cls.objects.filter(image_name=location).update(name=update)
         return updated
