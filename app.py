from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from models import GPTRequest
from config import Settings
from openai import OpenAI
import os
import sys

api_path = os.path.abspath('./API')
sys.path.append(api_path)
from prompts.completion_prompt import get_completion_prompt
from prompts.code_prompt import get_code_prompt
from prompts.user_prompt import get_user_prompt

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

@app.get("/")
async def root():
    print("Hello")
    return {"Hello": "Mundo"}


@app.post("/makeGPTRequests")
async def make_gpt_requests(request: GPTRequest):
    try:
        completion_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": get_completion_prompt(request.inputObjString, request.prevAIMessage)},
                {"role": "user", "content": request.userMessage},
            ],
        )

        code_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": get_code_prompt(request.prevAIMessage)},
                {"role": "user", "content": request.userMessage},
            ],
        )

        user_response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": get_user_prompt(request.inputObjString, request.prevAIMessage)},
                {"role": "user", "content": request.userMessage},
            ],
        )

        return {
            "completionResponse": completion_response.choices[0].message["content"],
            "codeResponse": code_response.choices[0].message["content"],
            "userResponse": user_response.choices[0].message["content"],
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))