from diffusers import StableDiffusionPipeline
import torch

device ="cuda" if torch.cuda.is_available() else "cpu"
model= model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(device)

def generate_image(prompt):
    image= model(prompt).images[0]
    image_path="generated_image.png"
    image.save(image_path)
    return image_path
