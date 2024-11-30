#!/bin/python3
#COSC1519 Introduction to Programming
#Student name: Chi Thinh Do
#Student number: S3817145
#Practical group: Thursday 8:30am
import re
f = open("A3_s3817145_stock.txt")
fish_stock = {}

for line in f:
  stripped_line = line.rstrip()
  fish_name, origin, quantity, price = stripped_line.split(",")
  fish_stock[fish_name] = origin, quantity, price
  
f.close()

print('Loading Data\nReading file A3_s3817145_stock.txt\nAll data loaded\nWelcome to Fish Shop manager 2077')


while True:
  print('What would you like to do?')
  action_list = ['Show one fish information', 'Show all Stock information', 'Add/Update item', 'Remove Item', 'Compute stock price', 'save data and exit']
  for index in range(len(action_list)):
    print('\t','{} - {}'.format(index+1, action_list[index]))
  action_number = int(input(''))
  if action_number == 1:
    def show_all_items():
      for line in f:
        line = line.rstrip()
        print(line)
    show_all_items()
    
  elif action_number == 2:
    def show_one_item():
      try:
        searched = str(input("What is the name of the Fish?"))
        for line in f:
          if line.startswith(searched):
            print(line)
      except:
        print("String only!")
    show_one_item()
  elif action_number == 3:
    def add_or_update_items():
      try:
        searched = str(input("What is the name of the Fish?"))
        for line in f:
          if line.startswith(searched):
            print('Fish in Stock!')
            print(line)
            try:
              new_origin = str(input("What is the (new) country of origin?"))
              new_quantity = int(input("What is the (new) quantity?"))
              new_price = float(input("What is the (new) price?"))
              fish_stock[searched] = new_origin, new_quantity,  new_price
              print('sucsessfully updated')
            except:
              print('only string for country name, only interger for quantity and ony number for price')
      except:
            try:
              new_fish_name = str(input("What is the name of (new) item?"))
              new_origin = str(input("What is the (new) country of origin?"))
              new_quantity = int(input("What is the (new) quantity?"))
              new_price = float(input("What is the (new) price?"))
              fish_stock[new_fish_name] = new_origin, new_quantity,  new_price
              print('sucsessfully updated')
            except:
              print('only string for item name,only string for country name, only interger for quantity and ony number for price!')
      write_file = open("A3_s3817145_stock.txt", "w")
    
      for fish, item in fish_stock.items():
            fish_info = str(item)
            fish_info = fish_info.replace("'", "")
            fish_info  = fish_info.replace(", ", ",")
            fish_info  = fish_info.replace(")", ",")
            fish_info  = fish_info.replace("(", ",")
            write_file.write('%s,%s\n' % (fish_name, fixed_write_fish_name))
      write_file.close()
    add_or_update_items()
  elif action_number == 4:
    def remove_item():
      try:
        searched = str(input("What is the name of the item would you like to remove?"))
        fish_stock.pop(searched)
      except:
        print("String only!")
      write_file = open("A3_s3817145_stock.txt", "w")
      print('Fish removed')
    
      for fish, item in fish_stock.items():
            fish_info  = str(item)
            fish_info  = fish_info.replace("'", "")
            fish_info  = fish_info.replace(", ", ",")
            fish_info  = fish_info.replace(")", ",")
            fish_info  = fish_info.replace("(", ",")
            write_file.write('%s,%s\n' % (fish, fish_info))
      write_file.close()
    remove_item()
  elif action_number == 5:
    def calculate_total_price():
    
      f = open("A3_s3817145_stock.txt")
      price_total = 0
      
      for line in f:
        stripped_line = line.strip()
        value = stripped_line.split(",")
        stock = int(value[2])
        price = float(value[3])
  
          
        total = (stock * price)
        price_total = price_total + total
      f.close()
      print('\n the total amount for all the stock is $AUD', price_total)
    calculate_total_price()
  elif action_number == 6:
    def exit():
      print('end of prograam')
    exit()
    break
  else:
    print('we do not have this choose\n')







        



        





  








      
 
