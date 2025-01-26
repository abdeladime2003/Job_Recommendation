import os
import sys
import logging
import json
from typing import Dict

import yaml
from dotenv import load_dotenv
load_dotenv('.env')
import google.generativeai as genai

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.Exceptions.TextFormatException import TextFormatException

class LLMTextToDict:
    """
    A class that converts input text to a structured dictionary using Google's Generative AI.

    This class handles loading configurations, processing text through the LLM model,
    and converting the response into a structured dictionary format.

    Attributes:
        LLM_CONFIG_FILE (str): Path to the YAML configuration file for LLM settings
    """
    LLM_CONFIG_FILE = r"C:\Users\LENOVO\Desktop\project_job\resume_automation\config\llm_config.yaml"

    def __init__(self, text: str):
        """
        Initialize the LLMTextToDict instance.
        
        Args:
            text (str): The input text to be processed
        """
        self.logger = logging.getLogger(__name__)
        self.__input_text = text


    @property
    def resume_text(self):
        return self.__input_text
    
    @resume_text.setter
    def resume_text(self, new_input_text):
        self.__input_text = new_input_text


    def load_api(self) -> str:
        """
        Load the Gemini API key from environment variables.
        
        Returns:
            str: The API key for Google's Generative AI
        """
        try:
            API_KEY = "AIzaSyDNVRLBwEkz6KcOEsTXaEuLrHpUp94HJo0"
            return API_KEY
        except Exception as e:
            self.logger.error(f"Problem occured while reading from .env file: {e}")


    def load_config(self) -> Dict:
        """
        Load configuration settings from the YAML file.
        
        Returns:
            dict: Configuration settings
        """
        if not os.path.exists(LLMTextToDict.LLM_CONFIG_FILE):
            raise FileNotFoundError(f"Prompt file not found at {LLMTextToDict.LLM_CONFIG_FILE}")
        try:
            with open(LLMTextToDict.LLM_CONFIG_FILE, 'r') as file:
                config = yaml.safe_load(file)
            return config
        except Exception as e:
            self.logger.error(f"Problem while reading the config file {LLMTextToDict.LLM_CONFIG_FILE}: {e}")


    def load_prompt(self) -> str:
        """
        Load the prompt template from the file specified in the config.
        
        Returns:
            str: The prompt template
        """
        FILE_PATH = self.load_config()["prompt_file"]
        if not os.path.exists(FILE_PATH):
            raise FileNotFoundError(f"Prompt file not found at {FILE_PATH}")
        try:
            with open(FILE_PATH, 'r') as file:
                return file.read()
        except Exception as e:
            self.logger.error(f"Problem occured while reading the prompt file {FILE_PATH}: {e}")


    @staticmethod
    def process_text(text) -> Dict:
        """
        Extract and parse JSON data from the text response.
        
        Looks for content enclosed in curly braces and attempts to parse it as JSON.
        
        Args:
            text (str): The text containing JSON data
            
        Returns:
            dict: Parsed JSON data
        """
        start_idx, end_idx = None, None
        for idx in range(len(text)):
            if start_idx is not None and end_idx is not None:
                break

            if text[idx] == '{' and start_idx is None:
                start_idx = idx
            if text[len(text)-1-idx] == '}' and end_idx is None:
                end_idx = len(text) - idx - 1

        if start_idx is not None and end_idx is not None:
            try:
                data = json.loads(text[start_idx: end_idx+1])
                return data     # Dictionnary
            except Exception as e:
                raise ValueError(f"Problem occurred while transforming the text into a dictionary: {e}")
        else:
            raise TextFormatException("Invalid curly brackets found in the text.")


    def pormpt_llm(self) -> Dict:
        """
        Process the input text through the LLM model and convert the response to a dictionary.
        
        This method:
        1. Configures the Gemini AI with the API key
        2. Creates the full prompt by combining the template with input text
        3. Generates content using the LLM
        4. Processes the response into a dictionary
        
        Returns:
            dict: Structured data extracted from the LLM response
        """
        input_example = f"\nthe text:\n{self.resume_text}"
        try:
            genai.configure(api_key=self.load_api())
            model = genai.GenerativeModel(self.load_config()["model"])
            prompt = self.load_prompt() + input_example
            response = model.generate_content(prompt)
            
            data = self.process_text(response.text)
            return data
        except Exception as e:
            self.logger.error(f"Problem occured while prompting the LLM: {e}")
    

    @staticmethod
    def save_as_json(data, save_path):
        """
        Save the dictionary data as a JSON file.
        
        Args:
            data (dict): The data to be saved
            save_path (str): The path where the JSON file will be saved
        """
        with open(save_path, 'w') as json_file:
            json.dumps(data, json_file, indent=4)
        print(f"JSON file saved as {save_path}")