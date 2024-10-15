import streamlit as st
import os
import time
from PIL import Image
from diffusers import StableDiffusionPipeline
import torch

st.title("Text-to-Image Generator with Stable Diffusion")
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id).to("cuda")


prompt = st.text_input("Enter a text prompt:")


if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            try:
               


               
       
          
                
                image = pipe(prompt).images[0]
           
                st.image(image, caption="Generated Image", use_column_width=True)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a text prompt to generate an image.")
