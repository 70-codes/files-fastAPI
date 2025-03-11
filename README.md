# FastAPI File Upload and Download API

This project provides a simple FastAPI-based application that allows users to upload and download files.

## Features

- Upload files to the server
- Download files from the server
- Serve static files

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

To start the FastAPI application, run:

```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Endpoints

### Root Endpoint

- **GET /**
- Returns a JSON response with a welcome message.

**Response:**

```json
{
  "message": "Hello World"
}
```

### Upload File

- **POST /uploadfile/**
- Allows users to upload a file to the server.

**Request:**

- Form-data with a file input field.

**Response:**

```json
{
  "status": "success",
  "message": "File uploaded successfully",
  "filename": "files/example.txt",
  "type": "text/plain"
}
```

### Download File

- **GET /download/{filename}**
- Retrieves the specified file if it exists on the server.

**Response:**

- Returns the requested file if available.
- If the file does not exist, returns a 404 error.

### Static File Serving

- Files are stored in the `files/` directory and can be accessed via `/files/{filename}`.

## Directory Structure

```
project-folder/
│── main.py  # FastAPI application
│── files/   # Directory where uploaded files are stored
│── requirements.txt  # Dependencies
│── README.md  # Project documentation
```

## Dependencies

The required dependencies are listed in `requirements.txt`. You can install them using:

```sh
pip install -r requirements.txt
```

## License

This project is open-source and available under the [MIT License](LICENSE).

## Author

Stephen Kinuthia Kinyuru

**LinkedIn Profile:** [Stephen Kinuthia Kinyuru](https://www.linkedin.com/in/stephen-kinuthia-7b0702218/)

