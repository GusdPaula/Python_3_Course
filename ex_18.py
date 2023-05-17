"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractmethod
import random

#Criar classe Cliente que herda da classe Pessoa (Herança)
#    Pessoa tem nome e idade (com getters)

class Person(ABC):
    def __init__(self, name, age) -> None:
        super().__init__()
        self.name_ = name
        self.age_ = age

    @property
    def get_name(self):
        return self.name_


    @get_name.setter
    def get_name(self, name):
        self.name_ = name


    @property
    def get_age(self):
        return self.age_
    

    @get_age.setter
    def get_age(self, age):
        self.age_ = age

    
#    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
#Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
#    ContaCorrente deve ter um limite extra
#    Contas têm agência, número da conta e saldo
#    Contas devem ter método para depósito
#    Conta (super classe) deve ter o método sacar abstrato (Abstração e
#    polimorfismo - as subclasses que implementam o método sacar)


class Account(ABC):
    def __init__(self, agency: int, account_number: int, balance: float = 0) -> None:
        super().__init__()

        self.agency_ = agency
        self.account_number_ = account_number
        self.balance_ = balance
        self.customer_ = None
    
    @abstractmethod
    def deposit(self, amount: float) -> None:
        self.balance_ += amount
    

    #    * Checar se a agência é daquele banco
    #    * Checar se o cliente é daquele banco
    #    * Checar se a conta é daquele banco
    #Só será possível sacar se passar na autenticação do banco (descrita acima)
    #Banco autentica por um método.
    @abstractmethod
    def withdraw(self, amount: float, bank) -> bool:
        if self.agency_ in bank.agencies_:
            if self.customer_ in bank.customers_:
                if (self.account_number_ == bank.accounts_[self.customer_][0].__dict__['account_number_']) or \
                    (self.account_number_ == bank.accounts_[self.customer_][1].__dict__['account_number_']):
                    return True
                
                else:
                    raise TypeError('Account not found...')
            
            else:
                raise TypeError('Customer not found...')
        
        else:
            raise TypeError('Agency not found')



class CheckingAccount(Account):
    def __init__(self, agency, account_number, balance, extra_limit) -> None:
        super().__init__(agency, account_number, balance)
        self.extra_limit_ = extra_limit


    def withdraw(self, amount, bank):
        super().withdraw(amount, bank)
        if amount > self.balance_ + self.extra_limit_:
            raise ValueError('There are no limit to this amount...')
        
        self.balance_ -= amount

        if self.balance_ < 0:
            self.extra_limit_ += self.balance_

    
    def deposit(self, amount):
        return super().deposit(amount)


class SavingsAccount(Account):
    def withdraw(self, amount, bank):
        super().withdraw(amount, bank)

        if amount > self.balance_:
            raise ValueError('There are no limit to this amount...')
        
        self.balance_ -= amount
    

    def deposit(self, amount):
        return super().deposit(amount)


class Customer(Person):
    def __init__(self, name, age, account_type) -> None:
        super().__init__(name, age)

        self.account_type_ = account_type
        self.savings_account_ = None
        self.checking_account_ = None

        if self.account_type_ == 'Savings':
            self.savings_account_ = SavingsAccount(1010, random.randint(1,1000), 100000)
            self.savings_account_.customer_ = name

        elif self.account_type_ == 'Checking':
            self.checking_account_ = CheckingAccount(1010, random.randint(1,1000), 10000, 1000)
            self.checking_account_.customer_ = name

        elif self.account_type_ == 'Both':
            self.savings_account_ = SavingsAccount(1010, random.randint(1,1000), 100000)
            self.savings_account_.customer_ = name
            self.checking_account_ = CheckingAccount(1010, random.randint(1,1000), 10000, 1000)
            self.checking_account_.customer_ = name
            
        else:
            raise TypeError(f'There are no account type as this: {account_type}')


#Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
#Banco será responsável autenticar o cliente e as contas da seguinte maneira:
#    Banco tem contas e clentes (Agregação)

class Bank():
    def __init__(self) -> None:
        self.agencies_ = dict()
        self.accounts_ = dict()
        self.customers_ = dict()
    
    
    def new_customers(self, name, age, account_type):
        customer_id = name
        self.customers_[customer_id] = Customer(name, age, account_type)
        self.accounts_[customer_id] = (self.customers_[customer_id].checking_account_, self.customers_[customer_id].savings_account_)

        self.agencies_[1010] = 'Main'