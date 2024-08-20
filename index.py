# Problem 1: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

def flatten_dict(d):
    flat_dict = {}
    for key, value in d.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flat_dict[f"{key}.{sub_key}"] = sub_value
        else:
            flat_dict[key] = value
    return flat_dict

nested_dict = {'a':1, 'b': {'i': 2, 'j':3}, 'c': 4}
flattened = flatten_dict(nested_dict)
print(flattened)
# Expected output: {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}


# Problem 2: Write a function unflatten_dict to do reverse of flatten_dict.
def unflatten_dict(d):
    unflattened = {}
    
    for key, value in d.items():
        keys = key.split('.')
        temp_dict = unflattened
        
        # Navigate through the keys to find or create the nested structure
        for part in keys[:-1]:
            if part not in temp_dict:
                temp_dict[part] = {}
            temp_dict = temp_dict[part]
        
        # Set the value at the final key
        temp_dict[keys[-1]] = value
    
    return unflattened

# Example usage
flattened_dict = {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}
unflattened = unflatten_dict(flattened_dict)
print(unflattened)  # Output: {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}


# Problem 3: Write a function treemap to map a function over nested list.
def treemap(func, lst):
    if isinstance(lst, list):
        return [treemap(func, item) for item in lst]
    else:
        return func(lst)

result = treemap(lambda x: x * x, [1, 2, [3, 4, [5]]])
print(result)  # Output: [1, 4, [9, 16, [25]]]