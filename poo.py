class Animales:
    def __init__(self,nombre, especie, edad, genero, raza):
        self.nombre=nombre
        self.especie=especie
        self.edad=edad
        self.genero=genero
        self.raza=raza
        
    def correr (self):
        print(self.nombre," esta corriendo")
    def jugar (self):
        print(self.nombre," esta jugando ajedrez")
    def dormir (self):
        print(self.nombre," esta sonando ser unicornio")
    def comer (self):
        print(self.nombre," esta con tremendo postre")

a1 = Animales("jose ","perro ","15 ","hembra ","pug ")
print(a1.nombre,a1.especie,a1.edad)
a1.jugar()
a1.correr()
a2 = Animales("Maria","ave","4","loro","melopsittacus undulatus")
print(a2.genero,a2.raza,a2.nombre)
a2.dormir()
a2.comer
a3 = Animales("Martin ", "felino","14","macho","caracal")
print(a3.especie,a3.nombre,a3.edad)
a3.comer()
a3.dormir()
a4 = Animales("Luis","perro","16","macho","Rottwailer")
print(a4.genero,a4.raza,a4.edad)
a4.correr()
a4.jugar()
a5 = Animales("marcu","felino","12","macho","persa")
print(a5.raza,a5.genero,a5.nombre)
a5.comer()
a5.jugar()
a6 = Animales("Raul","aracnido","2","hembra","viuda negra")
print(a6.especie,a6.raza,a6.genero)
a6.jugar()
a6.dormir()
a7 = Animales("vale","felino","18","hembra","birmano")
print(a7.especie,a7.raza,a7.nombre)
a7.dormir()
a7.comer()