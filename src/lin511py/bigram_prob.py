from nltk.util import bigrams as big
from collections import Counter


def get_conditional_prob(
    tokens:list[str], 
    w1:str, 
    w2:str
  ) -> float:
  """Get the conditional probability of w2|w1

  Args:
      tokens (list[str]): A list of tokens
      w1 (str): word1
      w2 (str): word2

  Returns:
      (float): The conditional probability
  """
  bigrams = big(tokens)
  counts = Counter(bigrams)
  target = counts[(w1, w2)]
  denom = Counter({
    k:v 
    for k,v in counts.items()
    if k[0] == w1
  }).total()

  return target/denom

