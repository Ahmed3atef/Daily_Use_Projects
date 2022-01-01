import database
table = database.connect()

#here we cand take any action on database and make some object from database class 
op = input("firstname or lastname: ")
new = input("new record: ")
id = int(input("id: "))
#first = input("firstname: ")
#last = input("lastname: ")

table.update(op,new,id)
table.show_all()
table.close()
