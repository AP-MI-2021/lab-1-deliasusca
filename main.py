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

'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  product=1
  for number in lst:
    product *= number
  return product

'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  while x!=y:
    if x>y:
      x-=y
    else:
      y-=x
  return x
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''

  
def main():
  # interfata de tip consola aici
  print(is_prime(7))
  print(get_product([1,2,3]))
  print(get_cmmdc_v1(10,9))
  print("Am implementat interfata")

if __name__ == '__main__':
  print('hello')
  main()


