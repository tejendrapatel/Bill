from django.db import models

class Calculator(models.Model):
    Main_meter_bill_RS =  models.IntegerField(null = True)
    Main_Meter_Unit = models.IntegerField(null = True)
    Per_Unit_Rs = models.FloatField(null = True)
    First_meter_bill_RS = models.FloatField(null=True)
    First_Meter_Unit = models.IntegerField(null=True)
    Second_meter_bill_RS = models.FloatField(null = True)
    Second_Meter_Unit = models.IntegerField(null = True)
    Bill_image = models.FileField(null = True)
    Bill_date = models.DateField(null = True)