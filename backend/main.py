import os
from os.path import abspath, dirname, join

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Define the allowed origins
current_directory = dirname(abspath(__file__))
env_path = join(current_directory, "..", ".env")
load_dotenv(env_path)

origins = [
    os.environ.get("VUE_APP_URL_DEV"),  # Your Vue frontend
    "https://your-production-url.com",  # Your production frontend
]

# Add CORSMiddleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/merx")
# async def get_merx():
#     return {"Merx": parser.merx_email_parser()}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
