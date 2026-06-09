from fastapi import FastAPI
from services.pdf_parser import extract_text
from services.preprocess import clean_text
from services.similarity import compare_documents
from services.policy_shift import detect_policy_shift
from services.manifesto_analyzer import analyze_manifesto
from fastapi import UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/compare-manifestos")
async def compare_manifestos(
    file1: UploadFile = File(...),
    file2: UploadFile = File(...)
):

    os.makedirs("uploads", exist_ok=True)

    path1 = f"uploads/{file1.filename}"
    path2 = f"uploads/{file2.filename}"

    with open(path1, "wb") as buffer:
        shutil.copyfileobj(
            file1.file,
            buffer
        )

    with open(path2, "wb") as buffer:
        shutil.copyfileobj(
            file2.file,
            buffer
        )

    doc1 = clean_text(
        extract_text(path1)
    )

    doc2 = clean_text(
        extract_text(path2)
    )

    similarity = compare_documents(
        doc1,
        doc2
    )

    shifts = detect_policy_shift(
        doc1,
        doc2
    )

    return {
        "similarity_score": similarity,
        "policy_shifts": shifts
    }

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "message": "Upload successful",
        "path": file_path
    }

@app.post("/analyze")
async def analyze_pdf(
    file: UploadFile = File(...)
):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = analyze_manifesto(
        file_path
    )

    return result

@app.get("/manifesto-analysis")
def manifesto_analysis():

    result = analyze_manifesto(
        "data/BJP_2024.pdf"
    )

    return result



@app.get("/")
def home():
    return {"message": "NEW VERSION"}


@app.get("/compare")
def compare():

    doc1 = extract_text(
        "data/BJP_2019.pdf"
    )

    doc2 = extract_text(
        "data/BJP_2024.pdf"
    )

    doc1 = clean_text(doc1)
    doc2 = clean_text(doc2)

    similarity = compare_documents(
        doc1,
        doc2
    )

    shifts = detect_policy_shift(
        doc1,
        doc2
    )

    return {
        "similarity_score": similarity,
        "policy_shifts": shifts
    }
import os

@app.get("/test")
def test():
    return {
        "cwd": os.getcwd()
    }