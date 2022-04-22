from django.urls import path
from subbackend import views


urlpatterns = [
    path('subscriptions/', views.subscriptions, name="subscriptions"),
    path('subscriptions/current', views.currUserSubs, name="currUserSubs"),
    path('subscriptions/<int:id>/', views.getSubsById, name="getSubsById"),
    path('subscriptions/update/', views.getUpdatedSubs, name="getUpdatedSubs"),
    path('subscriptions/<int:id>/invoice', views.invoice, name="invoice"),
]
