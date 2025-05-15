# Function Calling in Google Agent Development Kit (ADK)

So when we talk about function calling - we mostly refer to this as the set of tools that an agent uses to extend its capabilities

In ADK, a tool is typically a modular code component - normally a Python function, a class method, or even another specialized agent - designed to execute a distinct, predefined task.

## Key characteristics of tools

Before we dig into implementing basic function calling, let's check on the basic key characteristics of a tool:

1. **Action Oriented**
   - Querying databases
   - Making API requests
   - Searching the web
2. **Extends Agent capabilities**
3. **Execute predefined logic**
   - Execute specific, developer-defined logic

## How Agents Use Tools

Agents leverage tools dynamically through mechanisms often involving function calling. The process generally follows these steps:

1. **Reasoning**: The agent's LLM analyzes its system instruction, conversation history, and user request.
2. **Selection**: Based on the analysis, the LLM decides which tool, if any, to execute, based on the tools available to the agent and the docstrings that describe each tool.
3. **Invocation**: The LLM generates the required arguments (inputs) for the selected tool and triggers its execution.
4. **Observation**: The agent receives the output (result) returned by the tool.
5. **Finalization**: The agent incorporates the tool's output into its ongoing reasoning process to formulate the next response, decide the subsequent step, or determine if the goal has been achieved.

Think of the tools as a specialized toolkit that the agent's intelligent core (the LLM) can access and utilize as needed to accomplish complex tasks.

## Types of Tools in ADK

There are three main types of tools in ADK:

1. **Function Tools**
   - Tools created by you, tailored to your specific needs
2. **Built-in Tools**
   - Google Search, Code Execution
3. **Third-Party Tools**
   - Tools from popular external libraries

## Workshop Implementation Example

In this workshop, we've implemented a demo agent that showcases function calling capabilities. The implementation can be found in the `tool-agent/tools/` directory.

### Example Tools in Our Demo

```python
def get_current_time() -> dict:
  """Get the current date and time."""
  return {
    "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  }
  
def get_weather_today(location: str = "San Francisco") -> dict:
  """Get the current weather for a specific location."""
  # This is a mock function - in a real app, you'd call a weather API
  weather_data = {
    "San Francisco": "foggy, 65°F",
    "New York": "rainy, 72°F",
    "London": "cloudy, 60°F",
    "Tokyo": "sunny, 78°F"
  }
  return {
    "location": location,
    "weather": weather_data.get(location, "unknown")
  }

def calculate_tip(bill_amount: float, tip_percentage: float = 15.0) -> dict:
  """Calculate tip amount based on the bill and percentage."""
  tip_amount = bill_amount * (tip_percentage / 100)
  total = bill_amount + tip_amount
  return {
    "bill_amount": bill_amount,
    "tip_percentage": tip_percentage,
    "tip_amount": round(tip_amount, 2),
    "total": round(total, 2)
  }
```

### Key Implementation Points

1. **Well-defined docstrings**: Each function has a clear docstring that helps the LLM understand its purpose.
2. **Type annotations**: Using `-> dict` specifies the return type, which is important for ADK tools.
3. **Parameter handling**: Functions can have required parameters (like `bill_amount`) and optional parameters with defaults (like `tip_percentage`).
4. **Return structure**: Each function returns a dictionary with well-named keys for the agent to interpret.

### Agent Configuration

```python
root_agent = Agent(
  name="adk_workshop_function_calling_agent",
  model="gemini-2.0-flash",
  description="A workshop demonstration agent that showcases ADK function calling capabilities.",
  instruction=instruction_prompt,
  tools=[get_current_time, get_weather_today, calculate_tip]
)
```

## Running the Demo

To run this demo:

1. Make sure you have the Google ADK installed:
   ```
   pip install google-adk
   ```

2. Run the agent:
   ```
   cd function-calling
   adk web
   ```

3. Test different queries:
   - "What time is it right now?"
   - "How's the weather in Tokyo?"
   - "Calculate a 20% tip for my $48.75 dinner bill"

## Best Practices for Function Calling

1. **Write clear docstrings**: The LLM relies heavily on your docstrings to understand tool functionality.
2. **Use descriptive parameter names**: Make parameter names self-explanatory.
3. **Include type hints**: Proper typing helps both the LLM and developers understand the expected inputs/outputs.
4. **Handle edge cases**: Add validation and error handling in your tools.
5. **Return structured data**: Consistent return formats help the agent process results.
6. **Be specific in instructions**: Guide the agent on exactly when to use each tool.

## Chaining Tools Together

ADK supports sequential tool usage where the output of one tool can serve as the input for another. Your agent instructions should specify how to chain tools together when needed.

For example, you might instruct the agent to:
1. First, get the current time
2. Then, use that information to make a relevant weather recommendation

## Error Handling

When implementing tools, include specific instructions on how the agent should handle errors:

```python
instruction="""
...
If the weather tool returns 'unknown', ask the user for a different location.
If the tip calculator receives invalid inputs, explain to the user what went wrong.
...
"""
```

This workshop example demonstrates how to create powerful, reusable function calling capabilities that extend your agent's abilities beyond what's possible with the LLM alone.





