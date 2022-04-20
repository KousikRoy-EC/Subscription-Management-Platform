from pyexpat import model
from rest_framework import serializers
from api.models import Subscription, SubsDetails


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['Provider_Name', 'Created_On', 'Current_Start_Date', 'Is_Automatic_Payment_Enabled',
                  'Last_Modified_On', 'Status', 'key']


class SubscriptionDetailSerializer(serializers.ModelSerializer):
    model = SubsDetails
    fields = ['subscriptionID', 'Amount_Paid', 'Started_On', 'Ends_On',
              'Invoice_File']
