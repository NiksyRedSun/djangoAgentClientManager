from django.db import models

# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    membership = models.BooleanField(default=True)
    start_membership = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'


