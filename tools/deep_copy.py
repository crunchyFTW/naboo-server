def json_deep_update(original_dict: dict, new_data_dict: dict):
    for k, v in new_data_dict.items():
        if k not in original_dict:
            original_dict[k] = v
        elif isinstance(v, dict):
            if not isinstance(original_dict[k], dict):
                raise ValueError(f"failed to override configuration data for key : {k}")
            json_deep_update(original_dict[k], v)

        else:
            original_dict[k] = v