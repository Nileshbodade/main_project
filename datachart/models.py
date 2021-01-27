from django.db import models

class Parameter(models.Model):
    Voltage = models.IntegerField(default=0)
    Temperature = models.IntegerField(default=0)
    Speed = models.IntegerField(default=0)
    current_datetime = models.DateTimeField()
    time = models.TimeField(blank=True, null=True)

    def __str__(self):
        parameter = str(self.time)
        Timestamp = str(self.current_datetime)
        return  Timestamp
        print(parameter)




# Create your models here.
