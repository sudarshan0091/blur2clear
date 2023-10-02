import streamlit as st
import io
import numpy as np
from PIL import Image
import stablediffusion.client as sdc


def convert_blur_to_clear(image):
  """Converts a blur image into a clear image using Stable Diffusion.

  Args:
    image: A PIL Image object.
p
  Returns:
    A PIL Image object of the clear image.
  """

  # Convert the PIL Image object to a NumPy array.
  image_array = np.array(image)

  # Create a Stable Diffusion client.
  client = sdc.Client()

  # Generate a clear image from the blur image.
  clear_image_array = client.generate(image_array)

  # Convert the NumPy array back to a PIL Image object.
  clear_image = Image.fromarray(clear_image_array)

  return clear_image


st.title("Blur Image to Clear Image Converter")

# Upload image
uploaded_image = st.file_uploader("Upload image")

# Display image
if uploaded_image is not None:
  image = Image.open(uploaded_image)
  st.image(image)

# Allow users to edit image
edited_image = st.image(image, use_column_width=True)

# Option to convert image to clear image
if st.button("Convert to clear image"):
  clear_image = convert_blur_to_clear(edited_image)
  st.image(clear_image)

