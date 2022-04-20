from django.db import models


class subscription(models.Model):
    Provider_Name = models.CharField(max_length=20)
    Created_On = models.CharField(max_length=122)
    Current_Start_Date = models.CharField(max_length=122)
    Current_End_Date = models.CharField(max_length=122)
    Is_Automatic_Payment_Enabled = models.CharField(max_length=122)
    Last_Modified_On = models.CharField(max_length=122)
    Status = models.CharField(max_length=122)


class subsDetails(models.Model):
    subscriptionID = models.CharField(max_length=20)
    Amount_Paid = models.CharField(max_length=122)
    Started_On = models.CharField(max_length=122)
    Ends_On = models.CharField(max_length=122)
    Invoice_File = models.CharField(max_length=122)
    subscription = models.ForeignKey(
        subscription, on_delete=models.CASCADE)
