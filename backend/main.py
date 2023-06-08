import uvicorn
from gateway.api import app

if __name__ == "__main__":
    uvicorn.run(app="gateway.api:app", host="localhost", port=8000, reload=True)