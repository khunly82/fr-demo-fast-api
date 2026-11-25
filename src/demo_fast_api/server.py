from typing import Annotated

import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/api/hello')
def say_hello(name: Annotated[str, Query()] = 'World'):
    return f'Hello {name} !!'

def main():
    uvicorn.run('demo_fast_api.server:app', port=8080, reload=True)