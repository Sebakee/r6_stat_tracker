def find_operator_list(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "operators" and isinstance(value, list):
                return value

            found = find_operator_list(value)
            if found is not None:
                return found

    elif isinstance(data, list):
        for item in data:
            found = find_operator_list(item)
            if found is not None:
                return found

    return None


def get_sorted_operators(data):
    operators = find_operator_list(data)

    if not operators:
        return []

    return sorted(
        operators,
        key=lambda op: op.get("roundsPlayed", 0),
        reverse=True
    )