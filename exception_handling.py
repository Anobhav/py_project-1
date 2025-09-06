def user_type_input(user_type):
    try:
        if user_type not in (1, 2):
            raise ValueError("Invalid input, please enter 1 or 2 next time")
        return True
    except ValueError as e:
        print(e)
        return False
