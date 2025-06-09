# 📋 Student Attendance System

A web-based attendance system built with **FastAPI**, **MongoDB**, and **HTML/CSS**, allowing students to log in and mark attendance, while teachers can view daily attendance records.

---

## 🚀 Features

- 🌐 **Login System** for students
- ✅ **Prevents duplicate submissions** (once per day per student)
- 📅 **Tracks attendance by date**
- 📄 **Dashboard** to view all records
- 🎨 **Responsive UI** using HTML & CSS
- 🔒 Secure data handling with validation
- 🧾 Organized templates with Jinja2

---

## 🛠️ Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [MongoDB](https://www.mongodb.com/)
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Tools**: Uvicorn, Pydantic

---

## 🧑‍🏫 How It Works

### 🧩 For Teacher
1. Run the FastAPI server.
2. Share the URL (e.g., `http://localhost:8000`) with students.
3. Visit `/attendance` to see who logged in.

### 🎓 For Student
1. Visit the login page.
2. Enter your **Username** and **Password** (dummy for now).
3. If already marked for today, it will show an error.
4. Upon success, you'll be redirected to the home/dashboard.

---

❗ Password is stored in plain text (for demo purposes). Never do this in production.

❗ No authentication/session implemented.

✅ Each user can submit only once per day using date-based validation.

💡 Future Improvements
Add authentication (JWT or OAuth2)

Password hashing (bcrypt)

Admin login panel

CSV export for attendance

Date-based filters in dashboard

Deployment on Render / Vercel
