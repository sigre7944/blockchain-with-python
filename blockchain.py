blockchain =[

def get_last_value():
  if len(blockchain) < 1:
    return None
  return blockchain[-1]

def add_value(adding_value):
    blockchain.append([get_last_value(), adding_value])
    print(blockchain)

def get_value():
  """ Return the input of user"""
  num = float(input("enter a number"))
  return num

def get_choice():
  input = input('Your choice: ')
  return input

def print_elemetns():
  for block in blockchain:
    print('Blocks:')
    print(block)

def switch_user_choice():
  

tx_amount = get_value()
add_value(tx_amount)

while True:
  print('Please choose')
  print('1: Add new transaction value')
  print('2: Output the blockchain blocks')
  print('q: Quit')
  user_choice = get_choice()
  switch_user_choice(user_choice)

