import os
import base64
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

Groq_API_KEY = os.environ.get("Groq_APIkey")
def encoded_image(image_path):   
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')
query="Is there something wrong with my face?"
#model = "meta-llama/llama-4-maverick-17b-128e-instruct"
model="meta-llama/llama-4-scout-17b-16e-instruct"
#model = "meta-llama/llama-4-scout-17b-16e-instruct"
#model="llama-3.2-90b-vision-preview" #Deprecated
def analyze_image_with_query (query:str, model:str, encoded_image, Groq_API_KEY:str):
    """
    Analyzes an image with a query using a Groq multimodal model.
    This function's signature already correctly accepts 'query' as a parameter.
    """
    client = Groq(api_key=Groq_API_KEY)  
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }
    ]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content