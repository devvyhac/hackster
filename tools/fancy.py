from art import text2art
import art
from random import choice

#print(art.font_list())

heading = [
  "avatar", "doom", 
  "bulbhead",
  "double", 
  "glenym", "puffy"]
  
typo = [
  "fari", "blackbubble",
  "blacksquare", "whitebubble",
  "whitesquare", "fancy19", 
  "fancy33", "fancy127", "love1",
  "love2", "native_lands"
]

def fancy_text(text, font=choice(heading)):
  return text2art(text, font=font)

def fancy_typo(text, font=choice(typo)):
  return text2art(text, font=font)

#for i in heading:
#  print(i)
#  print(fancy_text("Auth Hoard", font=i))
