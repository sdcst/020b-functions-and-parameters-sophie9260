#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger(number):
  try:
    number = float(number)
    newNumber = number/2
    newNumber = round(newNumber)
    NN = newNumber*2
    if NN == number:
      return True
    else:
      return False
  except:
    return False

if __name__ == "__main__":
  assert isInteger( 9.5 ) == False
  assert isInteger( -2 ) == True    
  assert isInteger("hello") == False
  assert isInteger(0) == True
