
from django.urls import path, include
from .views import VehicleCreateView, VehicleNoneListView, VehicleListView,  VehicleJoinDriverView, VehicleAllListView
urlpatterns = [    
    path('', VehicleCreateView.as_view(), name='Vehicle create'),
    path('lista/sin-conductor/', VehicleNoneListView.as_view(), name='Vehicle list none'),
    path('lista/con-conductor/<int:id>', VehicleListView.as_view(), name='Vehicle list with driver'),
    path('<int:id>/asociar/conductor/', VehicleJoinDriverView.as_view(), name='Vehicle join driver' ),
    path('lista/', VehicleAllListView.as_view(), name='Vehicle list all')
]
