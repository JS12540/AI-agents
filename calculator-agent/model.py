from groq import Groq

class Model:
    def __init__(self, model,system_prompt,temperature=0.0):
        self.client = Groq(
            api_key="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"
        )
        self.model = model
        self.system_prompt = system_prompt
        self.temperature = temperature

    
    def generate_text(self,prompt):

        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=self.temperature,
            model=self.model,
            stream=False,
            max_tokens=1024,
            top_p=0.2,
            response_format={"type": "json_object"}
        )

        return response.choices[0].message.content