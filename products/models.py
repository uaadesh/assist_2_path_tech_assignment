from django.db import models

# Create your models here.
class product(models.Model):
    P_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.Name
        