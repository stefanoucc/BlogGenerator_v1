# baselineproject
First project using LLms
# Baseline Project

## Overview

This project is the first implementation using Large Language Models (LLMs). It is designed to generate blogs based on user input, leveraging the powerful capabilities of Meta-Llama.

## Features

- **Blog Generation**: Generate blogs for different job profiles based on a given topic and word count.
- **Streamlit Integration**: User-friendly interface built with Streamlit for easy interaction.
- **Hugging Face Integration**: Utilizes transformers from Hugging Face for natural language processing.

## Setup

### Prerequisites

- Python 3.8+
- Git
- Virtual Environment

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/stefanoucc/baselineproject.git
    cd baselineproject
    ```

2. **Create and Activate Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Hugging Face Token**
    - Add your Hugging Face token in the script or set it as an environment variable.

## Usage

1. **Run the Streamlit App**
    ```bash
    streamlit run app.py
    ```

2. **Interact with the Interface**
    - Enter the blog topic.
    - Specify the number of words.
    - Choose the target audience (Researchers, Data Scientist, Common People).
    - Click "Generate" to create the blog.

## Project Structure

- `app.py`: Main application script for Streamlit.
- `requirements.txt`: List of dependencies.

## Contributing

1. **Fork the Repository**
2. **Create a Feature Branch**
    ```bash
    git checkout -b feature-branch
    ```
3. **Commit Changes**
    ```bash
    git commit -m "Add new feature"
    ```
4. **Push to Branch**
    ```bash
    git push origin feature-branch
    ```
5. **Open a Pull Request**

## License

This project is licensed under the MIT License.

## Acknowledgements

- [Hugging Face](https://huggingface.co/)
- [Streamlit](https://streamlit.io/)
- [Meta-Llama](https://github.com/facebookresearch/metaseq/tree/main/projects/OPT)

