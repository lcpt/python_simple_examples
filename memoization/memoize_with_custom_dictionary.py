# Initialize your storage dictionary
results_cache = {}

def heavy_calculation(x, y):
    # Create a tuple of arguments to serve as a hashable dictionary key
    key = (x, y)
    
    # Check if the result is already stored
    if key in results_cache:
        return results_cache[key]
    
    # If not stored, calculate it
    result = x * y + 10
    
    # Store the result using the parameter key
    results_cache[key] = result
    return result

# Running the function
print(heavy_calculation(4, 5))  # Stores in cache and returns 30
print(heavy_calculation(2, 8))  # Stores in cache and returns 26

# Inspecting your stored results
print(results_cache)  
# Output: {(4, 5): 30, (2, 8): 26}
