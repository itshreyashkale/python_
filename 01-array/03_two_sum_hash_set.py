"""
Two Sum - Hash Set Approach
===========================

Problem:
    Given a list of integers and a target, determine whether two
    different elements add up to the target.

Example:
    numbers = [2, 7, 11, 15]
    target = 9
    Output: True

Approach:
    Visit each number once. Calculate the partner needed to reach
    the target. Check whether that partner has already been seen.
    If not, store the current number for future checks.

Complexity:
    Time:  O(n) average - each set lookup and insertion is O(1) on average.
    Space: O(n) - the set can store up to n distinct values.
"""


def has_two_sum(numbers: list[int], target: int) -> bool:
    """Return True when two different positions sum to target."""
    seen = set()

    for number in numbers:
        required = target - number

        if required in seen:
            return True

        seen.add(number)

    return False


if __name__ == "__main__":
    print(has_two_sum([2, 7, 11, 15], 9))  # True
    print(has_two_sum([2, 11, 15], 100))  # False
    print(has_two_sum([5], 10))           # False
    print(has_two_sum([5, 5], 10))        # True
