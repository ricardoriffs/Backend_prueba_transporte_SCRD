
from django.urls import path, include
from .views import DriverCreateView, DriveListView

urlpatterns = [
    path('', DriverCreateView.as_view(), name='DriveCreate' ),
    path('lista/', DriveListView.as_view(), name='DriverList' )
]