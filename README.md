# Chat-GPT-Retrieval Plugin Setup

This is a GUI Tool for quickly setting up a Chat-GPT-Retrieval Plugin server to perform document retrieval with Pinecone datastore based on the document folder your specify. The other datastores will be implemented soon.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Requirements
- Python 3.x
- tkinter
- PyPDF2
- python-docx
- pandas
- beautifulsoup4
- openpyxl
- langchain
- pinecone

## Installation

1. Clone this repository:
git clone https://github.com/SergeSerb2/gui-chatgpt-retrieval.git

2. Move the gui.py and vectorizeAndUploadDocs.py files to the root of your ChatGPT Retrieval installation.

3. Install the required packages:
pip install -r requirements.txt


## Usage

1. Run the `gui.py` script:
python gui.py

2. Fill in the required fields (OpenAI API Key, Bearer Token, and Pinecone-specific environment variables) in the GUI.
3. Select the folder where your documents are stored. (Files supported range from .txt, .pdf, .doc/.docx, .xlsx, .csv, and many code files as well)
4. Click the "Submit" button.

Please note that if the index hasn't been created yet, an error is likely to occur. Simply rerun the program once the index is created, and no issues should persist. Once the server is running, you can access it at `localhost:3333`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
