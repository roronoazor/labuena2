from django.db import models


# Create your models here.
class WhatsappInfo(models.Model):

    name = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return "name: %s, phone number: %s" % (self.name, self.phone_number)
