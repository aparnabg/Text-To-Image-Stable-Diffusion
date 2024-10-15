# Text-To-Image-Stable-Diffusion
This repository contains a web app for text-to-image generation using the Stable Diffusion model. Built with Hugging Face's diffusers and Streamlit, it allows users to input a text prompt and generates an AI-created image. The app supports both CPU and GPU and is deployed on Hugging Face Spaces for easy access.

This repository contains a web-based application for **text-to-image generation** using the **Stable Diffusion** model. Users can input a text prompt, and the app generates an AI-created image based on the input.

The model is built with the Hugging Face **diffusers** library and utilizes **Streamlit** for the user interface. It supports both CPU and GPU execution, ensuring faster generation on GPUs while remaining flexible for other setups. The app is easily deployable and hosted on **Hugging Face Spaces**, making it publicly accessible.

## Demo

You can try the live app [here](#) (replace `#` with the URL of your Hugging Face Space).

## Features

- **Text-to-Image Generation**: Generate images based on text prompts using the Stable Diffusion model.
- **Streamlit Frontend**: User-friendly interface for inputting prompts and viewing generated images.
- **GPU Support**: Optimized for GPU acceleration for faster image generation.
- **Easy Deployment**: Deploy seamlessly on Hugging Face Spaces.

## Model and Libraries Used

- **Model**: [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5) by RunwayML.
- **Libraries**:
  - `torch`
  - `diffusers`
  - `transformers`
  - `streamlit`
  - `accelerate`

## Installation and Running Locally

To run this project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/aparnabg/Text-To-Image-Stable-Diffusion.git
   cd Text-To-Image-Stable-Diffusion

2. **Set up a virtual environment**:
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install the dependencies**:
    pip install -r requirements.txt

4. **Run the Streamlit app**:
    streamlit run app.py

5. **Run the Streamlit app**:
    Deployment
    The app is deployed on Hugging Face Spaces for easy access. To deploy it yourself:
        Push your code to a GitHub repository.
        Create a new Hugging Face Space and select Streamlit as the SDK.
        Sync your Hugging Face Space with the GitHub repository or manually upload the files.
        The app will automatically be built and deployed.

## License
This project is open-source and available under the MIT License.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions or improvements.

