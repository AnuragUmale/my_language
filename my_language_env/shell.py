# Import the 'basic' module. Assuming this module contains functions for running a custom language interpreter.
import basic

# Run a REPL (Read-Eval-Print Loop) that continuously takes user input and evaluates it.
while True:
    # Prompt the user for input with 'my_lang > ' and store it in the 'text' variable.
    text = input('my_lang > ')

    # If the input text is empty or contains only whitespaces, skip to the next iteration (restart the loop).
    if text.strip() == "":
        continue

    # Call the 'run' function from the 'basic' module to execute the user's input.
    # The function takes the filename (here represented as '<stdin>') and the user's input 'text'.
    # It returns two values: 'result' (the result of the execution) and 'error' (if any error occurred during execution).
    result, error = basic.run('<stdin>', text)

    # Check if there was an error during the execution.
    if error:
        # If an error occurred, print the error message.
        print(error.as_string())
    elif result:
        # If there was no error and there is a result, check if the result contains a single element.
        if len(result.elements) == 1:
            # If there is only one element, print its representation.
            print(repr(result.elements[0]))
        else:
            # If there are multiple elements, print the representation of the entire result object.
            print(repr(result))
