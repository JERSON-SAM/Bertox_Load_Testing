from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
async def calculate(operation: str, num1: float, num2: float):
    if operation == "add":
        return {"result": num1 + num2}
    elif operation == "subtract":
        return {"result": num1 - num2}
    elif operation == "multiply":
        return {"result": num1 * num2}
    elif operation == "divide":
        return {"result": num1 / num2 if num2 != 0 else "Cannot divide by zero"}
    else:
        return {"error": "Invalid operation"}
