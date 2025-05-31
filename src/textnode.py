from enum import Enum

class TextType(Enum):
    NORMAL = 'text'
    BOLD = '*text*'
    ITALIC = '_text_'
    CODE= '`text`'
    LINK = '[text](url)'
    IMAGE = '![alt_text](url)'

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text != other.text:
            return False
        if self.text_type != other.text_type:
            return False
        if self.url != other.url:
            return False
        return True
    
    def __repr__(self):
        return (
                "TextNode("
                + f"{self.text}, "
                + f"{self.text_type}, "
                + f"{self.url})"
                )
