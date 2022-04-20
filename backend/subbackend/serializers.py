from pyexpat import model
from rest_framework import serializers
from subbackend.models import subscription, subsDetails


class subscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = subscription
        fields = ['Provider_Name', 'Created_On', 'Current_Start_Date', 'Is_Automatic_Payment_Enabled',
                  'Last_Modified_On', 'Status', 'key']


class subscriptionDetailSerializer(serializers.ModelSerializer):
    model = subsDetails
    fields = ['subscriptionID', 'Amount_Paid', 'Started_On', 'Ends_On',
              'Invoice_File']
