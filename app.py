import asyncio
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from models import GPTRequest
from config import Settings
from openai import AsyncOpenAI
import os
import sys

api_path = os.path.abspath('./API')
sys.path.append(api_path)
from completion_prompt import get_completion_prompt
from code_prompt import get_code_prompt
from user_prompt import get_user_prompt

app = FastAPI()
settings = Settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    print("Hello")
    return {"Hello": "Mundo"}


@app.post("/makeGPTRequests")
async def make_gpt_requests(request: Request, gptRequest: GPTRequest):
    print(f"Received request: {gptRequest}")

    try:
        async def get_completion():
            return await client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": get_completion_prompt(gptRequest.inputObjString, gptRequest.prevAIMessage)},
                    {"role": "user", "content": gptRequest.userMessage},
                ],
            )

        async def get_code():
            return await client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": get_code_prompt(gptRequest.prevAIMessage)},
                    {"role": "user", "content": gptRequest.userMessage},
                ],
            )

        async def get_user():
            return await client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": get_user_prompt(gptRequest.inputObjString, gptRequest.prevAIMessage)},
                    {"role": "user", "content": gptRequest.userMessage},
                ],
            )

        completion_response, code_response, user_response = await asyncio.gather(
            get_completion(), get_code(), get_user()
        )

        response = {
            "completionResponse": completion_response.choices[0].message.content,
            "codeResponse": code_response.choices[0].message.content,
            "userResponse": user_response.choices[0].message.content,
        }

        return response

    except ValueError as ve:
        print(f"Value error: {str(ve)}")
        raise HTTPException(status_code=422, detail=str(ve))
    
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))