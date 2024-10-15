# Third-party imports
import openai
from fastapi import FastAPI, Request, HTTPException, Depends
from starlette.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from decouple import config


# Internal imports
from models import Conversation, SessionLocal
from utils import send_message, logger


# Set up the OpenAI API client
openai.api_key = config('OPENAI_KEY')


# Dependency
def get_db():

    try:
        db = SessionLocal()
        yield db

    finally:
        db.close()



# FastAPI app setting
app = FastAPI()

@app.post("/message")
async def reply(request: Request, db: Session = Depends(get_db)):

    try:
        # Parse the form data from the request
        form_data = await request.form()
        Body = form_data.get('Body')
        From = form_data.get('From')

        if not Body:
            raise HTTPException(status_code=400, detail="No message body found")
        
        if not From:
            raise HTTPException(status_code=400, detail="No sender number found")


        # Call the OpenAI API to generate text (with openai==0.28)
        response = openai.Completion.create(
                engine='davinci-002',
                prompt=Body,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )

        # The generated text
        chat_response = response.choices[0].message['content'].strip()

        

        # # Predetermined response
        # chat_response = "Hey, what's up?!"


        # Store the conversation in the database
        try:
            conversation = Conversation(
                sender=From,
                message=Body,
                response=chat_response
            )
            db.add(conversation)
            db.commit()
            logger.info(f"Conversation #{conversation.id} stored in database")

        except SQLAlchemyError as e:
            db.rollback()
            logger.error(f"Error storing conversation in database: {e}")



        # Log the received message and response
        logger.info(f"Received message from {From}: {Body}")
        logger.info(f"Responding with: {chat_response}")



        # Send the generated response back to the user
        send_message(From, chat_response)

        # Send the response back as JSON (for logging purposes)
        return JSONResponse(content={"status": "success", "message": chat_response})


    except Exception as e:

        logger.error(f"Error processing request: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


























"Tutorial's Version"
'############################################################'

# # Endpoint definition
# app.post("/message")
# async def reply(Body: str = Form(), db: Session = Depends(get_db)):

#     # Call the OpenAI API to generate text with GPT-3.
#     response = openai.Completion.create(

#         engine = 'text-davinci-002',
#         prompt = Body,
#         max_tokens = 200,
#         n = 1,
#         stop = None,
#         temperature = 0.5,
#     )


#     # The generated text
#     chat_response = response.choices[0].text.strip()


#     # Store the conversation in the database
#     try:
#         conversation = Conversation(

#             sender=whatsapp_number,
#             message = Body,
#             response = chat_response
#         )
    
#         db.add(conversation)
#         db.commit()
#         logger.info(f"Conversation #{conversation.id} stored in database")
    
#     except SQLAlchemyError as e:
#         db.rollback()
#         logger.error(f"Error storing conversation in database: {e}")
    
#     send_message(whatsapp_number, chat_response)
#     return ""

'############################################################'









'''SAFE SERVER TEST (Twilio's Response)'''
'############################################################'

# # Third-party imports
# from fastapi import FastAPI, Request, HTTPException
# from starlette.responses import JSONResponse

# # Internal imports
# import logging
# from utils import send_message

# # Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


# app = FastAPI()

# @app.post("/message")
# async def reply(request: Request):

#     try:
#         # Parse the form data from the request
#         form_data = await request.form()
#         Body = form_data.get('Body')
#         From = form_data.get('From')

#         if not Body:
#             raise HTTPException(status_code=400, detail="No message body found")

#         if not From:
#             raise HTTPException(status_code=400, detail="No sender number found")

#         # Predetermined response
#         chat_response = "Hello there! What's up"

#         # Log the received message and response
#         logger.info(f"Received message from {From}: {Body}")
#         logger.info(f"Responding with: {chat_response}")

#         # Send the response back via Twilio
#         send_message(From, chat_response)

#         # Send the response back as JSON (for logging purposes)
#         return JSONResponse(content={"message": chat_response})

#     except Exception as e:
#         logger.error(f"Error processing request: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# # If you have other parts of the server setup, include them below this line

'############################################################'
