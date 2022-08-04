# Firstly, install langdetect
# pip install langdetect
from langdetect import detect

# Input the text of any language to detect
text =  input ("Enter any text in any language: ")
print(detect(text))