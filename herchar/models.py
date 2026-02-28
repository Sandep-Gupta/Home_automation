from django.db import models # models provides the base class and field types needed to define your database tables like CharField, BooleanField

class Appliance(models.Model): # creates a table named automation_control_appliance
    name = models.CharField(max_length=50) # defines a name field of type CharField. sets the maximum number of characters allowed
    status = models.BooleanField(default=False)  # defines  a status field of type BooleanFieled (False = OFF, True = ON)

    def __str__(self): # defines a special method that controls how the object is displayed when printed.
        return f"{self.name} - {'ON' if self.status else 'OFF'}" # return a readable string. returns "Light - ON" of status == True