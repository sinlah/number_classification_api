# Number Classification API

## Overview
The **Number Classification API** is a simple Flask-based web service that accepts a number as input and returns interesting mathematical properties about it, along with a fun fact fetched from the [Numbers API](http://numbersapi.com/#42).

## Features
- Determines whether a number is **prime**.
- Checks if a number is **perfect**.
- Identifies if a number is an **Armstrong number**.
- Determines whether a number is **even** or **odd**.
- Computes the **sum of the digits**.
- Fetches a **fun fact** about the number from the Numbers API.
- Returns responses in **JSON format**.
- Handles **CORS (Cross-Origin Resource Sharing)**.

## API Endpoint
### `GET /api/classify-number?number=<number>`
**Request Parameters:**
- `number` (integer, required): The number to classify.

**Response Format (200 OK):**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

**Error Response (400 Bad Request):**
```json
{
    "number": "invalid_input",
    "error": "Invalid input. Please provide an integer value."
}
```

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- `pip` (Python package manager)

### Clone the Repository
```sh
git clone https://github.com/sinlah/number_classification_api.git
cd number_classification_api
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Run the API Locally
```sh
python app.py
```
By default, the API runs on `http://0.0.0.0:10000`.

## Deployment
The API is deployed on **Render**. You can use any other deployment platform of your choice such as Heroku.

### Deployment Steps
1. Push your code to a **public GitHub repository**.
2. Log in to [Render](https://render.com/) and create a **new web service**.
3. Connect your GitHub repository.
4. Set the **Build Command** to:
   ```sh
   pip install -r requirements.txt
   ```
5. Set the **Start Command** to:
   ```sh
   gunicorn app:app --bind 0.0.0.0:$PORT
   ```
6. Deploy and wait for Render to provide a **publicly accessible URL**.

## Environment Variables
The following environment variable should be set for local deployment:
```sh
PORT=10000
```
(Render automatically assigns the `PORT` variable, so no need to set it manually on Render.)

## Technologies Used
- **Python** (Flask framework)
- **Gunicorn** (WSGI server for deployment)
- **Flask-CORS** (Handles CORS)
- **Requests** (Fetches data from Numbers API)

## Testing the API
### Using cURL
```sh
curl -X GET "https://number-classification-api-ry90.onrender.com/api/classify-number?number=371"
```

### Using Postman
1. Open Postman.
2. Set request type to **GET**.
3. Enter your API endpoint:
   ```sh
   https://number-classification-api-ry90.onrender.com/api/classify-number?number=371
   ```
4. Click **Send** and check the response.

### Using a Web Browser
Simply visit:
```
https://number-classification-api-ry90.onrender.com/api/classify-number?number=371
```

## License
This project is licensed under the **MIT License**.

## Author
**[Sinlah Ebi]**

