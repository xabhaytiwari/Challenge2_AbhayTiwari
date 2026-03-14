from diffusers import DiffusionPipeline
import torch

# Load model once (important for speed)
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16"
)

pipe.to("cuda")


def get_image(prompt, output_path):

    image = pipe(prompt=prompt).images[0]

    image.save(output_path)
