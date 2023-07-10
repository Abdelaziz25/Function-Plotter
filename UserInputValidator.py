class InputValidator:
    @staticmethod
    def validate_function(function):
        allowed_chars = set("0123456789x.+-*/^ ")
        if set(function) <= allowed_chars:
            return True
        else:
            print("Invalid characters in the function.")
            return False

    @staticmethod
    def validate_min_max(min_value, max_value):
        if min_value >= max_value:
            print("Minimum value should be smaller than the maximum value.")
            return False
        return True