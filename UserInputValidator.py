class InputValidator:
    @staticmethod
    def validate_function(function):
        """
        Validates the given function to ensure it contains only allowed characters.

        Parameters:
            function (str): The function string to validate.

        Returns:
            bool: True if the function is valid, False otherwise.
        """
        allowed_chars = set("0123456789x.+-*/^ ")

        # Check if the function is empty or contains only spaces
        if not function.strip():
            print("Function cannot be empty.")
            return False

        # Check if all characters in the function are allowed
        if set(function) <= allowed_chars:
            return True
        else:
            print("Invalid characters in the function.")
            return False

    @staticmethod
    def validate_min_max(min_value, max_value):
        """
        Validates the minimum and maximum values to ensure they are in the correct order.

        Parameters:
            min_value (float): The minimum value to validate.
            max_value (float): The maximum value to validate.

        Returns:
            bool: True if the values are valid (min_value < max_value), False otherwise.
        """
        if min_value >= max_value:
            print("Minimum value should be smaller than the maximum value.")
            return False
        return True
