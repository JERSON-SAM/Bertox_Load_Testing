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
    </head>
    <body>
        <h1>Simple Calculator</h1>
        <form action="/calculate" method="get">
            <label for="operation">Operation:</label>
            <select name="operation" required>
                <option value="+">(+)</option>
                <option value="-">(-)</option>
                <option value="*">(×)</option>
                <option value="/">(÷)</option>
            </select><br><br>

            <label for="num1">Number 1:</label>
            <input type="number" name="num1" step="any" required><br><br>

            <label for="num2">Number 2:</label>
            <input type="number" name="num2" step="any" required><br><br>

            <button type="submit">Calculate</button>
        </form>
    </body>
    </html>
    """

@app.get("/calculate")
async def calculate(operation: str, num1: float, num2: float):
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
