class Solver:
    def __init__(self , numbers):
        self.number = numbers


    def average_finder(self , numbers):
        numbers = [23, 43, 42, 76]

        average = 0

        for number in numbers:
            average += number

            print(average)


