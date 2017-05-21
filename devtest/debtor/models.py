from django.db import models
from django.db.models import Sum, Avg

class tbl_due_listing(models.Model):
    date_joined = models.DateField()
    customer_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()

    def __str__(self):  
        return "%s" %self.first_name

class tbl_profiles(models.Model):
    date = models.DateField(auto_now_add=True)
    principal_amt = models.DecimalField(max_digits=10, decimal_places=2)
    intrest_rate = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(tbl_due_listing, on_delete=models.CASCADE)
    #present_balance = models.DecimalField(max_digits=10, decimal_places=2)



# Create your models here.
