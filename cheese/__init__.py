class hello:
    """Repeats the phrase "Hi there" the number of times specified using the amount variable

    Does this using loops
    
    Args:
        Amount (int): How many times to repeat hi

    Returns:
        string: Hi there

    """
    def __init__(self, amount):
      self.amount = amount

    def hi(self, amount):
      x = "Hi there"
      for x in range(amount):
        print(X)