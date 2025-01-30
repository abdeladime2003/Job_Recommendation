import os
import sys
import logging
from PIL import Image
import io

import fitz
import pytesseract

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.Exceptions.StrategyException import StrategyException


class PdfExtractText:
    """
    A class to extract text from PDF files using either classic text extraction or OCR methods.

    The class supports two strategies:
    - 'classic': Direct text extraction by iterating through PDF pages
    - 'ocr': Optical Character Recognition using Tesseract OCR engine

    Attributes:
        __file_path (str): Path to the PDF file
        __strategy (str): Selected extraction strategy ('classic' or 'ocr')
    """
    STRATEGIES = {'ocr', 'classic'}

    def __init__(self, file_path: str, strategy: str):
        self.logger = logging.getLogger(__name__)

        self.__file_path = file_path

        try:
            self.check_strategy(strategy=strategy)
            self.__strategy = strategy
        except StrategyException as e:
            self.logger.error(f"Problem occured while setting the strategy: {e}")


    @property
    def strategy(self):
        return self.__strategy

    @property
    def file_path(self):
        return self.__file_path

    @strategy.setter
    def strategy(self, new_strategy):
        self.check_strategy(new_strategy)
        self.__strategy = new_strategy

    @file_path.setter
    def file_path(self, new_file_path):
        self.__file_path = new_file_path


    @staticmethod
    def check_strategy(strategy):
        """
        Validate if the provided strategy is supported.

        Args:
            strategy (str): Strategy to validate

        Raises:
            StrategyException: If strategy is not in STRATEGIES set
        """       
        if strategy not in PdfExtractText.STRATEGIES:
            raise StrategyException(f"Invalid Strategy: '{strategy}'. Allowed strategies are 'classic' or 'ocr'.") 


    def extract_classic(self) -> str:
        """
        Extract text from PDF using classic method.

        Returns:
            str: Extracted text from the PDF, or empty string if extraction fails
        """
        doc = None
        text = ""
        try:
            doc = fitz.open(self.file_path)
        except Exception as e:
            self.logger.error(f"Problem occured while reading the input file: {e}")
            return text

        self.logger.info("Starting extraction using classic method...")

        if doc:
            for page in doc:
                try:
                    text += page.get_text()
                except Exception as e:
                    self.logger.error(f"Error extracting text from page {page.number}: {e}")
                    continue
            
            if text:
                self.logger.info("Text is extracted successfully!")
            else:
                self.logger.warning("No text extracted from the document.")

        return text


    @staticmethod
    def is_windows() -> bool:
        """
        Check if the current operating system is Windows or Unix/Linux.

        Returns:
            bool: True if running on Windows, False if running on Unix/Linux
        """
        return os.name == 'nt'      # true if windows, false if unix ('posix')


    def extract_ocr(self) -> str:
        """
        Extract text from PDF using OCR (Optical Character Recognition).

        This method first converts each page to an image and then uses Tesseract OCR
        to extract text from the images.

        Returns:
            str: Extracted text from the PDF, or empty string if extraction fails
        """
        if self.is_windows():
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        doc = None
        text = ""
        try:
            doc = fitz.open(self.file_path)
        except Exception as e:
            self.logger.error(f"Problem occured while reading the input file: {e}")
            return text

        self.logger.info("Starting extraction using ocr method...")

        if doc:
            for page_num in range(len(doc)):
                try:
                    page = doc[page_num]

                    pix = page.get_pixmap()
                    img = Image.open(io.BytesIO(pix.tobytes("png")))

                    text += pytesseract.image_to_string(img)
                except Exception as e:
                    self.logger.error(f"Problem occured while converting text page into image: {e}")
                    continue
            if text:
                self.logger.info("Text is extracted successfully!")
            else:
                self.logger.warning("No text extracted from the document.")
        return text


    def extract(self) -> str:
        """
        Extract text using the configured strategy.

        Returns:
            str: Extracted text from the PDF using either classic or OCR method
        """
        if self.strategy == "classic":
            return self.extract_classic()
        else:   # ocr case
            return self.extract_ocr()