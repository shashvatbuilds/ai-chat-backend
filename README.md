# Eternal Chat Backend

AI-powered full-stack chat application backend built using FastAPI, PostgreSQL, SQLAlchemy, JWT Authentication, and OpenRouter AI integration.

---

# Features

- User Registration
- User Login Authentication
- JWT Token Authentication
- Protected Routes
- Conversation Management
- AI Chat System
- Persistent Message History
- Dynamic Conversation Titles
- Delete Conversations
- PostgreSQL Database Integration
- OpenRouter AI Integration

---

# Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- OpenRouter API
- Python
- Alembic (optional)
- Pydantic

---

# Project Structure

```bash
app/
│
├── auth/
├── core/
├── models/
├── routers/
├── schemas/
├── services/
├── utils/
│
├── config.py
├── database.py
└── main.py
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/eternal-chat-backend.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` file:

```env
APP_NAME=Eternal Chat Backend

DATABASE_URL=your_database_url

SECRET_KEY=your_secret_key

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

OPENROUTER_API_KEY=your_openrouter_api_key
```

---

# Run Server

```bash
uvicorn app.main:app --reload
```

---

# API Documentation

Swagger Docs:

```bash
http://127.0.0.1:8000/docs
```

---

# Main API Endpoints

## Authentication

- POST `/auth/register`
- POST `/auth/login`
- GET `/auth/me`

---

## Conversations

- GET `/conversations`
- POST `/conversations`
- PUT `/conversations/{id}`
- DELETE `/conversations/{id}`

---

## Messages

- GET `/messages/{conversation_id}`

---

## AI Chat

- POST `/chat`

---

# Frontend Repository

Frontend is built using:

- React
- Tailwind CSS
- React Router

---

# Author

Shashvat Yadav

GitHub:
https://github.com/Shashvat3