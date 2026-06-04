from dotenv import load_dotenv
import os

load_dotenv()

print("KEY:", os.getenv("OPENROUNTER_API_KEY"))