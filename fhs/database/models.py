from django.db import models


class signup(models.Model):
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=50, blank=False)
    email=models.EmailField(max_length=100, blank=False,unique=True)

    class signup(models.Model):
        db_table="signup_table"

class cart(models.Model):
    mail=models.CharField(max_length=30,blank=False)
    pid=models.IntegerField(max_length=10,blank=False)
    def str(self):
        return self.mail
    class Meta:
        db_table="cart_table"
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    class Reservation(models.Model):
        db_table="reserve_table"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    message = models.TextField()

    class  ContactMessage(models.Model):
        db_table="contact_table"


