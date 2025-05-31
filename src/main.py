from textnode import *

print("hello world")
text_node = TextNode("anchortext", "link", "https://www.boot.dev")
output = text_node.__repr__()
print(output)
