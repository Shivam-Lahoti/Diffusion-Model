from diffusers import StableDiffusionPipeline
import os

device = "cpu"
model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(device)

def generate_image(prompt, filename="generated_image.png"):
    try:
        print(f"Generating image for prompt: {prompt}")

        # Ensure the output directory exists
        output_dir = "E:/Diffusion-Model/env/Model/generated_image"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        

        # Generate the image
        image_path = os.path.join(output_dir, filename)
        image = model(prompt).images[0]
        image.save(image_path)
        print(f"Image saved successfully at {image_path}")

        return image_path
    except Exception as e:
        print(f"Error in generate_image: {e}")
        raise
