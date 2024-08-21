# bicycles : list[str] = ['car',"bike"]


# message = f"My first bicycle name was {bicycles[-1].title()}"
# print(message)

# bicycles.append("Cycle")

# print(bicycles)

# bicycles.insert(-1,"Hi-Roof")

# print(bicycles)

# del bicycles[-3]
# print(bicycles)

# bicycles.sort()
# print(bicycles)


# bicycles.remove("Cycle")
# print(bicycles)

# for bicycle in bicycles:
#     print(bicycle)

# for value in range(1,10):
#     print(value)

# num = list(range(1,7))
# print(num)
# for i in num:
#     sqr = pow(i,2)
#     print(sqr)

# lists = list(range(1,8))

# print(min(lists))
# print(max(lists))
# print(sum(lists))

# list_comp = [pow(i,2) for i in range(1,10)]

# print(list_comp)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print("Here are three top players of my team")

# for player in players[-3:]:
#     print(f"Players are {player}")

# dimensions : tuple[int] = (9090,8765)

# print(dimensions[0])

# inputs = input("Which programming language you want to learn?")
# print(inputs)


# class Dog :
#     """ A simple attempt to model a dog"""

#     def __init__(self,name,age) -> None:
#         self.name = name
#         self.age = age
#     def rollout(self):
#         """Simulate rolling over in response to a command."""
#         print(f"{self.name} rolled over!")
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(f"{self.name} is now sitting.")
              
# dog = Dog("bully",19)
# dog2 = Dog("Johnny",19)
# print(dog.name )
# print(dog.age)
# dog.rollout()
# dog.sit()

# print(dog2.name )
# print(dog2.age)
# dog2.rollout()
# dog2.sit()


from typing import override


class Car:
    def __init__(self,speed : int,time:int) -> None:
        self.time = time
        self.speed = speed
        self.odomerter_read = 0
    
    def odo(self):
        """Print a statement showing the car's mileage."""
        print(f"The value of odo is {self.odomerter_read} ")

cars = Car(19,600)
cars.odo()
cars.odomerter_read =19
cars.odo()

class Electric_Cars(Car):
    def __init__(self, speed: int, time: int,battery :str) -> None:
        """Initialize attributes of the parent class."""
        super().__init__(speed, time)
        self.battery= battery
    @override
    def odo(self) -> None:
        print(f"This is the odo of child class and it's battery is {self.battery}")
    

e_cars = Electric_Cars(43,88,90)
print(e_cars.battery)
e_cars.odo()
