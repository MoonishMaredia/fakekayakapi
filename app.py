import asyncio
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from models import GPTRequest, TriageRequest, FlightDataRequest, FlightScalarRequest
from config import Settings
from openai import AsyncOpenAI
from pymongo.mongo_client import MongoClient
import os
import sys
from dotenv import load_dotenv
import traceback

load_dotenv()

client = AsyncOpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

mongoURI = "mongodb+srv://moonishm:"+ os.getenv("MONGODB_PASS") + "@fakekayakcluster.jdydf.mongodb.net/?retryWrites=true&w=majority&appName=FakeKayakCluster"
mongoClient = MongoClient(mongoURI)


api_path = os.path.abspath('./API')
sys.path.append(api_path)
from completion_prompt import get_completion_prompt
from code_prompt import get_code_prompt
from user_prompt import get_user_prompt
from triage_prompt import get_triage_prompt
from get_flight_scalars import generate_scalars


from get_flight_data import query_data

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
    
    print(f"Received request")

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
    
    
@app.post("/makeTriageRequest")
async def make_triage_request(request: Request, triageRequest: TriageRequest):
    
    print(f"Received request")

    try:
        async def get_triage():
            return await client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": get_triage_prompt(triageRequest.prevAIMessage)},
                    {"role": "user", "content": triageRequest.userMessage},
                ],
            )

        triage_response_list = await asyncio.gather(
            get_triage())

        triage_response = triage_response_list[0]

        response = {
            "triageResponse": triage_response.choices[0].message.content,
        }

        return response

    except ValueError as ve:
        print(f"Value error: {str(ve)}")
        raise HTTPException(status_code=422, detail=str(ve))
    
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/getFlightResults")
async def get_flight_results(request: Request, flightDataRequest: FlightDataRequest):
    print(flightDataRequest)
    try: 
        result = {}
        input_dict = flightDataRequest.dict()
        orig_code = input_dict['originCode']
        dest_code = input_dict['destinationCode']
        orig_date = input_dict['origDate']
        flightsTo = query_data(mongoClient, "fakekayak", "flights", orig_code, dest_code)
        result['flightsTo'] = flightsTo
        result['scalarsTo'] = generate_scalars(orig_date, len(flightsTo))
        flightsReturn = query_data(mongoClient, "fakekayak", "flights", dest_code, orig_code)
        result['flightsReturn'] = flightsReturn
        return_date = input_dict['returnDate']
        result['scalarsReturn'] = generate_scalars(return_date, len(flightsReturn))

        return result

    # In your exception handling blocks:
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        print(traceback.format_exc())  # This will print the full traceback
        raise HTTPException(status_code=500, detail=str(e))
    

@app.post("/getFlightScalars")
async def get_flight_results(request: Request, flightScalarRequest: FlightScalarRequest):
    try: 
        input_dict = flightScalarRequest.dict()
        orig_date = input_dict['date']
        num_flights = input_dict['numFlights']
        result = generate_scalars(orig_date, num_flights)
        return result

    # In your exception handling blocks:
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        print(traceback.format_exc())  # This will print the full traceback
        raise HTTPException(status_code=500, detail=str(e))   



# When shutting down your application, close the client
@app.on_event("shutdown")
def shutdown_event():
    mongoClient.close()
