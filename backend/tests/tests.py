from django.forms import FileInput
from rest_framework.test import APITestCase
from subbackend.models import Subscription, SubsDetails
from django.urls import reverse


class SubscriptionTest(APITestCase):

    def setUp(self):
        Subscription.objects.create(
            Provider_Name="Netflix",
            Created_On="20/04/2022",
            Current_Start_Date="20/04/2022",
            Current_End_Date="25/04/2022",
            Is_Automatic_Payment_Enabled=True,
            Last_Modified_On="20/04/2022"
        )

        SubsDetails.object.create(
            Amount_Paid="200",
            Started_On="22/04/2022",
            Ends_On="200/04/2022",
            Invoice_File=FileInput,
            subscription=8
        )

        def test_get_data(self):
            response = self.client.get("/api/subscriptions/")
            self.assertEqual(response.status_code, 200)

        def test_post_subscription(self):
            data = {
                "Provider_Name": "Netflix",
                "Created_On": "20/04/2022",
                "Current_Start_Date": "20/04/2022",
                "Current_End_Date": "25/04/2022",
                "Is_Automatic_Payment_Enabled": True,
                "Last_Modified_On": "20/04/2022"
            }
            response = self.client.post("/api/subscriptions/", data=data)
            self.assertEqual(response.status_code, 201)

        def test_get_subs_details(self):
            request = self.client.get("/api/subscriptions/1/")
            response = request.json()
            self.assertEqual(request.status_code, 200)
            self.assertEqual(response[0]["Provider_Name"], "Netflix")

        def test_delete_subscription(self):
            request = self.client.delete("/api/subscriptions/1/")
            request1 = self.client.get("/api/subscriptions/1/")
            response1 = request1.json()
            self.assertEqual(request.status_code, 204)
            self.assertEqual(len(response1), 0)

        def test_current_subs(self):
            request = self.client.get("/api/subscriptions/current/1/")
            response = request.json()
            self.assertEqual(request.status_code, 200)
            self.assertEqual(response[0]["Provider_Name"], "Netflix")

        def test_details(self):
            request = self.client.get("/api/subsriptions/details")
            self.assertEqual(request.status_code, 200)

        def test_post_subscDetails(self):
            data = {
                "Amount_Paid": "200",
                "Started_On": "22/04/2022",
                "Ends_On": "200/04/2022",
                "Invoice_File": FileInput,
                "subscription": 8
            }
            response = self.client.post("/subscriptions/1/renew", data=data)
            self.assertEqual(response.status_code, 201)
