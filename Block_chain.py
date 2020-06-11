from datetime import datetime
import hashlib
import uuid


class User(object):
    name = ''
    credit = 0
    key = ''

    '''------------------------------Builder-------------------------'''
    def __init__(self, name, initial_credit):
        self.name = name
        self.credit = initial_credit
        print('Introduzca la palabra clave del usuario '+name+': ', end = '')
        seed = str(input())
        # The uuid has the timestamp already. 
        self.key = seed + str(uuid.uuid1)

    '''------------------------------Methods-------------------------'''
    '''------------------------Setters and getters-------------------'''
    def Get_name(self):
        return self.name

    def Set_name(self, name):
        self.name = name

    def Get_credit(self):
        return self.credit

    def Set_credit(self, total):
        self.credit = total

    def Check_balance(self):
        return "Nombre: " + str(self.name) + "\nBalance: " + str(self.credit)

    def Get_key(self):
        return self.key

    def Create_user(self):
        print('Introduzca un nombre: ')
        self.name = str(input())
        print('Introduzca el saldo inicial: ')
        self.credit = float(input())


class Admin(object):
    users = []

    def Add_user(self, user):
        self.users.append(user)

    def Get_element(self, index):
        return self.users[index]
    
    def Find_user(self, name):
        for index in range(len(self.users)):
            if self.users[index].Get_name() == name:
                return self.users[index]
                break
            elif index+1 == len(self.users):
                print("Elemento no encontrado")

    def Print(self):
        for index in range(len(self.users)):
            print('Key: ' + str(self.users[index].Get_key()))
            print('Nombre:' + str(self.users[index].Get_name()))
            print('Saldo: ' + str(self.users[index].Get_credit()) + '\n')


#Block class, which will be listed on the Blockchain.
class Block(object):
    #Attribute containing the Hash.
    id = ''
    #Transaction total is captured on each Block. 
    total = 0.0

    '''------------------------------Methods-------------------------'''
    '''------------------------Setters and getters-------------------'''
    def Set_id(self, id):
        self.id = id

    def Get_id(self):
        return self.id

    def Set_total(self, total):
        self.total = total

    def Get_total(self):
        return self.total


class Block_Chain(object):
    chain = []

    '''------------------------------Methods-------------------------'''
    '''------------------------Setters and getters-------------------'''
    def Get_chain(self):
        return self.chain

    def Deposit(self, transmitter, receiver, total):
        if((int(transmitter.Get_credit())-int(total)) >= 0):
            receiver.Set_credit(int(receiver.Get_credit())+total)
            transmitter.Set_credit(int(transmitter.Get_credit())-total)
            timestamp = datetime.timestamp(datetime.now())
            name = hashlib.sha256(str(transmitter.Get_key()).encode('utf-8')+
            str(receiver.Get_key()).encode('utf-8')+str(timestamp).encode('utf-8')).hexdigest()
            n = Block()
            n.Set_id(name)
            n.Set_total(total)
            self.chain.append(n)
        else:
            print("No hay credito suficiente para realizar la operación")

    def Add(self):
        print('\nIntroduce el nombre: ', end = '')
        name = str(input())
        print('Introduce el credito inicial: ', end = '')
        credit = str(input())
        u = User(name, credit)
        a = Admin()
        a.Add_user(u)

    def Transfer(self):
        ad = Admin()
        print('\nIntroduce la cantidad: ', end = '')
        credit = int(input())
        print('Introduce el nombre del usuario que depositará: ', end = '')
        a = ad.Find_user(str(input()))
        print('Introduce el nombre del usuario que recibira el deposito: ', end = '')
        b = ad.Find_user(str(input()))
        bc = Block_Chain()
        bc.Deposit(a, b, credit)

    def Print(self):
        a = Admin()
        bc = Block_Chain()
        print("\n----------------------Los usuarios son: --------------------")
        a.Print()
        print("\n------------------------La cadena es: ----------------------")
        for index in range(len(self.chain)):
            print(str(self.chain[index].Get_id())+" ")

def main():
    while True:
        print(
            '\n\n1)Agregar'+'\n'
            '2)Depositar'+'\n'
            '3)Imprimir'+'\n'
            '4)Salir'+'\n'
        )
        bc = Block_Chain()
        print('--->', end = '')
        ans = int(input())
        if ans  == 1:
            bc.Add()
        if ans == 2:
            bc.Transfer()
        if ans == 3:
            bc.Print()
        if ans == 4:
            break
main()