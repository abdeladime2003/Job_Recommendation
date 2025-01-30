class StrategyException(Exception):
    """
    Exception raised when the strategy to extract text from a PDF is invalid.

    This exception is triggered if the strategy is set to a value other than 'classic' or 'ocr'.

    Attributes:
        message (str): Explanation of the error.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"