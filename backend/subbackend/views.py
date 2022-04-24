
from subbackend.models import SubsDetails,  Subscription
from subbackend.serializers import SubscriptionSerializer, SubscriptionDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser


@api_view(['POST', 'GET', 'DELETE'])
def subscriptions(req):
    if req.method == 'POST':
        serializer = SubscriptionSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method == 'GET':
        data = Subscription.objects.all()
        serializer = SubscriptionSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    return Response({'key': 'value'}, status=status.HTTP_200_OK)


def currUserSubs(req, id):
    if req.method == 'GET':
        data = Subscription.objects.filter(id=id)
        serializer = SubscriptionSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['POST', 'GET', 'DELETE'])
def getSubsById(request, id):
    try:
        subscription = Subscription.objects.filter(id=id)
    except Subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubscriptionSerializer(subscription, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        subscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def invoice(req, id):
    if req.method == 'GET':
        data = SubsDetails.objects.filter(id=id)
        serializer = SubscriptionDetailSerializer(data, many=True)
        return JsonResponse(serializer.data.Invoice_File, safe=False)


@csrf_exempt
@api_view(["POST"])
def getUpdatedSubs(req):
    if req.method == 'POST':
        print(req.data)
        serializer = SubscriptionDetailSerializer(data=req.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["POST"])
def renewSubscription(req, id, *args, **kwargs):
    parser_classes = (MultiPartParser, FormParser)
    if req.method == 'POST':
        startDate = req.data['Started_On']
        endDate = req.data['Ends_On']
        Subscription.objects.filter(id=id).update(
            Current_Start_Date=startDate, Current_End_Date=endDate)
        serializer = SubscriptionDetailSerializer(
            data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def subscriptionDeatils(req):
    if req.method == 'GET':
        data = SubsDetails.objects.all()
        serializer = SubscriptionDetailSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
