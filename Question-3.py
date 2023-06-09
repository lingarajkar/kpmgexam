def get_value(obj, key):
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for value in obj.values():
            result = get_value(value, key)
            if result is not None:
                return result
    elif isinstance(obj, list):
        for item in obj:
            result = get_value(item, key)
            if result is not None:
                return result

# Example usage:
nested_object = {
    'a': {
        'b': {
            'c': 42
        }
    },
    'd': [1, 2, {'e': 3}]
}

print(get_value(nested_object, 'c'))  # Output: 42
print(get_value(nested_object, 'e'))  # Output: 3
print(get_value(nested_object, 'f'))  # Output: None
