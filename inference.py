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

# for i in range(0, len(images)):
#     sub_images = os.listdir(os.path.join(base_path, images[i]))
#     for img in sub_images:
#         # choose a random character
#         character = random.choice(list(characters.keys()))
#         # choose a random character from the list
#         char = random.choice(characters[character])

#         prompt = f"Turn {images[i]} into {char}"
#         edited_prompt = f"{images[i]} as {char}"
#         edited_json[iter] = {"prompt": prompt, "input_image": os.path.join(images[i], img), "edited_prompt": edited_prompt}
#         iter += 1

edited_json = {0: {'prompt': 'Turn Angelina Jolie into Captain Marvel',
  'input_image': 'Angelina Jolie/019_57ab290d.jpg',
  'edited_prompt': 'Angelina Jolie as Captain Marvel'},
 1: {'prompt': 'Turn Angelina Jolie into Avatar',
  'input_image': 'Angelina Jolie/005_582c121a.jpg',
  'edited_prompt': 'Angelina Jolie as Avatar'},
 2: {'prompt': 'Turn Angelina Jolie into Darth Vader',
  'input_image': 'Angelina Jolie/100_31ff9373.jpg',
  'edited_prompt': 'Angelina Jolie as Darth Vader'},
 3: {'prompt': 'Turn Angelina Jolie into Jack Sparrow',
  'input_image': 'Angelina Jolie/060_4037f0f7.jpg',
  'edited_prompt': 'Angelina Jolie as Jack Sparrow'},
 4: {'prompt': 'Turn Angelina Jolie into Star Wars',
  'input_image': 'Angelina Jolie/094_c255b703.jpg',
  'edited_prompt': 'Angelina Jolie as Star Wars'},
 5: {'prompt': 'Turn Angelina Jolie into Will Turner',
  'input_image': 'Angelina Jolie/099_c22d3e48.jpg',
  'edited_prompt': 'Angelina Jolie as Will Turner'},
 6: {'prompt': 'Turn Angelina Jolie into Will Turner',
  'input_image': 'Angelina Jolie/004_f61e7d0c.jpg',
  'edited_prompt': 'Angelina Jolie as Will Turner'},
 7: {'prompt': 'Turn Brad Pitt into Will Turner',
  'input_image': 'Brad Pitt/028_181cbb8a.jpg',
  'edited_prompt': 'Brad Pitt as Will Turner'},
 8: {'prompt': 'Turn Brad Pitt into Avatar',
  'input_image': 'Brad Pitt/069_8533eee4.jpg',
  'edited_prompt': 'Brad Pitt as Avatar'},
 9: {'prompt': 'Turn Brad Pitt into Rapunzel',
  'input_image': 'Brad Pitt/027_78f200c3.jpg',
  'edited_prompt': 'Brad Pitt as Rapunzel'},
 10: {'prompt': 'Turn Brad Pitt into Avatar',
  'input_image': 'Brad Pitt/083_d6f1d5ac.jpg',
  'edited_prompt': 'Brad Pitt as Avatar'},
 11: {'prompt': 'Turn Megan Fox into Avatar',
  'input_image': 'Megan Fox/003_61dd1e53.jpg',
  'edited_prompt': 'Megan Fox as Avatar'},
 12: {'prompt': 'Turn Megan Fox into Star Wars',
  'input_image': 'Megan Fox/008_74bda018.jpg',
  'edited_prompt': 'Megan Fox as Star Wars'},
 13: {'prompt': 'Turn Megan Fox into Doctor Strange',
  'input_image': 'Megan Fox/095_fc25a60b.jpg',
  'edited_prompt': 'Megan Fox as Doctor Strange'},
 14: {'prompt': 'Turn Megan Fox into Rapunzel',
  'input_image': 'Megan Fox/004_6aede3d3.jpg',
  'edited_prompt': 'Megan Fox as Rapunzel'},
 15: {'prompt': 'Turn Megan Fox into Captain Marvel',
  'input_image': 'Megan Fox/046_953d292e.jpg',
  'edited_prompt': 'Megan Fox as Captain Marvel'},
 16: {'prompt': 'Turn Natalie Portman into Avatar',
  'input_image': 'Natalie Portman/088_c6c7b0b2.jpg',
  'edited_prompt': 'Natalie Portman as Avatar'},
 17: {'prompt': 'Turn Natalie Portman into Will Turner',
  'input_image': 'Natalie Portman/089_7a22dd1d.jpg',
  'edited_prompt': 'Natalie Portman as Will Turner'},
 18: {'prompt': 'Turn Natalie Portman into Darth Vader',
  'input_image': 'Natalie Portman/056_666b6673.jpg',
  'edited_prompt': 'Natalie Portman as Darth Vader'},
 19: {'prompt': 'Turn Natalie Portman into Belle',
  'input_image': 'Natalie Portman/049_f7490e79.jpg',
  'edited_prompt': 'Natalie Portman as Belle'},
 20: {'prompt': 'Turn Natalie Portman into Avatar',
  'input_image': 'Natalie Portman/007_b82eb947.jpg',
  'edited_prompt': 'Natalie Portman as Avatar'},
 21: {'prompt': 'Turn Sandra Bullock into Jack Sparrow',
  'input_image': 'Sandra Bullock/028_5388c983.jpg',
  'edited_prompt': 'Sandra Bullock as Jack Sparrow'},
 22: {'prompt': 'Turn Sandra Bullock into Jack Sparrow',
  'input_image': 'Sandra Bullock/003_0e3303fc.jpg',
  'edited_prompt': 'Sandra Bullock as Jack Sparrow'},
 23: {'prompt': 'Turn Sandra Bullock into Belle',
  'input_image': 'Sandra Bullock/021_7ae7b9a5.jpg',
  'edited_prompt': 'Sandra Bullock as Belle'},
 24: {'prompt': 'Turn Sandra Bullock into Spiderman',
  'input_image': 'Sandra Bullock/054_81a12509.jpg',
  'edited_prompt': 'Sandra Bullock as Spiderman'},
 25: {'prompt': 'Turn Sandra Bullock into Ariel',
  'input_image': 'Sandra Bullock/019_7a6470ab.jpg',
  'edited_prompt': 'Sandra Bullock as Ariel'},
 26: {'prompt': 'Turn Tom Hanks into Ariel',
  'input_image': 'Tom Hanks/005_dac94cfe.jpg',
  'edited_prompt': 'Tom Hanks as Ariel'},
 27: {'prompt': 'Turn Tom Hanks into Belle',
  'input_image': 'Tom Hanks/064_898b4b7e.jpg',
  'edited_prompt': 'Tom Hanks as Belle'},
 28: {'prompt': 'Turn Tom Hanks into Jack Sparrow',
  'input_image': 'Tom Hanks/021_b7e22acc.jpg',
  'edited_prompt': 'Tom Hanks as Jack Sparrow'},
 29: {'prompt': 'Turn Tom Hanks into Darth Vader',
  'input_image': 'Tom Hanks/080_13b6a4b6.jpg',
  'edited_prompt': 'Tom Hanks as Darth Vader'}}

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
