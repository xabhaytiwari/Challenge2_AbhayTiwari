from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
from pydantic import BaseModel
from visual_local import get_image
from prompt_local import generate_prompt

class Sentence(BaseModel):
    sentence: str


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

def create_visual_prompt(scene):

    return generate_prompt(scene)


@app.post("/process")
async def process_text(data: Sentence):

    text = data.sentence

    scenes = [s.strip() for s in text.split(".") if s.strip()]

    # 5 Scenes max limit (AMD Laptop!)
    scenes = scenes[:5]

    storyboard = []

    for i, scene in enumerate(scenes):

        prompt = create_visual_prompt(scene)

        image_path = f"static/output_{i}.png"

        get_image(prompt, image_path)

        storyboard.append({
            "scene": scene,
            "image": f"/{image_path}"
        })

    return {"storyboard": storyboard}
