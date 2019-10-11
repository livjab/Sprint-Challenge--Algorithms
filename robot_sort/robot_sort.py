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
        while robot.can_move_right():
            robot.move_right()
        print(f"Position is {robot._position}")

        # drop/swap "none" item with item in front of robot
        robot.swap_item()
        print(f"Holding item {robot._item}")

        # Move to the far left side of list.
        while robot.can_move_left():
            robot.move_left()
        print(f"Position is {robot._position}, and light on is {robot.light_is_on()}")

        # Continue the below pattern until robot has reached the right side)
        while robot.can_move_right():

        # compare item in hand with item in front of robot
        # If item in hand is lower, swap items, then move one space to right
        # If a swap occurs, turn on the robot's light.
            if robot.compare_item() == -1:
                robot.swap_item()
                robot.set_light_on()
                robot.move_right()

            # If item in hand is higher, keep it and move one space to the right
            elif robot.compare_item() == 1:
                robot.move_right()


            # If items are equal, keep and move one space to right.
            elif robot.compare_item() == 0:
                robot.move_right()

        # When robot reaches 'none' item at far right side ...
        if robot.compare_item() == None:
            # Check if light is on, if so return to far left, reset light to off
            if robot.light_is_on():
                robot.set_light_off()
                while robot.can_move_left():
                    robot.move_left()

            # If light is off, swap item in hand for "none" and return list
            elif robot.light_is_off():
                robot.swap_item()
                #return robot._list


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`
    #l = [5, 4, 3, 2, 1]
    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
