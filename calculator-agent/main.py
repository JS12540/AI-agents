from agent import Agent
from tools import basic_calculator,reverse_string

if __name__ == "__main__":
    tools = [basic_calculator, reverse_string]
    model_name="llama3-8b-8192"

    agent = Agent(
        tools=tools,
        model_name=model_name
    )

    while True:
        prompt = input("Ask me anything: ")
        if prompt.lower() == "exit":
            break
        agent.work(prompt)