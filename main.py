from FunctionEvaluator import FunctionEvaluator
from UserInput import UserInput


if __name__ == '__main__':
    user_input = UserInput()
    function_evaluator = FunctionEvaluator()
    function = user_input.get_function()
    while not function:
        function = user_input.get_function()

    min_value, max_value = user_input.get_min_max()



