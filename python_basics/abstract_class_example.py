class Saludo(object):
    def __str__(self):
        return self.sayHi()

class Spanish(Saludo):
    def sayHi(self):
        return "Hola"

class French(Saludo):
    def sayHi(self):
        return "Salut"

#abstractHi= Saludo() # This doesn't work
spanisHi= Spanish()
frenchHi= French()


print(spanisHi, frenchHi)
#print(abstractHi) # This doesn't work
