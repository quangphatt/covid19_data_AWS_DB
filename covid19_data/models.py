from django.db import models

class Covid19Data(models.Model):
    FIPS = models.IntegerField(null=True)
    Admin = models.CharField(max_length=80,null=True)
    Province_State = models.CharField(max_length=80,null=True)
    Country_Region = models.CharField(max_length=80,null=True)
    Last_Update = models.DateTimeField(null=True)
    Lat = models.FloatField(null=True)
    Long = models.FloatField(null=True)
    Confirmed = models.IntegerField(null=True)
    Deaths = models.IntegerField(null=True)
    Recovered = models.IntegerField(null=True)
    Active = models.IntegerField(null=True)
    Combined_Key = models.CharField(max_length=80,null=True)
    Incident_Rate = models.FloatField(null=True)
    Case_Fatality_Ratio = models.FloatField(null=True)

