import json

def convert_keys_to_int(obj):
    """Recursively convert dictionary keys that are integer strings to integers."""
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            try:
                new_key = int(key)
            except (ValueError, TypeError):
                # Leave non-integer keys unchanged
                new_key = key
            new_dict[new_key] = convert_keys_to_int(value)
        return new_dict

    elif isinstance(obj, list):
        return [convert_keys_to_int(item) for item in obj]

    else:
        return obj


# Example usage
json_str = """
{
    "1": {
        "2": "hello",
        "3": [
            {"4": "world"},
            {"5": {"6": "nested"}}
        ]
    },
    "7": 42,
    "not_an_int": {
        "8": "still converted"
    }
}
"""

data = json.loads(json_str)
converted = convert_keys_to_int(data)

print(converted)
