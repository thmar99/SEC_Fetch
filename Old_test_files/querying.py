#MySQL handler

'''this modeule is brokedn down to the CRUD basics of SQL, and handles queries based on such models'''

from py_sql_connect import get_base

#Collect database info from user, establish connection & command cursor
pw = input('Enter server password: ')
db = input('Select database to use: ')
mydb = get_base(pw,db)
cursor = mydb.cursor(buffered=True)

cursor.execute('show tables')
'''Display known tables in database'''
print('known tables in: '+db)
for db in cursor:
    print(db)

def read()->None:
    '''handles the following queries: SELECT '''
    e_data = input('Enter query: ')
    cursor.execute(e_data)
    result = cursor.fetchall() 
    for i in result:
        print(i)
    return None

def create()->None:
    '''handles the following queries: CREATE TABLE, DROP TABLE, INSERT INTO TABLE'''
    c_data = input('Enter query: ')
    cursor.execute(c_data)
    mydb.commit()
    return None

exit = False
while exit != True:
    '''BREAK DOWN CRUD SELECTION'''
    inp = input('do you want to continue? (y/n): ')
    if inp == 'n':
        print('exiting...')
        exit = True
    elif inp =='y':
        cmd = input('\nAre you:\n reading data(r) \n creating data(c): \n')
        if cmd =='r':
            read()
        elif cmd =='c':
            create()
        else:
            pass
    else:
        pass