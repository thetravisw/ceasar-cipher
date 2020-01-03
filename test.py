import pytest 
from main import *

def test_1():
  i=3
  while i < 30:
    txt = "Hello, I love you, won't you tell me your name?"
    enc_txt = cypher (txt,i)
    dec_text = decrypt(enc_txt,i)
    assert txt == dec_text
    i+=5

def test_codebreaker():
  txt = "Hello, I love you, won't you tell me your name?"
  enc_txt = cypher (txt,17)
  dec_text = solve(enc_txt)
  assert enc_txt == dec_text
