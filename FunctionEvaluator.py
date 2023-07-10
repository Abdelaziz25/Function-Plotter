class FunctionEvaluator:
    @staticmethod
    def evaluate_function(function, x):
        try:
            y = eval(function, {"x": x})
            return y
        except:
            print("Error evaluating the function.")
            return None