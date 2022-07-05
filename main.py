import os
import graphene
from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends, Response, status, Request, Security
from fastapi.security import HTTPBearer
from mongoengine import connect
from sentry_sdk import capture_message
import sentry_sdk
from dotenv import load_dotenv
from starlette.graphql import GraphQLApp
import requests
from car import Query, Mutation
from fastapi.middleware.cors import CORSMiddleware
from utils import VerifyToken
from fastapi_auth0 import Auth0, Auth0User


load_dotenv()
mongo_password = os.environ.get("MONGO_PASSWORD")

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    traces_sample_rate=1.0
)

token_auth_scheme = HTTPBearer()
auth = Auth0(domain=os.environ.get("DOMAIN"), api_audience=os.environ.get("API_AUDIENCE"))
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route(
    "/graphql", GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutation))
)


@app.on_event("startup")
async def startup_event():
    connect(host=f"mongodb+srv://user:{mongo_password}@clusterfastapi.pypfeid.mongodb.net/?retryWrites=true&w=majority")


async def send_email_message(email: str, message: str, subject: str):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox0e5250958a554839a80d913a29fdbc71.mailgun.org/messages",
        auth=("api", os.environ.get("MAILGUN_API_PRIVATE")),
        data={"from": email,
              "to": email,
              "subject": subject,
              "text": message})


@app.get("/divide/")
async def divide():
    division_by_zero = 1 / 0
    return division_by_zero


@app.get("/raise/")
async def raise_some():
    capture_message("Item not found", level="error")
    raise HTTPException(status_code=404, detail="Item not found")


@app.get("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks, response: Response,
                            token: str = Depends(token_auth_scheme)):
    result = VerifyToken(token.credentials).verify()
    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result
    background_tasks.add_task(send_email_message, email, message="some notification",
                              subject="hi there")
    return {"message": "Notification sent in the background"}


@app.get("/secure", dependencies=[Depends(auth.implicit_scheme)])
def get_secure(user: Auth0User = Security(auth.get_user, scopes=['read:blabla'])):
    return {"message": f"{user}"}