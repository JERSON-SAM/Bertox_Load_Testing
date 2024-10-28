from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            h1 {
                color: #333;
            }
            form {
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            input, select, button {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                background-color: #28a745;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background-color: #218838;
            }
        </style>
    </head>
    <body>
        <h1>Simple Calculator</h1>
        <form action="/calculate" method="get">
            <label for="num1">Num1:</label>
            <input type="number" name="num1" step="any" required><br>
            
            <label for="operation">Operation:</label>
            <select name="operation" required>
                <option value="+">(+)</option>
                <option value="-">(-)</option>
                <option value="*">(×)</option>
                <option value="/">(÷)</option>
            </select><br>

            <label for="num2">Num2:</label>
            <input type="number" name="num2" step="any" required><br>

            <button type="submit">Calculate</button>
        </form>
    </body>
    </html>
    """

@app.get("/calculate")
async def calculate(num1: float,operation: str,num2: float):
    if operation == "+":
        return {"result": num1 + num2}
    elif operation == "-":
        return {"result": num1 - num2}
    elif operation == "*":
        return {"result": num1 * num2}
    elif operation == "/":
        return {"result": num1 / num2 if num2 != 0 else "Cannot divide by zero"}
    else:
        return {"error": "Invalid operation"}
