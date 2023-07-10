import UserInputValidator
class UserInput:
    @staticmethod
    def get_function():
        function = input("Enter a function of x: ")
        if(UserInputValidator.InputValidator.validate_function(function)):
            return function
        else:
            return False

    @staticmethod
    def get_min_max():
        while True:
            try:
                min_value = float(input("Enter the minimum value of x: "))
                max_value = float(input("Enter the maximum value of x: "))
                if UserInputValidator.InputValidator.validate_min_max(min_value, max_value):
                    return min_value, max_value
            except ValueError:
                print("Invalid input. Please enter numeric values.")