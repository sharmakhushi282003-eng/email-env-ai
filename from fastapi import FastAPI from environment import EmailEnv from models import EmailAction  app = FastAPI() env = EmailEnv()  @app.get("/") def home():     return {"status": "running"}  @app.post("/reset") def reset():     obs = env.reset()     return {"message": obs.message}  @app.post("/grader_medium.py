def grade_medium(action):
    if action == "reply":
        return 1.0
    elif action == "forward":
        return 0.5
    return 0.0
