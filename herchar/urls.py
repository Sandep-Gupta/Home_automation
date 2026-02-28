from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),  # <-- root path
    path('api/appliances/', views.get_appliances,name = 'get_appliances'),
    path('api/toggle/<int:pk>/', views.toggle_appliance, name = 'toggle_appliance'),
]
