import os
import glob
import yaml
from src.classes.PdfExtractText import PdfExtractText
from src.classes.LLMTextToDict import LLMTextToDict
from src.classes.MongoDbStorage import get_mongo_connection
import warnings
warnings.filterwarnings("ignore")
CONFIG_FILE = r"C:\Users\LENOVO\Desktop\project_job\resume_automation\config\main_config.yaml"

def load_config(config_file=CONFIG_FILE):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
        FOLDER_PATH = config["uploads_path"]
        MIN_THRESHOLD = config["MIN_THRESHOLD"]
        return FOLDER_PATH, MIN_THRESHOLD
    
def get_sorted_files(folder_path: str):
    try:
        files = glob.glob(os.path.join(folder_path, "*.pdf"))
        return sorted(files, key=os.path.getmtime)
    except Exception as e:
        print(f"Problem occured while reading from {folder_path}: {e}")
def main():
    FOLDER_PATH, MIN_THRESHOLD = load_config()
    files_path = get_sorted_files(folder_path=FOLDER_PATH)
    print(f"Found {len(files_path)} files in the folder: {FOLDER_PATH}")
    for file_path in files_path:
        print(f"Extracting text from {file_path}...")
        extracted_text = PdfExtractText(file_path=file_path, strategy="classic").extract()
        if len(extracted_text) <= MIN_THRESHOLD:
            extracted_text = PdfExtractText(file_path=file_path, strategy="ocr").extract()
        elif len(extracted_text) == 0:
            raise ValueError("Blank input pdf!")
        print("Text is extracted successfully!")
        print("Formating the extracted text...")
        formated_text = LLMTextToDict(extracted_text).pormpt_llm()
        print("Text is formated successfully!")
        print(formated_text)
        print("Storing data...")
        db = get_mongo_connection()
        db.insert_one(formated_text)
        print(f"{file_path} is processed and stored successfully in the databse!")
        print("---------------------------------------------------")
    print("All files are processed and stored successfully in the databse!")



if __name__ == "__main__":
    main()