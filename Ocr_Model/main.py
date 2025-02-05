import os
import yaml
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from Ocr_Model.src.classes.PdfExtractText import PdfExtractText
from Ocr_Model.src.classes.LLMTextToDict import LLMTextToDict
from Ocr_Model.src.classes.MongoDbStorage import get_mongo_connection
import warnings

warnings.filterwarnings("ignore")
CONFIG_FILE = r"C:\Users\LENOVO\Desktop\project_job\Ocr_Model\config\main_config.yaml"

def load_config(config_file=CONFIG_FILE):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
        MIN_THRESHOLD = config["MIN_THRESHOLD"]
        return MIN_THRESHOLD
def main(file_path, user):
    File_path = file_path
    MIN_THRESHOLD = load_config()
    print(f"i get the file {file_path}")
    try :
        extracted_text = PdfExtractText(file_path=file_path, strategy="classic").extract()
        if len(extracted_text) <= MIN_THRESHOLD:
            extracted_text = PdfExtractText(file_path=file_path, strategy="ocr").extract()
        elif len(extracted_text) == 0:
            raise ValueError("Blank input pdf!")
        print("Text is extracted successfully!")
    except Exception as e:
        print(f"Error while extracting text: {e}")
        return None
    try:
        print("Formating the extracted text...")
        formated_text = LLMTextToDict(extracted_text).pormpt_llm()
        print("Text is formated successfully!")
    except Exception as e:
        print(f"Error while formating text: {e}")
        return None
    try:
        print("Storing data...")
        db = get_mongo_connection()
        formated_text["user"] = user
        db.insert_one(formated_text)
        print(f"{file_path} is processed and stored successfully in the database!")
    except Exception as e:
        print(f"Error while storing data: {e}")
        return None
    return formated_text["_id"]
if __name__ == "__main__":
    main()