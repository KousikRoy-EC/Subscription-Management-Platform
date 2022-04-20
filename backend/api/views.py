from django.shortcuts import render
from api.models import subsDetails, subscription
from api.serializers import SubscriptionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse


@api_view(['POST', 'GET', 'PUT', 'DELETE'])
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
        data = subscription.objects.all()
        serializer = SubscriptionSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)

    return Response({'key': 'value'}, status=status.HTTP_200_OK)


def currUserSubs(req):
    if req.method == 'GET':
        data = subscription.objects.all()
        serializer = SubscriptionSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)


def getSubsById(request, id):
    try:
        userID = subscription.objects.get(id=id)
    except subscription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SubscriptionSerializer(userID)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubscriptionSerializer(userID, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        subscription.delete()
        subsDetails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def invoice(req, id):
    print("This is invoice")
