import json
import operator

def basic_calculator(input_str):
    """
    Perform a numeric operation on two numbers based on the input string.
    Parameters:
        input_str (str): A JSON string representing a dictionary with keys 'num1',
    
    Operations: add, subtract, multiply, divide, floor_divide, mod, power, lt, le, eq, ne, ge, gt

    Returns:
        str: The formatted result of the operation.
    Raises:
        Exception: If an error occurs during the operation (e.g., division by zero)
        ValueError: If an unsupported operation is requested or input is invalid.
    """
    try:
        # Replace single quotes with double quotes
        input_str_clean = input_str.replace("'", "\"")

        # Remove any extraneous characters such as trailing quotes
        input_str_clean = input_str_clean.strip().strip("\"")
        input_dict = json.loads(input_str_clean)
        num1 = input_dict['num1']
        num2 = input_dict['num2']
        operation = input_dict['operation']
    except (json.JSONDecodeError, KeyError) as e:
        return str(e)
    
    # Define the supported operations
    operations = {
        'add': operator.add,
        'subtract': operator.sub,
        'multiply': operator.mul,
        'divide': operator.truediv,
        'floor_divide': operator.floordiv,
        'mod': operator.mod,
        'power': operator.pow,
        'lt': operator.lt,
        'le': operator.le,
        'eq': operator.eq,
        'ne': operator.ne,
        'ge': operator.ge,
        'gt': operator.gt
    }

    # Check if the operation is supported
    if operation in operations:
        try:
            # Perform the operation
            result = operations[operation](num1, num2)
            print(f"DEBUG: result: {result}")
            result_formatted = f"\n\nThe answer is: {result}."
            return result_formatted
        except Exception as e:
            return str(e), "\n\nError during operation execution."
    else:
        return "\n\nUnsupported operation. Please provide a valid operation."


def reverse_string(input_string):
    """
    Reverse the given string.
    Parameters:
    input_string (str): The string to be reversed.
    Returns:
    str: The reversed string.
    """
    # Reverse the string using slicing
    reversed_string = input_string[::-1]
    reversed_string = f"The reversed string is: {reversed_string}"
    print(f"DEBUG: reversed_string: {reversed_string}")
    return reversed_string

