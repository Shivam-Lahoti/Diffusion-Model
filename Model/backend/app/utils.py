from diffusers import StableDiffusionPipeline
import torch
import os

device = "cpu"
model= model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(device)

def generate_image(prompt,filename="generated_image.png"):
    image= model(prompt).images[0]
    output_dir= "E:\Diffusion-Model\env\Model\generated_image"
    image_path=os.path.join(output_dir, filename)
    image.save(image_path)
    return image_path
