# Manifesto Comparison Engine

AI-powered platform for comparing political manifestos using NLP, semantic similarity, and policy shift analysis.

## Features

- Semantic manifesto comparison
- Topic distribution analysis
- Policy shift detection
- Interactive React dashboard
- PDF upload support
- FastAPI backend

## Tech Stack

### Frontend
- React
- Axios
- Recharts

### Backend
- FastAPI
- Sentence Transformers
- Scikit-learn
- PyPDF

## Architecture

PDF Upload
↓
Text Extraction
↓
Preprocessing
↓
Semantic Similarity
↓
Policy Shift Analysis
↓
Dashboard Visualizations



## Run Locally

### Backend

```bash
cd backend
uvicorn app:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Screenshots

### Dashboard

![Dashboard](screenshots/dashboard-charts.png)

### Upload Page
  ![Upload Page](screenshots/uploads_page.png)