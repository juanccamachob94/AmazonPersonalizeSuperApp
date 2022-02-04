class ApplicationHelper:
    def keys_values_to_dict(keys, values):
        length = len(keys)
        response = {}
        for i in range(length):
            response[keys[i]] = values[i]
        return response
