# !pip3 install ColabTurtle
# !pip install ColabTurtlePlus

#import ColabTurtle.Turtle as lia
import ColabTurtlePlus.Turtle as lia

class Tartaruga:
    def __init__(self, w=500, h=550, bg="white"):
        lia.initializeTurtle(window=(w, h)) #, initial_speed=5
        lia.bgcolor(bg)
        lia.shape('turtle2')
        self.canvas_size=(w, h)
        self.turtle=lia
        #self.cancella(bg)  
    def sinistra(self, q):
        self.turtle.left(q)
    def destra(self, q):
        self.turtle.right(q)
    def avanti(self, q):
        self.turtle.forward(q)
    def indietro(self, q):
        self.turtle.backward(q)
    def solleva(self):
        self.turtle.penup()
    def posa(self):
        self.turtle.pendown()
    def sposta(self, x, y):
        self.turtle.goto(x, y)    
    def colore(self, c):
        self.turtle.pencolor(c)
    def cancella(self, bg="white"):
        self.turtle.reset()
        self.turtle.bgcolor(bg)        
    def casa(self):        
        self.turtle.home()        
    def sollevaCasaPosa(self):        
        self.solleva()
        self.turtle.home() 
        self.posa()
    def sollevaSpostaPosa(self, x, y):        
        self.solleva()
        self.sposta(x, y)
        self.posa()
    def cerchio(self, raggio, angolo=360):
        self.turtle.circle(raggio, angolo)
    def iniziaRiempi(self, colore):
        self.turtle.begin_fill()
        self.turtle.fillcolor(colore)
    def terminaRiempi(self):
        self.turtle.end_fill()
    def spessore(self, s):
        self.turtle.pensize(s)
    def velocita(self, valore):
        self.turtle.speed(valore)
    def posizione(self):
        return self.turtle.pos()
    def xy(self):        
        self.indietro(self.canvas_size[0]//2)
        self.sollevaCasaPosa()
        self.avanti(self.canvas_size[0]//2)        
        self.iniziaRiempi("black")
        self.sinistra(150)
        self.avanti(10)
        self.sinistra(120)
        self.avanti(10)
        self.sinistra(120)
        self.avanti(10)
        self.terminaRiempi()
        self.sollevaCasaPosa()
        self.sinistra(90)
        self.indietro(self.canvas_size[1]//2)        
        self.sollevaCasaPosa()
        self.sinistra(90)
        self.avanti(self.canvas_size[1]//2)
        self.iniziaRiempi("black")
        self.sinistra(150)
        self.avanti(10)
        self.sinistra(120)
        self.avanti(10)
        self.sinistra(120)
        self.avanti(10)
        self.terminaRiempi()
        self.sollevaCasaPosa()        
