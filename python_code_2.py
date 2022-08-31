###Creating a class, which initialize our specific objekt
class Scoot:
### __init__ python special method to initialize data to the Scoot. Assigning characteristics to the Scoot. 
    def __init__(self, name, year):
        self.name = name
        self.year = year
### define function to get output like " I am Mi Scooter and was produced in 2021".
    def show(self):
        print(f"I am {self.name} and was produced in {self.year} ")

###Creating a class, which initialize the bill to pay for a distance.
class Distance():
    def pay_distance(self, x):
        return x * 1.5
###Creating a class, which initialize the bill to pay by hour.
class Hour():
    def pay_by_hour(self, y):
        return y * 0.5
      
### Creating Objekt - Mi Scooter, 2021 model
p = Scoot("Mi Scooter", 2021)
p.show()

### Define Object from a class Distance and giving input from a customer like attribute. We will get this output: "Enter distance in km: 10".
d = Distance()
x = int(input('enter distance in km: '))

###Your total payment for a distance is 15.0 euro
print(f"Your total payment for a distance is {d.pay_distance(x)} euro")

### ### Define Object from a class Hour and giving input from a customer like attribute. We will get this output: "enter duration of your ride in minutes: 3".
e = Hour()
y = int(input('enter duration of your ride in minutes: '))

###Your total payment by hour is 1.5 euro
print(f"Your total payment by hour is {e.pay_by_hour(y)} euro")

# __name__() is executed at the end to ensure all functions (def) are defined
if __name__ == "__init__":
    __init__()
