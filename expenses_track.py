# import csv
# data = [
#   {'Category':'Clothes', 'Description':'New year clothes', 'Expense' : 'Rp. 100.000'},
#   {'Category':'Clothes', 'Description':'New year clothes', 'Expense' : 'Rp. 100.000'},
#   {'Category':'Yifu', 'Description':'New year clothes', 'Expense' : 'Rp. 100.000'}
# ]

# fieldnames = ['Category', 'Description', 'Expense']

# with open('track.csv', 'w', newline='') as file:
#   write= csv.DictWriter(file, fieldnames=fieldnames)

#   write.writeheader()
#   write.writerows(data)

# # print(id(data[1]))
# # print(id(data[2]))
# # print(id(data[0]))

import csv
import os

data = []
fieldscol = ['category', 'description', 'price']  

def get_input():

    data_store = []
    data_input = {'category':'', 'description':'', 'price':''}

    try:
      category_input = input('Input Category [Housing, Transportation, Foods, Health, Custom ]: ').capitalize()
      if category_input == 'Custom':
        category_input = input('Input Custom Category: ').capitalize()
      # elif category_input not in ['Housing', 'Transportation', 'Foods', 'Health', 'Custom']:
      #   print('Please Input by category')
      #   print('Input "Custom" to input another category')
      # else:
      description_input = input('Input Description: ')
      price_input = float(input('Input Price: $ '))

      data_input['category'] = category_input
      data_input['description'] = description_input
      data_input['price'] = price_input

      data_store.append(data_input)
      data.extend(data_store)


      if not os.path.exists('expenses.csv') or os.path.getsize('expenses.csv') == 0:
           with open('expenses.csv', 'a', newline='') as file:
             write = csv.DictWriter(file, fieldnames=fieldscol)
             write.writeheader()
             write.writerows(data)
      else:
        with open('expenses.csv', 'a', newline='') as file:
             write = csv.DictWriter(file, fieldnames=fieldscol)
             write.writerows(data_store)
             
      print('~'*10+' '+'Data Already saved' + ' '+ '~'*10)

    except ValueError:
      print('~'*5 + ' ' +'Error:'+ ' '+'Price must be a number' + ' '+ '~'*5)

    

      

def del_row():
  todel = input('Input description to delete: ')

  with open('expenses.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    new_list=[] # list comprehension: new_list = [r for r in rows if r.get('description') != todel]

    for r in rows:
      if r.get('description') != todel:
          new_list.append(r)
    with open('expenses.csv', 'w', newline='') as file:
      write = csv.DictWriter(file, fieldnames=fieldscol)
      write.writeheader()
      write.writerows(new_list)
    print('~'*10+' '+'Deleted'+' '+ '~'*10)

def tot_expense():
  with open('expenses.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    total = []

    for tot in rows:
      if 'price' in tot:
        total.append(tot['price'])
    print(f'Price list: {total}')
    summ= sum(map(float, total))
    print(f'Total Expense: $ {summ}')
      


def by_category():
   viewinput = input('Category to search: ').capitalize()
   with open('expenses.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    rows = list(reader)
    catfound = False

    for view in rows:
      if view.get('category') == viewinput:
        catfound = True
        print(f'{view['category']} : {view['description']}')
    if not catfound: #not catfoudn mean : "Did we make it through the entire list without finding a match?"
      print('No category found')




def main():
  try:
    with open('expenses.csv', 'r', newline='') as file:
      reader = csv.reader(file)
      rows = list(reader)
  except FileNotFoundError:
    with open('expenses.csv', 'w', newline='') as file:
      write = csv.DictWriter(file, fieldnames=fieldscol)
      write.writeheader()
  while True:
    print('~'*10+' '+'Expenses Tracker' + ' '+ '~'*10)
    user_input = input('Choose One [Add, Delete, Total, Filter, Exit]: ').lower()

    if user_input == 'add':
      get_input()
    elif user_input == 'delete':
      del_row()
    elif user_input == 'total':
      tot_expense()
    elif user_input == 'filter':
      by_category()
    elif user_input == 'exit':
      return
    else:
      print('Invalid Input')

main()
    

  ## Read CSV
    # sample = f.read(2048)
        # f.seek(0)
  
        # has_header = csv.Sniffer().has_header(sample)
  
        # if has_header:
        #    with open('expenses.csv', 'a', newline='') as file:
        #     write = csv.DictWriter(file, fieldnames=fieldscol)
        #     write.writerows(data_store)
        # else:
        #   with open('expenses.csv', 'a', newline='') as file:
        #     write = csv.DictWriter(file, fieldnames=fieldscol)
        #     write.writeheader()
        #     write.writerows(data)

  ## Sort by Category
    # for view in rows:
    #   if view.get('category') == viewinput:
    #     category_value.append(view['category'])
    #     description_value.append(view['description'])
    #     for i in range(len(category_value)):
    #       views = f'{category_value[i]}:{description_value[i]}'
    #     if views:
    #       print(views)
    #       continue
    #     elif not views:
    #       print('No category found')
    