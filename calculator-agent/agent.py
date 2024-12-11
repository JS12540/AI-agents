from toolbox import ToolBox
from model import Model
import json

def return_tool_desc(tool_descriptions):
    agent_system_prompt_template = f"""
    You are an intelligent agent with access to a set of tools designed to help you answer user queries effectively. Based on the user's query, your task is to determine the most suitable tool from your toolbox, if any, and provide the necessary input for that tool.

    You will respond in the following JSON format:
    {{
        "tool_choice": "name_of_the_tool",
        "tool_input": "inputs_to_the_tool"
    }}

    tool_choice: The name of the tool you decide to use. This must be one of the tools available in your toolbox. If no tool is appropriate, specify "none".
    tool_input: The specific input required for the selected tool to perform its task. If no tool is chosen (i.e., tool_choice is "none"), leave this field empty.

    Here is a list of your tools along with their descriptions:
    {tool_descriptions}

    Carefully analyze the user's query, evaluate the available tools, and select the most suitable option. If no tool is applicable or needed, ensure that tool_choice is "none".
    """

    return agent_system_prompt_template


class Agent:
    def __init__(self, tools, model_name, stop=None):
        """
        Initializes the agent with a list of tools and a model.
        Parameters:
        tools (list): List of tool functions.
        model_service (class): The model service class with a generate_text met
        model_name (str): The name of the model to use.
        """
        self.tools = tools
        self.model_name = model_name
        self.stop = stop

    def prepare_tools(self):
        """
        Stores the tools in the toolbox and returns their descriptions.
        Returns:
        str: Descriptions of the tools stored in the toolbox.
        """
        toolbox = ToolBox()
        toolbox.store(self.tools)
        tool_descriptions = toolbox.tools()
        return tool_descriptions
    
    def think(self, prompt):
        """
        Runs the generate_text method on the model using the system prompt temp
        Parameters:
        prompt (str): The user query to generate a response for.
        Returns:
        dict: The response from the model as a dictionary.
        """
        tool_descriptions = self.prepare_tools()
        agent_system_prompt = return_tool_desc(tool_descriptions)
        # Create an instance of the model service with the system prompt

        model_instance = Model(
            model=self.model_name,
            system_prompt=agent_system_prompt
        )

        # Generate and return the response dictionary
        agent_response_dict = model_instance.generate_text(prompt)
        return agent_response_dict
    
    def work(self, prompt):
        """
        Parses the dictionary returned from think and executes the appropriate
        Parameters:
        prompt (str): The user query to generate a response for.
        Returns:
        The response from executing the appropriate tool or the tool_input if n
        """
        agent_response_dict = json.loads(self.think(prompt))
        tool_choice = agent_response_dict.get("tool_choice")
        tool_input = agent_response_dict.get("tool_input")
        print(agent_response_dict)
        for tool in self.tools:
            if tool.__name__ == tool_choice:
                response = tool(tool_input)
                print(response)
                return
            
        print(tool_input)
        return 
