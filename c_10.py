# Class names should be in PascalCase
# A Class can have attributes that will work with data inside the Class
# And a Class can have methods that will do actions for the Class
# All the methods in a class MUST HAVE as the first parameter the "self"
# Self is the variable
# The class has her own scope

class PessoaCadastrada:
    '''
        This will work for study porpose.
    
    '''
    def __init__(self, nome, sobrenome):
        # These are attributes
        self.nome = nome
        self.sobrenome = sobrenome


    def __str__(self):
        return self.nome + ' ' + self.sobrenome


    # This is a method
    def enviar_msg(self):
        print("Enviamos a mendagem, ", self.nome)

#--------------------------------------------------------------#
#                        Testing the class                     #
#--------------------------------------------------------------#
p1 = PessoaCadastrada("Gustavo", "de paula")

print(p1)
print(p1.nome)


p1.nome = 'Luiz' # Attribute
p1.sobrenome = 'Miranda' # Attribute
print(p1)
print(p1.nome)
print(p1.sobrenome)

p1.enviar_msg()
