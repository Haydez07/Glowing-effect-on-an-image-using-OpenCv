# -*- coding: utf-8 -*-
"""DIP_CEC

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1v7oJs1PTn2QqGGZoJG_A3oOMYcmMXWFw

###Soft Glow effect on Images "


##What is going to be :
Effect: Adds a soft glow with a blurred, brightened layer blended over the original image.
"""

from PIL import Image, ImageFilter, ImageEnhance
from google.colab import files
import io
import matplotlib.pyplot as plt

def apply_soft_glow(input_image):
    # Convert image to RGBA
    img = input_image.convert("RGBA") # Convert the image into RGBA (RED, GREEN , BLUE, ALPHA CHANNEL)

    # Increase brightness slightly for a glowing base
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(1.2) # Applies Enhancement means i'm increasing the brightness by 20%
    # 1.0 = Original Brightness, < 1.0 = Darker , > 1.0 = Brighter

    # Create a blurred version of the image for the glow
    glow = img.filter(ImageFilter.GaussianBlur(radius=10)) # creates a blur where the intensity spreads outward from each pixel
    # r =1 slight Softening , r = 5 visible blur , r = 10 strong glow

    # Increase brightness and saturation of the glow layer
    enhancer = ImageEnhance.Brightness(glow)
    glow = enhancer.enhance(1.5) # blurred the image brighter by 50%
    enhancer = ImageEnhance.Color(glow)
    glow = enhancer.enhance(1.3) # increase the color saturation of the glow by 30%

    # Blend the original image with the glowing layer
    soft_glow_img = Image.blend(glow, img, 0.4) #It softly mixes the glowing blur with the original image to create a dreamy, glowing effect
    # 0.6 gives the 60% weight of the original image

    return soft_glow_img

# Upload an image
uploaded = files.upload()

# Process the uploaded image
for filename in uploaded.keys():
    # Open the uploaded image
    input_image = Image.open(io.BytesIO(uploaded[filename]))

    # Apply the soft glow effect
    output_image = apply_soft_glow(input_image)

    # Display original and output images side by side
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(input_image)
    axes[0].set_title("Original Image")
    axes[0].axis("off")

    axes[1].imshow(output_image)
    axes[1].set_title("Soft Glow Image")
    axes[1].axis("off")

    plt.show()

    # Save the output image
    output_filename = "glow_" + filename
    output_image.save(output_filename, "PNG")
    print(f"Saved as {output_filename}")

    # Download the result
    #files.download(output_filename)