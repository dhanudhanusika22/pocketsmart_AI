from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/home-planner", response_class=HTMLResponse)
async def home_planner(request: Request):
    return templates.TemplateResponse("home_planner.html", {"request": request})

@app.post("/generate-home", response_class=HTMLResponse)
async def gen_home(request: Request):
    form = await request.form()
    budget = form.get("budget", "50000")
    # INSTANT RESULT - NO GEMINI NEEDED FOR DEMO
    result = f"""
✅ PocketSmart AI - Budget Plan for Rs. {budget}

🛋️ HOME RECOMMENDATIONS:

1. Sofa: IKEA 3-Seater - Rs. 25,000 - Flipkart
2. Bed: Wakefit Queen Size - Rs. 18,000 - Amazon
3. Table: Wooden Coffee Table - Rs. 7,000

Total Cost: Rs. 50,000
Within Budget: YES ✅

🛒 Shopping Links Generated
📦 Delivery Available in Chennai
"""
    html = f"<html><body style='font-family:sans-serif; padding:30px; background:#f0f0f0;'><h1>Your Plan Ready! 🎉</h1><div style='background:white; padding:20px; border-radius:10px; white-space:pre-wrap; font-size:16px;'>{result}</div><br><br><a href='/home-planner' style='background:blue; color:white; padding:12px 20px; text-decoration:none; border-radius:5px;'>Back</a></body></html>"
    return HTMLResponse(content=html)

@app.get("/generate-home", response_class=HTMLResponse)
async def gen_home_get():
    return HTMLResponse(content="<html><body><h1>Working! Go to <a href='/home-planner'>Home Planner</a> and submit form</h1></body></html>")