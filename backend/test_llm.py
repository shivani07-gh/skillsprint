#from app.ai.llm import llm

#response = llm.invoke(
#    "Reply with exactly this text: SkillsPrint AI is ready!"
#)

#print(response.content)
import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("NVIDIA_API_KEY"))