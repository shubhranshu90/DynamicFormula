
# Dynamic Formula Execution API

## Description
This project implements a Python-based web API capable of interpreting and executing mathematical expressions on datasets containing diverse data types such as numbers, strings, booleans, dates, and currencies. It supports formula chaining, allowing the output of one mathematical expression to be used as the input for another.

The API is built with **FastAPI** for rapid development and high performance, and it leverages **Uvicorn** as the ASGI server.

---

## Features

- **Dynamic Execution**: Execute mathematical formulas on diverse data types.
- **Formula Chaining**: Supports chaining of expressions where the result of one formula is used in another.
- **Type Support**: Handles numbers, booleans, dates, strings, and currencies.
- **Validation**: Validates each expression for correctness before execution.
- **Fast Performance**: Ensures sub-second response times and detects infinite loops.

---

## Technical Requirements

- **Endpoint URL**: `/api/execute-formula`
- **Supported Data Types**: Numbers, Strings, Booleans, Dates, Percentages, and Currencies.
- **Supported Operations**: All basic arithmetic operators, following BODMAS rules.
  
---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-repo/dynamic-formula-api.git
cd dynamic-formula-api
```

### Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the API

To run the API locally, execute the following command:

```bash
uvicorn app.main:app --reload
```

- `app.main:app` points to the FastAPI app instance.
- `--reload` enables auto-reloading for development mode.

The API will now be accessible at:

```
http://127.0.0.1:8000/docs
```

You can interact with the API via the interactive Swagger UI at the `/docs` endpoint.

---

## Usage Examples

### 1. Simple Addition

**Request Body**:
```json
{
  "data": [
    { "id": 1, "fieldA": 10 },
    { "id": 2, "fieldA": 20 }
  ],
  "formulas": [
    {
      "outputVar": "result",
      "expression": "fieldA + 10",
      "inputs": [
        { "varName": "fieldA", "varType": "number" }
      ]
    }
  ]
}
```

**Expected Response**:
```json
{
  "results": { "result": [20, 30] },
  "status": "success",
  "message": "The formulas were executed successfully."
}
```

### 2. Formula Chaining

**Request Body**:
```json
{
  "data": [
    { "id": 1, "fieldA": 10, "fieldB": 2 },
    { "id": 2, "fieldA": 20, "fieldB": 3 }
  ],
  "formulas": [
    {
      "outputVar": "sumResult",
      "expression": "fieldA + fieldB",
      "inputs": [
        { "varName": "fieldA", "varType": "number" },
        { "varName": "fieldB", "varType": "number" }
      ]
    },
    {
      "outputVar": "finalResult",
      "expression": "sumResult * 2 + fieldA",
      "inputs": [
        { "varName": "sumResult", "varType": "number" },
        { "varName": "fieldA", "varType": "number" }
      ]
    }
  ]
}
```

**Expected Response**:
```json
{
  "results": { "sumResult": [12, 23], "finalResult": [32, 63] },
  "status": "success",
  "message": "The formulas were executed successfully with variable-based chaining."
}
```

---

## Running Tests

You can run unit tests by executing the following command:

```bash
pytest
```

Ensure that your test cases cover various scenarios, including edge cases for formula chaining and type validation.

---

## Deployment

1. **Containerization**: The app can be containerized using Docker for easy deployment. You can use the provided `Dockerfile`.
2. **Cloud Deployment**: FastAPI apps can be deployed on cloud platforms such as AWS, GCP, or Heroku.

Refer to the deployment instructions provided by your preferred platform for further details.

---

## Contributing

If you'd like to contribute to this project, feel free to create a pull request or raise an issue.

---

## License

This project is licensed under the MIT License.
