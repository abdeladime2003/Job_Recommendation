from src.classes.PdfExtractText import PdfExtractText
from src.classes.LLMTextToDict import LLMTextToDict
from src.classes.MongoDbStorage import MongoDbStorage

text = PdfExtractText(r"C:\Users\Lakhal Badr\Downloads\English_Resume_24_25.pdf", 'classic').extract()
data = LLMTextToDict(text).pormpt_llm()

db = MongoDbStorage("cvs_db", "cvs_collection")

db.store_dictionary(data)
db.close()