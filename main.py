from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <html>
        <head>
            <title>My First FastAPI App</title>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is my first webpage served by FastAPI.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)