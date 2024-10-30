"""A function that outputs the number of tea bags/treats and its price for a"
__author__ = "730660179"


def main_planner(guests: int) -> None:
    """Pull function together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    """str value outside so can be portrayed as str"""
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    """Put cost function together with $, still needs str outside of ()"""


def tea_bags(people: int) -> int:
    """Tea bag function definition"""
    return people * 2


def treats(people: int) -> int:
    """Number of treats for number of teas"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Count tea and treat functions"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    """Main function call"""
