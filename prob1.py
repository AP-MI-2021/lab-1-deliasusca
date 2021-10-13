'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  if n<2:
    return False
  for divisor in range (2,n//2):
    if n%divisor==0:
      return False
  return True

def test_is_prime():
    assert is_prime(0)==False
    assert is_prime(3)== True
    print(is_prime(3))

test_is_prime()