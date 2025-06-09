from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.status import HTTP_302_FOUND
from config.connection import conn
from datetime import datetime



app_router = APIRouter()
templates = Jinja2Templates(directory="templates")
from datetime import datetime
from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.status import HTTP_302_FOUND
from config.connection import conn

app_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@app_router.get("/", response_class=HTMLResponse)
async def read_attend(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})



@app_router.post("/", response_class=HTMLResponse)
async def present(request: Request, Username: str = Form(...), Password: str = Form(...)):
    today = datetime.now().strftime("%Y-%m-%d")

    # Check if the user has already submitted for today
    existing_user = conn.attendence.attend.find_one({
        "Username": Username.lower(),
        "date": today
    })

    if existing_user:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "⚠️ You already submitted your response for today."
        })

    # Insert new attendance record
    conn.attendence.attend.insert_one({
        "Username": Username.lower(),
        "Password": Password.lower(),
        "date": today
    })

    return RedirectResponse(url="/home", status_code=HTTP_302_FOUND)



@app_router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app_router.get("/attendance", response_class=HTMLResponse)
async def show_attendance(request: Request):
    students = list(conn.attendence.attend.find())
    return templates.TemplateResponse("attendance.html", {
        "request": request,
        "students": students
    })


@app_router.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    return templates.TemplateResponse("logout.html", {"request": request})
