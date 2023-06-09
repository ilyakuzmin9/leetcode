"""Design a parking system for a parking lot.
The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.
Implement the ParkingSystem class:
ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class.
The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType)
Checks whether there is a parking space of carType for the car that wants to get into the parking lot.
carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively.
A car can only park in a parking space of its carType.
If there is no space available, return false, else park the car in that size space and return true.
"""


class ParkingSystem:

    add_big_count = 0
    add_medium_count = 0
    add_small_count = 0

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small


    def addCar(self, carType: int) -> bool:

        if carType == 1:
            self.add_big_count += 1
            if (self.big - self.add_big_count) >= 0:
                return True
            else:
                return False
        if carType == 2:
            self.add_medium_count += 1
            if (self.medium - self.add_medium_count) >= 0:
                return True
            else:
                return False
        if carType == 3:
            self.add_small_count += 1
            if (self.small - self.add_small_count) >= 0:
                return True
            else:
                return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)

if __name__ == '__main__':
    # ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
    # [[1, 1, 0], [1], [2], [3], [1]]
    parkingSystem = ParkingSystem(100,10,100)
    print(parkingSystem.addCar(2))
    print(parkingSystem.addCar(1))
    print(parkingSystem.addCar(3))
    print(parkingSystem.addCar(2))
    print(parkingSystem.addCar(3))
    print(parkingSystem.addCar(2))
    print(parkingSystem.addCar(2))
    print(parkingSystem.addCar(1))
    print(parkingSystem.addCar(3))
    print(parkingSystem.addCar(1))
    print(parkingSystem.addCar(2))
    print(parkingSystem.addCar(1))
    print(parkingSystem.addCar(3))
    print(parkingSystem.addCar(1))
    print(parkingSystem.addCar(3))
    print(parkingSystem.addCar(2))










