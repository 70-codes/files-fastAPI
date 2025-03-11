import os
import shutil

from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/")
async def root():
    """_summary_

    Returns:
        _type_: json with default greeting
    """
    return {"message": "Hello World"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    """Upload a file to the server

    Args:
        file (UploadFile): The file to be uploaded

    Returns:
        dict: JSON response with file information or error message
    """
    try:
        # Make sure the directory exists
        os.makedirs("files", exist_ok=True)

        # Create the full path
        path = f"files/{file.filename}"

        # Check if the file has a name
        if not file.filename:
            raise HTTPException(status_code=400, detail="No filename provided")

        # Save the file
        with open(path, "w+b") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Return success response
        return {
            "status": "success",
            "message": "File uploaded successfully",
            "filename": path,
            "type": file.content_type,
        }

    except Exception as e:
        # Handle general exceptions
        raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")


@app.get("/download/{filename}", response_class=FileResponse)
async def get_file(filename: str):
    """_summary_

    Args:
        filename (str): string of the filename that you want to fetch from the server

    Raises:
        HTTPException: raises 404 error if the file is not found in th server

    Returns:
        _type_: returns the file from the server if the file is found and if the 404 exception is not raised
    """

    path = f"files/{filename}"

    # Check if file exists
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")

    # This will directly serve the file to the client
    return path


app.mount("/files", StaticFiles(directory="files"), name="files")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000)
