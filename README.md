# AuthCore API
Developed by: Kervin Philippe (tekprodige)


AuthCore API is a backend authentication and authorization system built with FastAPI.  
It provides user management, role-based access control (RBAC), and protected API routes.

## 🚀 Features

- User registration and management
- Role-based access control (Admin/User)
- Protected routes based on permissions
- RESTful API design
- Lightweight and easy to extend

## 🧱 Tech Stack

- Python
- FastAPI
- Uvicorn
- SQLite (for development)

## 📂 Project Structure

authcore/
│
├── main.py
├── models/        # Database models (coming soon)
├── routes/        # API routes (coming soon)
├── services/      # Business logic (coming soon)
└── README.md

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/tekprodige/AuthCore.git
cd authcore
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install fastapi uvicorn
```

4. Run the Server:

```bash
uvicorn main:app --reload
```

## Future Improvements

- JWT authentication
- Database integration (PostgreSQL)
- Password hashing (bcrypt)
- Role & permission system expansion
- Unit and integration tests
