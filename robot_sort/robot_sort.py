import random

class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # I will try to implement something similar to bubble sort. This will
        # allow the robot to reduce movements until it reaches the end of the list.

        # Start by moving to the far right side of the list
        while self.can_move_right():
            self.move_right()

        # Swapping "none" item with item in front of robot. "none" item will be our placeholder for sorted vs non sorted
        self.swap_item()

        # Move all the way back to the left to begin comparrisons.
        while self.can_move_left():
            self.move_left()

        # Continue the below pattern until robot has reached the right side
        while self.can_move_right():
            # compare item in hand with item in front of robot

            # If item in front of robot is none, we have reached the part of the list that is sorted to its right
            if self.compare_item() == None:
                self.swap_item() # this puts highest item in place of "none"
                if self.can_move_left():
                    # move "none" item one to the left. Now everything to its right is sorted.
                    self.move_left()
                    self.swap_item()
                    # Move all the way back to the left
                    while self.can_move_left():
                        self.move_left()

                else: # if robot is already at the far left, list should be sorted and we can end this while loop by moveing to far right
                    while self.can_move_right():
                        self.move_right()

            # If item in hand is lower, swap items, then move one space to right
            elif self.compare_item() == -1:
                self.swap_item()
                self.move_right()

            # If item in hand is higher, keep it and move one space to the right
            elif self.compare_item() == 1:
                self.move_right()

            # If items are equal, keep and move one space to right.
            elif self.compare_item() == 0:
                self.move_right()

       # If we have reached far right side, the while loop will stop
       # We need to sawp item and then move all the way back to the left and restart while loop.
        if self.can_move_right() == False:
            self.swap_item()
            self.move_left()
            self.swap_item()
            while self.can_move_left():
                self.move_left()

       # Restarting while loop
        while self.can_move_right():
            # compare item in hand with item in front of robot

            # If item in front of robot is none, we have reached the part of the list that is sorted to its right
            if self.compare_item() == None:
                self.swap_item() # this puts highest item in place of "none"
                if self.can_move_left():
                    # move "none" item one to the left. Now everything to its right is sorted.
                    self.move_left()
                    self.swap_item()
                    # Move all the way back to the left
                    while self.can_move_left():
                        self.move_left()

                else: # if robot is already at the far left, list should be sorted and we can end this while loop by moveing to far right
                    while self.can_move_right():
                        self.move_right()

            # If item in hand is lower, swap items, then move one space to right
            elif self.compare_item() == -1:
                self.swap_item()
                self.move_right()

            # If item in hand is higher, keep it and move one space to the right
            elif self.compare_item() == 1:
                self.move_right()

            # If items are equal, keep and move one space to right.
            elif self.compare_item() == 0:
                self.move_right()

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    #l = [5, 4, 3, 2, 1]
    #l = [11, 13, 7, 17, 9, 20, 1, 21, 2, 4, 22, 16, 15, 10, 23, 19, 8, 3, 5, 14, 6, 0, 24, 12, 18]
    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]
    #l = [1, -38, -95, 4, 23, -73, -65, -36, 85, 2, 58, -26, -55, 96, 55, -76, 64, 45, 69, 36, 69, 47, 29, -47, 13, 89, -57, -88, -87, 54, 60, 56, -98, -78, 59, 93, -41, -74, 73, -35, -23, -79, -35, 46, -18, -18, 37, -64, 14, -57, -2, 15, -85, 45, -73, -2, 79, -87, -100, 21, -51, 22, 26, -59, 81, 59, -24, 24, -81, 43, 61, 52, 38, -88, -95, 87, -57, -37, -65, -47, -3, 21, -77, 98, 25, 1, -36, 39, 78, 47, -35, -40, -69, -81, 11, -47, 21, 25, -53, -31]
    #l = [20, 77, 45, 16, 15, 91, 12, 6, 24, 89, 53, 19, 85, 56, 13, 74, 48, 98, 9, 92, 25, 35, 54, 44, 50, 5, 75, 34, 2, 42, 87, 49, 76, 52, 43, 23, 7, 80, 66, 14, 46, 90, 88, 40, 97, 10, 57, 63, 1, 18, 67, 79, 96, 27, 73, 28, 32, 61, 30, 8, 17, 93, 26, 51, 60, 55, 62, 31, 47, 64, 39, 22, 99, 95, 83, 70, 38, 69, 36, 41, 37, 65, 84, 3, 29, 58, 0, 94, 4, 11, 33, 86, 21, 81, 72, 82, 59, 71, 68, 78]
    #l = [random.randint(0, 100) for i in range(0, 100)]


    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
