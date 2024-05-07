import random
import os

characters = {"Disney" : ["Rapunzel", "Cinderalla", "Ariel", "Belle", "Jasmine"],
              "Marvel" : ["Iron Man", "Captain America", "Thor", "Hulk", "Spiderman", "Black Panther", "Doctor Strange", "Captain Marvel"],
              "Avatar" : ["Avatar"],
              "Pirates of the Caribbean" : ["Jack Sparrow", "Will Turner"],
              "Star Wars" : ["Darth Vader", "Star Wars"]}

base_path = os.getcwd()

images = ["Angelina Jolie", "Brad Pitt", 
          "Megan Fox", "Natalie Portman",
          "Sandra Bullock", "Tom Hanks"]

sub_images = os.listdir(os.path.join(base_path, images[0]))

edited_json = {}
iter = 0
images = ["Angelina Jolie", "Brad Pitt", 
          "Megan Fox", "Natalie Portman",
          "Sandra Bullock", "Tom Hanks"]

for i in range(0, len(images)):
    sub_images = os.listdir(os.path.join(base_path, images[i]))
    for img in sub_images:
        # choose a random character
        character = random.choice(list(characters.keys()))
        # choose a random character from the list
        char = random.choice(characters[character])

        prompt = f"Turn {images[i]} into {char}"
        edited_prompt = f"{images[i]} as {char}"
        edited_json[iter] = {"prompt": prompt, "input_image": os.path.join(images[i], img), "edited_prompt": edited_prompt}
        iter += 1

import PIL
import requests
import torch

from diffusers import StableDiffusionInstructPix2PixPipeline

model_id = "MODEL-NAME"
pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float16, local_files_only=True).to("cuda")
generator = torch.Generator("cuda").manual_seed(0)

# image = download_image(url)
for img in edited_json:
    image = PIL.Image.open(os.path.join(base_path, edited_json[img]["input_image"]))
    prompt = edited_json[img]["prompt"]
    num_inference_steps = 20
    image_guidance_scale = 1.5
    guidance_scale = 10

    edited_image = pipe(prompt, 
       image=image, 
       num_inference_steps=num_inference_steps, 
       image_guidance_scale=image_guidance_scale, 
       guidance_scale=guidance_scale,
       generator=generator,
    ).images[0]

    edited_image.save(os.path.join(base_path, f"edited_images/{edited_json[img]['edited_prompt']}_{img}.png"))
    # update the json
    edited_json[img]["edited_image"] = f"edited_images/{edited_json[img]['edited_prompt']}_{img}.png"

# make folders for the images and text
os.makedirs(os.path.join(base_path, "image"), exist_ok=True)
os.makedirs(os.path.join(base_path, "text"), exist_ok=True)

for img in edited_json:
    try:
      edited_image = PIL.Image.open(os.path.join(base_path,edited_json[img]["edited_image"]))
      prompt = edited_json[img]["edited_prompt"]
      edited_image.save(os.path.join(base_path,f"image/{img}.png"))
      with open(os.path.join(base_path,f"text/{img}.txt"), "w") as f:
          f.write(prompt)
      f.close()
      print(prompt)
    except:
      continue
