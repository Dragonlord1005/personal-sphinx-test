class hello:
    """Repeats the phrase "Hi there" the number of times specified using the amount variable

    Does this using range loops
    
    Args:
        Amount (int): How many times to repeat "Hi there"

    """
    def __init__(self, amount):
      """Simply decides what to do
      
      """
      self.amount = amount

    def hi(self):
      for _ in range(self.amount):
        print("Hi there")

test = hello(6)
print(test.hi())
