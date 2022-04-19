from pyexpat import model
from rest_framework import serializers
from subbackend.model.models import subscription


class subscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = subscription
        fields = ['Provider_Name', 'Created_On', 'Current_Start_Date', 'Is_Automatic_Payment_Enabled',
                  'Last_Modified_On', 'Status']
