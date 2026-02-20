from gutenbergpy import textget
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

def __check_punkt():
  try:
    nltk.data.find('tokenizers/punkt')
  except LookupError:
    nltk.download('punkt')

def __check_punkt_tab():
  try:
    nltk.data.find('tokenizers/punkt_tab')
  except LookupError:
    nltk.download('punkt_tab')  

def get_book(id:int) -> str:
  """This will return a Project Gutenberg book
  as a utf-9 string with the headers stripped.

  Args:
      id (int): The Project Gutenberg book id

  Returns:
      (str): The book
  """
  book = textget.get_text_by_id(id)
  book_str = (
    textget.strip_headers(book)
    .decode()
    .strip()
  )
  return book_str


def get_punkt_tokens(text:str) -> list[str]:
  """Given an input string, will return the 
  tokenized string using the punkt tokenizer.

  Args:
      text (str): The string to tokenize

  Returns:
      (list[str]): A list of tokens
  """
  __check_punkt()
  tokens = word_tokenize(text)
  return tokens


def get_punkt_sent(text:str) -> list[str]:
  """Given an input string, will return the 
  sentence tokenized string using the punkt tokenizer.

  Args:
      text (str): The string to tokenize

  Returns:
      (list[str]): A list of sentence tokens
  """
  __check_punkt_tab()
  tokens = sent_tokenize(text)
  return tokens