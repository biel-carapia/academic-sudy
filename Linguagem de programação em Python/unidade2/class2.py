class Animal:
  def __init__(self, nome):
    self.nome = nome
  def fazer_barulho(self):
    pass
class Cachorro(Animal):
  def fazer_barulho(self):
    return "Latir"
class Gato(Animal):
  def fazer_barulho(self):
    return "Miar"

rex = Cachorro("Rex")
whisker = Gato("whiskers")

print(f"{rex.nome} faz: {rex.fazer_barulho()}")

print(f"{whisker.nome} faz: {whisker.fazer_barulho()}")
