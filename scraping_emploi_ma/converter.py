import json

class Converter:
    @staticmethod
    def to_json(data):
        return json.dumps(data, ensure_ascii=False, indent=4)
