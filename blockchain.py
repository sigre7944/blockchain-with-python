blockchain =[

def get_last_value():
  if len(blockchain) < 1:
    return None
  return blockchain[-1]

def add_transaction(adding_value, last_transaction=[1]):
    blockchain.append([get_last_value(), adding_value])
    if last_transaction ==None:
      last_transaction = [1]
    print(blockchain)

def get_value():
  """ Return the input of user"""
  num = float(input("enter a number"))
  return num

def get_choice():
  input = input('Your choice: ')
  return input

def print_elements():
  for block in blockchain:
    print('Blocks:')
    print(block)

while True:
  print('Please choose')
  print('1: Add new transaction value')
  print('2: Output the blockchain blocks')
  print('q: Quit')
  user_choice = get_choice()
  if user_choice == '1':
    tx_amount = get_value()
    add_transaction(tx_amount, get_last_value())
  elif user_choice == '2':
    print print_elements()
  elif user_choice == 'q'
    break
  else:
    print('You entered wrong, you silly bastard')

