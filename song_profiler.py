from openai import OpenAI
from dotenv import load_dotenv
import json
import os
load_dotenv()
client=OpenAI(
    api_key=os.getenv("OPENROUNTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
def profile_batch(songs):

    song_list = "\n".join(
        f"{s['name']} - {s['artist']}"
        for s in songs
    )

    prompt = f"""
For each song, estimate:

{{
    "name":"",
    "mood":"",
    "energy":"",
    "themes":[]
}}

Return ONLY a JSON array.

Songs:

{song_list}
"""

    response = client.chat.completions.create(
        model="google/gemma-4-31b-it:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    content = response.choices[0].message.content

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    return json.loads(content)