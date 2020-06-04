import hashlib
import random


class Persona(object):
    name = ''
    credit = 0
    chain = []

    '''-------------------------Builder--------------------'''
    def __init__(self, name, initial_credit):
        self.name = name
        self.credit = initial_credit

    '''-------------------------Methods--------------------'''
    def Get_name(self):
        return self.name

    def Set_name(self, name):
        self.name = name

    def Get_credit(self):
        return self.credit

    def Set_credit(self, total):
        self.credit = total

    def Set_chain(self, trans):
        self.chain.append(trans)

    def Get_chain(self):
        return self.chain


class Block(object):
    id = ''
    total = ''

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

    '''-----------------------------Methods---------------------------'''
    def Get_chain(self):
        return self.chain

    def Deposit(self, transmitter, receiver, total):
        if((transmitter.Get_credit()-total) >= 0):
            receiver.Set_credit(receiver.Get_credit()+total)
            transmitter.Set_credit(transmitter.Get_credit()-total)
            name = hashlib.sha256(transmitter.Get_name().encode('utf-8')+
            receiver.Get_name().encode('utf-8')+str(random.randint(0,total)).encode('utf-8')).hexdigest()
            n = Block()
            n.Set_id(name)
            n.Set_total(total)
            transmitter.Set_chain(n)
            receiver.Set_chain(n)
            self.chain.append(n)
        else:
            print("No hay credito suficiente para realizar la operación")


def main():
    a = Persona("a", 0)
    b = Persona("b", 0)
    c = Persona("c", 1000)
    bc = Block_Chain()
    bc.Deposit(c, a, 500)
    print("\n\n------------------------La cadena es: ----------------------")
    print(bc.Get_chain())
    print("\n\n")
main()
