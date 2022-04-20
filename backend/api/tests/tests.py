from rest_framework.test import APITestCase
from api.models import Subscription
from django.urls import reverse


class SubscriptionTest(APITestCase):

    def setUp(self):
        Subscription.objects.create(
            Provider_Name="Netflix",
            Created_On="20/04/2022",
            Current_Start_Date="20/04/2022",
            Current_End_Date="25/04/2022",
            Is_Automatic_Payment_Enabled="yes",
            Last_Modified_On="20/04/2022",
            Status="NA"
        )

    def test_get_subscription(self):
        response = self.client.get(
            reverse('subscriptions')
        )
        self.assertEqual(response.status_code, 200)

    def test_post_subscription(self):
        data = {
            "Provider_Name": "Netflix",
            "Created_On": "20/04/2022",
            "Current_Start_Date": "20/04/2022",
            "Current_End_Date": "25/04/2022",
            "Is_Automatic_Payment_Enabled": "yes",
            "Last_Modified_On": "20/04/2022",
            "Status": "NA"
        }
        response = self.client.post("/", data=data)
        self.assertEqual(response.status_code, 201)

    def test_get_subs_details(self):
        request = self.client.get("/1/")
        response = request.json()
        self.assertEqual(request.status_code, 200)
        self.assertEqual(response["Provider_Name"], "Netflix")

    def test_put_subs_details(self):
        data = {
            "Provider_Name": "Netflix",
            "Created_On": "20/04/2022",
            "Current_Start_Date": "20/04/2022",
            "Current_End_Date": "25/04/2022",
            "Is_Automatic_Payment_Enabled": "yes",
            "Last_Modified_On": "20/04/2022",
            "Status": "NA"
        }

        request = self.client.put("/1/", data=data)
        response = request.json()
        self.assertEqual(request.status_code, 200)
        self.assertEqual(response["Provider_Name"], "Netflix")

    def test_delete_subscription(self):
        request = self.client.delete(reverse("getSubsById", args=[1]))
        request1 = self.client.get("/")
        response1 = request1.json()
        self.assertEqual(request.status_code, 204)
        self.assertEqual(len(response1), 0)
