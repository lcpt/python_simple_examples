from functools import lru_cache

@lru_cache(maxsize=None)  # maxsize=None allows unlimited caching
def calculate_power(base, exponent):
    print(f"Computing for {base}^{exponent}...")  # Visual proof of execution
    return base ** exponent

# First calls execute the logic
print(calculate_power(2, 3))  # Prints message, returns 8
print(calculate_power(5, 2))  # Prints message, returns 25

# Second calls pull instantly from the internal cache
print(calculate_power(2, 3))  # Returns 8 directly (No print message!)
