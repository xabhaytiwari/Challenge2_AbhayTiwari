from diffusers import DiffusionPipeline
import torch

# Load model once (important for speed)
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float32,
    #use_safetensors=True,
    #variant="fp16"
)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe.to(device)


def get_image(prompt, output_path):

    image = pipe(prompt=prompt).images[0]

    image.save(output_path)
