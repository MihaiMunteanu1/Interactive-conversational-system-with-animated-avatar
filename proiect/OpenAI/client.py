import os
from openai import OpenAI
from dotenv import load_dotenv

class OpenAIClient:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def ask(self, question, instructions):
        try:
            response = self.client.responses.create(
                model="gpt-4o-mini",
                instructions="Answer in a short paragraph." + instructions,
                input=question,
            )
            return response.output_text
        except Exception as e:
            return "I encountered an error: " + str(e)

    def generate_image(self, prompt, size="1024x1024", model="dall-e-3", quality="standard"):
        try:
            import base64

            response = self.client.images.generate(
                model=model,
                prompt=prompt,
                size=size,
                quality=quality,
                n=1,
                response_format="b64_json"
            )

            image_data = base64.b64decode(response.data[0].b64_json)
            return image_data
        except Exception as e:
            print(f"Error generating image: {str(e)}")
            return None