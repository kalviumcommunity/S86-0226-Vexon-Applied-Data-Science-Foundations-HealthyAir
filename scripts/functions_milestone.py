"""
Functions Milestone examples: defining and calling Python functions

Run this script to observe defining functions, passing arguments,
return values, local vs global scope, and simple usages.
"""

GLOBAL_VAR = "global-value"

def greet(name):
    """Return a greeting for `name`."""
    return f"Hello, {name}!"


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def repeat(text, times=2):
    """Demonstrate default parameter values."""
    return text * times


def var_args_demo(*args, **kwargs):
    """Show positional and keyword variable args."""
    print("positional args:", args)
    print("keyword args:", kwargs)


def scope_demo():
    """Demonstrate local vs global variables."""
    local_var = "local-value"
    print("inside function: GLOBAL_VAR=", GLOBAL_VAR)
    print("inside function: local_var=", local_var)


def modify_global():
    """Modify a global variable using `global` keyword."""
    global GLOBAL_VAR
    GLOBAL_VAR = "modified-global"


def main():
    print("--- greet() ---")
    print(greet("Alice"))

    print("\n--- add() ---")
    print("2 + 3 =", add(2, 3))

    print("\n--- repeat() with and without default ---")
    print(repeat("ha"))
    print(repeat("ha", times=4))

    print("\n--- var_args_demo() ---")
    var_args_demo(1, 2, 3, name="Bob", score=88)

    print("\n--- scope_demo() before modifying global ---")
    print("GLOBAL_VAR before:", GLOBAL_VAR)
    scope_demo()

    print("\n--- modify_global() and check value ---")
    modify_global()
    print("GLOBAL_VAR after:", GLOBAL_VAR)


if __name__ == "__main__":
    main()
