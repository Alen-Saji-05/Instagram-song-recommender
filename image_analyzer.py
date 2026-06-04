from openai import OpenAI
from dotenv import load_dotenv
import base64
import os
load_dotenv()
client = OpenAI(
    api_key= os.getenv("OPENROUNTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def analyze_image(image_path):
    with open(image_path,"rb") as img:
        image_base64=base64.b64encode(img.read()).decode("utf-8")
    response=client.chat.completions.create(
        model="google/gemma-4-31b-it",
        messages=[
            {
                "role":"user",
                "content":[
                    {
                        "type":"text",
                        "text": """
                        Analyze this image 
                        RETURN ONLY VALID JSON
                        {
                            "mood":"",
                            "energy":"",
                            "themes":[]
                        }
                        """
                        },
                        {
                            "type": "image_url",
                            "image_url":{
                                "url":f"data:image/jpeg;base64,{image_base64}"
                            }
                        }
                    ]
              }
        ]
    )
    return response.choices[0].message.content
