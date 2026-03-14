# The Pitch Visualizer
The Pitch Visualizer is a generative AI application that transforms a text narrative into a sequence of storyboard frames, created as an Assignment for the role of AI Engineer at Darwix AI by **Abhay Tiwari**. It uses a Large Language Model (LLM) to enhance simple sentences into detailed cinematic prompts, and a diffusion model to render those prompts into high-quality images. The application is served via a FastAPI backend and features a hacker-themed, terminal-style web interface.

## Features
- **Automated Storyboarding:** Automatically splits narrative text into distinct scenes (up to 5 scenes per run).

- **Cinematic Prompt Engineering:** Utilizes `Qwen/Qwen2.5-7B-Instruct` to expand basic scene descriptions into highly detailed, cinematic text-to-image prompts.

- **High-Quality Image Generation:** Uses `stabilityai/stable-diffusion-xl-base-1.0`(SDXL) to generate visual representations of the scenes.
- **Sleek Terminal UI:** Features a minimalist, retro-hacker aesthetic(me) interface built with raw HTML, CSS, and JavaScript (not a web-developer!).
- **FastAPI Backend:** Provides a lightweight, asynchronous backend for processing requests and serving static files.

## Prerequisites
To run this project, you will need to have Conda (Miniconda or Anaconda) installed on your system to manage the dependencies.

## Installation
- **Clone the repository (or navigate to the project directory)**:
>`cd Challenge2_AbhayTiwari`
- **Create the Conda environment using the provided `environment.yml` file**:
>`conda env create -f environment.yml`
- **Activate the environment:**
>`conda activate tthe_pitch_visualiser`
- **Prepare Static Directory:**
>`mkdir static`


## Usage
1. **Start the FastAPI server using Uvicorn:**
>`uvicorn main:app --reload`
2. **Access the Web Interface:**
Open your web browser and navigate to `http://127.0.0.1:8000.`
3. **Generate a Storyboard**
    - Enter your narrative in the text box. 

    - Click the `run_visualizer()` button.

    - The application will process each sentence, generate a cinematic prompt, render the image, and display the final storyboard on the screen. *(Note: Processing time depends heavily on your GPU hardware).*

## Project Essentials (Apart from me!)
              
`├── environment.yml            # Conda environment specifications and dependencies`

`├── main.py                    # FastAPI server setup and routing`

`├── prompt_local.py               # Houses the LLM logic. It loads Qwen/Qwen2.5-7B-Instruct.`

`├── visual_local.py     # Image Generation Logic`

`├── static/output_{*}           # The generated images served to the frontend`

`├── templates/index.html             # The frontend user interface`

## Models Used

https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0

https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
