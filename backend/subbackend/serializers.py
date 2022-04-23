from pyexpat import model
from rest_framework import serializers
from subbackend.models import Subscription, SubsDetails


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['Provider_Name', 'Created_On', 'Current_Start_Date', 'Current_End_Date', 'Is_Automatic_Payment_Enabled',
                  'Last_Modified_On']


class SubscriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubsDetails
        fields = "__all__"
