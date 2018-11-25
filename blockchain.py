blockchain =[]
open_transactions = []
owner = 'Hana '

def get_last_value():
  if len(blockchain) < 1:
    return None
  return blockchain[-1]

def add_transaction(sender =  owner, recipient, amount = 1.0)
    transaction = {
      'sender' : sender,
      'recipient' : recipient,
      'amount' : amount
    }
    open_transactions.append(transaction)

def mine_block():
  pass 

def get_value():
  """ Return the input of user"""
  tx_recipient = input("Enter the recipient's name")
  tx_amount = float(input("Enter a number"))
  return (tx_recipient, tx_amount)

def get_choice():
  choice = input('Your choice: ')
  return choice

def print_elements():
  for block in blockchain:
    print('Blocks:')
    print(block)
  else:
    print("-" * 20)

def verify_chain():
  #block_index = 0
  is_valid = True
  for block_index in range(len(blockchain)-1):
    if block_index == 0:
      continue
    if blockchain[block_index][0] == blockchain[block_index-1]:
      is_valid = True
    else:
      is_valid = False
      break
  return is_valid

waiting_for_input = True

while waiting_for_input:
  print('Please choose')
  print('1: Add new transaction value')
  print('2: Output the blockchain blocks')
  print('q: Quit')
  print('h: Manipulate the blockchain')
  user_choice = get_choice()
  if user_choice == '1':
    tx_data = get_transaction_value()
    recipient, amount = tx_data
    add_transaction(recipient, amount)
  elif user_choice == '2':
    print_elements()
  elif user_choice == 'q':
    waiting_for_input = False
  elif user_choice == 'h':
    if len(blockchain) >= 1:
      blockchain[0] = 2  
  else:
    print('You entered wrong, you silly bastard')
  if not verify_chain():
    print_elements()
    print('Invalid blockchain!!')
    waiting_for_input = False
  
else: 
  print('program ended :(')
