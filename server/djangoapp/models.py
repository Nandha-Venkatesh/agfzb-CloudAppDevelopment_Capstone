from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField(max_length=1000)

   def __str__(self):
    return  ("Name: " + self.name + "\n"
            + "Description: " + self.description + "\n")

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    TYPES = [
        ("Sedan", "Sedan"),
        ("SUV", "SUV"),
        ("Wagon", "Wagon"),
        ("Convertible", "Convertible"),
        ("Pickup Truck", "Pickup Truck"),
        ("Sports Car", "Sports Car"),
    ]

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=25, choices=TYPES, default="Sedan")
    year = models.DateField()

    def __str__(self):
        return  ("Make: " + self.make.__str__() + "\n" + 
                "Name: " + self.name + "\n" + 
                "Dealer ID: " + str(self.dealer_id) + "\n" + 
                "Type: " + self.type + "\n" + 
                "Year: " + str(self.year) + "\n")

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(): 
    def __init__(self, dealership, name, purchase, review): 
        self.dealership = dealership 
        self.name = name 
        self.purchase = purchase 
        self.review = review

        # The following fields are not always present 
        self.purchase_date = ""
        self.car_make = "" 
        self.car_model = "" 
        self.car_year = "" 
        self.sentiment = "" 
        self.id = ""
    