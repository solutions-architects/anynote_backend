def deep_update(base_dict: dict, update_with: dict) -> dict:
    """Update deeply nested dictionaries."""
    for key, value in update_with.items():
        # If the value is a dict
        if isinstance(value, dict):
            base_dict_value = base_dict.get(key)

            # If the nested value is also a dict then call recursively the deep_update()
            if isinstance(base_dict_value, dict):
                deep_update(base_dict_value, value)
            # If the nested value is NOT a dict then set the new value
            else:
                base_dict[key] = value

        # If the value is NOT a dict then set the new value
        else:
            base_dict[key] = value

    return base_dict
