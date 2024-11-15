from diffusers import StableDiffusionPipeline
import torch
import os

device = "cpu"
model= model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(device)

def generate_image(prompt, filename="generated_image.png"):
    try:
        print(f"Generating image for prompt: {prompt}")  # Debugging log

        # Generate the image based on the prompt
        image = model(prompt).images[0]
        
        # Define output directory and ensure it exists
        output_dir = "E:\Diffusion-Model\env\Model\generated_image"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Define full file path
        image_path = os.path.join(output_dir, filename)
        print(f"Saving image to: {image_path}")  # Debugging log

        # Save the generated image
        image.save(image_path)
        print("Image saved successfully")  # Confirmation log

        return image_path
    except Exception as e:
        print(f"Error in generate_image: {e}")
        raise

