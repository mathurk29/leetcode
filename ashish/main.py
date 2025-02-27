from fastapi import FastAPI
import uvicorn

app = FastAPI()

def MyPayload(BaseModel):
    x : int

@app.post("/{path_params}")
async def handler(path_params: str, query_params: str, payload: MyPayload):
    return {"x": 1} # It gets automatically serialized to JSON

# uvicorn.run(app) # This also works, if reload is not require.

# if reload is required
# WARNING:  You must pass the application as an import string to enable 'reload' or 'workers'. Import string "app" must be in format "<module>:<attribute>".
if __name__ == "__main__":
    uvicorn.run('main:app', reload=True)