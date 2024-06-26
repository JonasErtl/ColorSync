#imports
import numpy as np
from PIL import ImageGrab
from time import sleep
import requests

while True: 

    sleep(1)

    # Screenshot  
    screenshot = ImageGrab.grab()
    img_np = np.array(screenshot)
    pixels = img_np.reshape(-1,  3)

    # Calculate the average color
    average_color = pixels.mean(axis=0)

    #Home Assistant IP and Token
    ha_url = "replace_with_your_homeassistant_url"
    ha_token = "replace_with_your_homeassistant_token"

    headers = {
        "Authorization": f"Bearer {ha_token}",
        "content-type": "application/json",
    }

    # Homeassistent entity id of the desired light
    entity_id = "your_light.id"

    data = {
        "entity_id": entity_id,
        "rgb_color": [round(average_color[0]),  round(average_color[1]),  round(average_color[2])],  # RGB values 
        "transition":  5,  # Transition time in seconds
    }

    response = requests.post(f"{ha_url}/api/services/light/turn_on", headers=headers, json=data)

    if response.status_code ==  200:
        print("Light turned on successfully.")
    else:
        print("Failed to turn on light.")
