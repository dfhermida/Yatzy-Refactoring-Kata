from typing import List


class Roll:
    def __init__(self, die_1: int, die_2: int, die_3: int, die_4: int, die_5: int):
        self.dice = [die_1, die_2, die_3, die_4, die_5]

    def sum(self) -> int:
        return sum(self.dice)

    def count_number(self, number: int) -> int:
        return self.dice.count(number)

    def get_number_that_repeat_exactly(self, times: int) -> int:
        for number in [1, 2, 3, 4, 5, 6]:
            if self.count_number(number) == times:
                return number
        return 0

    def get_number_in_die_list_that_repeat_at_least(
        self, roll: List[int], times: int
    ) -> int:
        for number in roll:
            if self.count_number(number) >= times:
                return number
        return 0

    def get_highest_number_that_repeat_at_least(self, times: int) -> int:
        return self.get_number_in_die_list_that_repeat_at_least(
            [6, 5, 4, 3, 2, 1], times
        )

    def get_lowest_number_that_repeat_at_least(self, times: int) -> int:
        return self.get_number_in_die_list_that_repeat_at_least(
            [1, 2, 3, 4, 5, 6], times
        )

    def has_number(self, number: int) -> bool:
        return number in self.dice

    def has_numbers(self, numbers) -> bool:
        return all([self.has_number(number) for number in numbers])


class Yatzy:
    @staticmethod
    def chance(roll: Roll) -> int:
        return roll.sum()

    @staticmethod
    def yatzy(roll: Roll) -> int:
        if roll.get_highest_number_that_repeat_at_least(5) != 0:
            return 50

        return 0

    @staticmethod
    def ones(roll: Roll) -> int:
        return roll.count_number(1)

    @staticmethod
    def twos(roll: Roll) -> int:
        return roll.count_number(2) * 2

    @staticmethod
    def threes(roll: Roll) -> int:
        return roll.count_number(3) * 3

    @staticmethod
    def fours(roll: Roll) -> int:
        return roll.count_number(4) * 4

    @staticmethod
    def fives(roll: Roll) -> int:
        return roll.count_number(5) * 5

    @staticmethod
    def sixes(roll: Roll) -> int:
        return roll.count_number(6) * 6

    @staticmethod
    def pair(roll: Roll) -> int:
        return 2 * roll.get_highest_number_that_repeat_at_least(2)

    @staticmethod
    def two_pairs(roll: Roll) -> int:
        highest = roll.get_highest_number_that_repeat_at_least(2)
        lowest = roll.get_lowest_number_that_repeat_at_least(2)
        if highest != lowest:
            return 2 * highest + 2 * lowest

        return 0

    @staticmethod
    def three_of_a_kind(roll: Roll) -> int:
        return 3 * roll.get_highest_number_that_repeat_at_least(3)

    @staticmethod
    def four_of_a_kind(roll: Roll) -> int:
        return 4 * roll.get_highest_number_that_repeat_at_least(4)

    @staticmethod
    def small_straight(roll: Roll) -> int:
        if roll.has_numbers([1, 2, 3, 4, 5]):
            return roll.sum()

        return 0

    @staticmethod
    def large_straight(roll: Roll) -> int:
        if roll.has_numbers([2, 3, 4, 5, 6]):
            return roll.sum()

        return 0

    @staticmethod
    def full_house(roll: Roll) -> int:
        three_of = roll.get_number_that_repeat_exactly(3)
        two_of = roll.get_number_that_repeat_exactly(2)
        if (three_of != 0) and (two_of != 0):
            return roll.sum()

        return 0
