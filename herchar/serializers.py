from rest_framework import serializers # serializers are used to convert model instances to JSON and vice versa 
from .models import Appliance # imports the Appliance model from your local app's models.py

class ApplianceSerializer(serializers.ModelSerializer): # maps model fields to serializer fields
    class Meta:
        model = Appliance # automatically creates fields in the serializer for each field in the Appliance model
        fields = ['id', 'name', 'status'] # specifies exactly which fields from the model should be included in the serialized data. converted to JSON when sending data to the frontend.NodeMCU. accepted in request when updating data from clients
