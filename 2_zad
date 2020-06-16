documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
  '1': ['2207 876234', '11-2', '5455 028765'],
  '2': ['10006'],
  '3': []
}

def second_name_people():
	print('Введите номер документа человека, имя которого Вы хотите узнать: ')
	number_doc = 'Ничего не найдено'
	number_doc = input()
	for document in documents:
		if document['number'] == number_doc:
			res = document['name']
			print(res)
			break
	else:
		print('sdgsdg', number_doc)



def all_list():
	for document in documents:
		print('Документ:\n{} {} {}'.format(document['type'], document['number'], document['name']))


def number_shelf():
	print('Введите номер документа и Вы узнаете номер полки, на которой он располагается ')
	num_doc = 'Ничего не найдено'
	num_doc = input()
	for key_directories in directories:
		for values_directories in directories[key_directories]:
			if num_doc == values_directories:
				num_doc = print(f'Полка №:', key_directories)
	return num_doc
    
#				break
#		else:
#			print("Возможно, Вы неправильно ввели номер документа")
#			num_doc = input()
#			continue



def add_dok():
	add_doc = input('Type (passport, invoice, insurance):')
	add_number = input('number:')
	add_name = input('name:')
	information = {'type': add_doc, 'number': add_number, 'name': add_name}
	add_key = input('directory:')
	for key_directories in directories:
		if add_key == key_directories:
			print('Все хорошо, такая полка есть')
			break
		else:
			print("Возможно, Вы неправильно ввели номер полки. Попробуйте еще раз")
			add_key = input('directory:')
			continue
	directories[add_key].append(add_number)
	documents.append(information)

def new_doc_list():
  for document in documents:
    print('{} {} {}'.format(document['type'], document ['number'], document ['name']))


#Задача по исключениям - KeyError
def print_all_name(documents):
  for item in documents:
    try:
      print(item['name'])
    except KeyError as e:
      print(e)

def all_func():
  print ("Что Вы хотите сделать? \np - узнать фамилию человека по номеру документа. \nl - увидеть список всех документов. \ns - узнать номер полки, на которой хранится документ. \na - добавить документ. \nk - вывести все имена. \nВведите команду:")
  user_input = input()
  if user_input == 'p':
    second_name_people()
  elif user_input == 'l':
    all_list()
  elif user_input == 's':
    number_shelf()
  elif user_input == 'a':
    add_dok()
    new_doc_list() 
  elif user_input == 'k':
    print_all_name(documents)
  else:
    print ("Возможно, Вы неправильно ввели номер команды")
    
while True:
  all_func()
