from rest_framework.decorators import api_view # allows to define function based views that handle specific HTTP methods (e.g. GET, POST) 
from rest_framework.response import Response # return structured HTTP responses
from .models import Appliance
from django.shortcuts import render # render functio to return HTML pages for web pages
from .serializers import ApplianceSerializer
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # imports a decorator to disable CSRF protection for views - usually used for APIs accepting external POST requets (like from NodeMCU)
def api_home(request):
    return JsonResponse({"message": "Home Automation API is running."})

def index(request):
    return render(request, 'index.html')

@api_view(['GET']) # marks this view as accepting onlt GET requests
def get_appliances(request): # defines a view to fetch all appliance from the database
    appliances = Appliance.objects.all() # queries all appliances records from the database
    serializer = ApplianceSerializer(appliances, many=True) # serializes the queryset into a list of dictionaries. many = true tell the serializer it's working with multiple objects
    return Response(serializer.data) # returns the serialized appliance data as a JSON response

@csrf_exempt # disables CSRF protection (needed for external devices like NodeMCU)
@api_view(['POST']) # this view accepts POST request to toggle the status of an appliance
def toggle_appliance(request, pk):
    try:
        appliance = Appliance.objects.get(id=pk) # attempts to find the appliance with the given ID
        appliance.status = not appliance.status # reverse the status
        appliance.save() # save the new status to the database
        return Response({'id': appliance.id, 'status': appliance.status}) # returns a JSON response with the updated status
    except Appliance.DoesNotExist:
        return Response({'error': 'Not found'}, status=404) # if the appiance ID doesn't exist, return a 404 error
