# Tools Overview

## Function Tool

Transforming a function into a tool is a straightforward way to integrate custom logic into your agents. In fact, when you assign a Python function to an agent's tools list, the framework will automatically wrap it as a Function Tool for you. This approach offers flexibility and quick integration.

### Parameters

Define your function parameters using standard JSON-serializable types (e.g., string, integer, list, dictionary). It's important to avoid setting default values for parameters, as the language model (LLM) does not currently support interpreting them.

### Return Type

The preferred return type for a Python Function Tool is a dictionary. This allows you to structure the response with key-value pairs, providing context and clarity to the LLM. If your function returns a type other than a dictionary, the framework automatically wraps it into a dictionary with a single key named `"result"`.

> 🟢 **Good Practice:** Return descriptive dictionaries with meaningful keys and human-readable values.
> 
> 🔴 **Bad Practice:** Returning numeric error codes or cryptic values that require additional interpretation.

Strive to make your return values as descriptive as possible. For example, instead of returning a numeric error code, return a dictionary with an `"error_message"` key containing a human-readable explanation. Remember that the LLM, not a piece of code, needs to understand the result. As a best practice, include a `"status"` key in your return dictionary to indicate the overall outcome (e.g., `"success"`, `"error"`, `"pending"`), providing the LLM with a clear signal about the operation's state.

### Docstring

The docstring of your function serves as the tool's description and is sent to the LLM. Therefore, a well-written and comprehensive docstring is crucial for the LLM to understand how to use the tool effectively. Clearly explain the purpose of the function, the meaning of its parameters, and the expected return values.

> 🟡 **Remember:** Your docstring is the primary documentation that helps the LLM understand your tool's purpose and usage.

### Best Practices

While you have considerable flexibility in defining your function, remember that simplicity enhances usability for the LLM. Consider these guidelines:

- **✅ Fewer Parameters are Better**: Minimize the number of parameters to reduce complexity.
- **✅ Simple Data Types**: Favor primitive data types like `str` and `int` over custom classes whenever possible.
- **✅ Meaningful Names**: The function's name and parameter names significantly influence how the LLM interprets and utilizes the tool. Choose names that clearly reflect the function's purpose and the meaning of its inputs. Avoid generic names like `do_stuff()`.

> 🔵 **Pro Tip:** Design your function tools with the LLM as the end user, not another piece of code.
