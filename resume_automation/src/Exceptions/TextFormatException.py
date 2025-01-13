class TextFormatException(Exception):
    """
    Custom exception raised when the LLM output fails to meet JSON format requirements.
    
    This exception is specifically used when the LLM-generated text does not contain
    properly formatted JSON with opening and closing curly brackets. It helps in
    identifying and handling cases where the LLM output cannot be parsed as valid JSON.
    
    Attributes:
        message (str): The error message describing why the text format is invalid
    
    Example:
        >>> if not is_valid_json(text):
        >>>     raise TextFormatException("Missing closing bracket in LLM output")
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)
    
    def __str__(self):
        return f"{self.message}"