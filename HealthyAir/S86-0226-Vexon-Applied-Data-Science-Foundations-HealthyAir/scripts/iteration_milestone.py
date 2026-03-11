"""
Iteration Milestone examples: for and while loops

Run this script to observe loop behavior, break/continue usage,
and a safe demonstration of an infinite-loop pattern.
"""

def for_range_example():
    print("--- for_range_example: range(5) ---")
    for i in range(5):
        print(f"i={i}, i*i={i*i}")


def for_list_example():
    fruits = ["apple", "banana", "cherry"]
    print("--- for_list_example: iterate list with enumerate ---")
    for idx, fruit in enumerate(fruits, start=1):
        print(f"{idx}. {fruit}")


def for_dict_example():
    scores = {"Alice": 90, "Bob": 75, "Cara": 82}
    print("--- for_dict_example: iterate dict items ---")
    for name, score in scores.items():
        print(f"{name}: {score}")


def while_countdown():
    print("--- while_countdown: counting down from 5 ---")
    n = 5
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")


def while_with_break_continue():
    print("--- while_with_break_continue: scanning numbers ---")
    numbers = [2, -1, 0, 7, 3]
    i = 0
    while i < len(numbers):
        val = numbers[i]
        i += 1
        if val < 0:
            # skip negative numbers
            print(f"skipping negative: {val}")
            continue
        if val == 0:
            # exit early when a zero is found
            print("found zero, exiting loop with break")
            break
        print(f"processed: {val}")


def infinite_loop_safe_demo(max_iters=6):
    print("--- infinite_loop_safe_demo: simulated infinite loop with safety counter ---")
    i = 0
    while True:
        print(f"iteration {i}")
        i += 1
        if i >= max_iters:
            print("Reached safety limit; breaking to avoid an actual infinite loop")
            break


def main():
    for_range_example()
    print()
    for_list_example()
    print()
    for_dict_example()
    print()
    while_countdown()
    print()
    while_with_break_continue()
    print()
    infinite_loop_safe_demo()


if __name__ == "__main__":
    main()
