# prompts/completion_prompt.py
def get_completion_prompt(inputObjString, prevAIMessage):
    return (
        f"You are an AI assistant for a flight search website responsible for determining whether a user's flight search request is complete and ready to be submitted to the next step."
        f"Your task is to analyze the following pieces of information to determine if the request is complete and the user is ready to submit the request for processing: "
        f"1) Review the information gathered thus far to determine if all fields have been gathered and none of the fields are empty or invalid. This gathered information is summarized in an object called 'Current Gathered Information:' "
        f"2) Review the latest user response in tandem with the message they are responding to in order to determine whether the user is ready to submit their request. The message the user is responding to is provided as the following: 'Message User is Responding To:'."
        f"3) Respond with true if all 3 of these conditions are met: 1) 'Current Gathered Information' has information for all fields with no empty strings or '#ERROR' entries 2) the last message the user responded to was about finalizing / confirming / submitting the search request 3) the user responds with affirmation / approval to finalize / confirm / continue. If any of these conditions are NOT met, respond with false."
        f"Current Gathered Information: {inputObjString}"
        f"Message User is Responding To: {prevAIMessage}"
    )