from fastapi import FastAPI
from fastapi.responses import JSONResponse

@app.get("/calculate")
def calculate(operation: str, num1: float, num2: float):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return JSONResponse(content={"error": "Invalid operation"}, status_code=400)

    return JSONResponse(content={"result": result})
