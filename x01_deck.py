#!python3

"""
Create a list of cards
the cards should be denoted with a number or A, J, Q, K, T (for ace, jack, queen, king or ten)
as well as a suit
"""

def createDeck():
  ranks = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
  suits = ['C','D','H','S']
  a = []
  for c in ranks:
    for l in suits:
      deck = [c + l]
      a = a + deck
  return a
createDeck()





def main():
  deck = createDeck()
  assert "JH" in deck 
  print(deck)
  assert "AC" in deck 
  assert "TD" in deck 
  assert len(deck) == 52
  
if __name__ == "__main__":
  main()
