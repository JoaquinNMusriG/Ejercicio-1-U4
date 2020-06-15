from tkinter import *
from tkinter import ttk, font

class Aplicacion():
    __ventana=None
    __altura=None
    __peso=None
    __mensaje=None
    __mensajeRta=None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title("Calculadora de IMC")
        self.__ventana.resizable(0,0)

        self.marco = ttk.Frame(self.__ventana,relief="flat", padding=(10,10))
        self.tituloLbl = ttk.Label(self.marco, text="Calculadora de IMC",font=font.Font(weight='bold'), padding=(5,5))
        self.alturaLbl = ttk.Label(self.marco, text="Altura:", padding=(5,5))
        self.pesoLbl = ttk.Label(self.marco, text="Peso:", padding=(5,5))
        self.cmLbl = ttk.Label(self.marco, text="cm", padding=(5,5))
        self.kgLbl = ttk.Label(self.marco, text="kg", padding=(5,5))

        self.__mensaje = StringVar()
        self.__mensajeRta = StringVar()
        self.etiq1 = ttk.Label(self.marco, textvariable=self.__mensaje,font=font.Font(weight='bold'))
        self.etiq2 = ttk.Label(self.marco, textvariable=self.__mensajeRta,font=font.Font(weight='bold'))

        self.__altura = StringVar()
        self.__peso = StringVar()
        self.ctext1 = ttk.Entry(self.marco, textvariable=self.__altura,width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable=self.__peso, width=30)
        self.separ1 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.separ2 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.separ3 = ttk.Separator(self.marco, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marco, text="Calcular", padding=(5,5), command=self.calcular)
        self.boton2 = ttk.Button(self.marco, text="Limpiar", padding=(5,5), command=self.limpiar)

        self.marco.grid(column=0, row=0)
        self.tituloLbl.grid(column=0, row=0, columnspan=4)
        self.separ1.grid(column=0, row=1, columnspan=4,sticky="ew")

        self.alturaLbl.grid(column=0, row=2)
        self.ctext1.grid(column=1, row=2, columnspan=2)
        self.separ2.grid(column=0, row=3, columnspan=4,sticky="ew")
        self.cmLbl.grid(column=3, row=2)

        self.pesoLbl.grid(column=0, row=4)
        self.ctext2.grid(column=1, row=4, columnspan=2)
        self.separ3.grid(column=0, row=5, columnspan=4,sticky="ew")
        self.kgLbl.grid(column=3, row=4)

        self.boton1.grid(column=1, row=6)
        self.boton2.grid(column=2, row=6)

        self.etiq1.grid(column=1, row=7, columnspan=2)
        self.etiq2.grid(column=1, row=8, columnspan=2)

        self.__ventana.mainloop()

    def calcular(self):
        try:
            altura = float(self.ctext1.get())
            peso = float(self.ctext2.get())
            if (altura > 0) & (peso > 0):
                mtr = (altura / 100) * (altura / 100)
                imc = peso / mtr
                self.etiq1.configure(foreground='green')
                self.__mensaje.set('Tu Indice de Masa Corporal(IMC) es {:0.2f}'.format(imc))
                self.etiq2.configure(foreground='green')
                if imc < 18.5:
                    self.__mensajeRta.set('Peso inferior al normal')
                elif imc < 24.9:
                    self.__mensajeRta.set('Normal')
                elif imc < 29.9:
                    self.__mensajeRta.set('Peso superior al normal')
                else:
                    self.__mensajeRta.set('Obesidad')
            else:
                self.etiq1.configure(foreground='red')
                self.__mensaje.set('Valor inválido.')
        except ValueError:
            self.etiq1.configure(foreground='red')
            self.__mensaje.set('Debe ser un numero.')

    def limpiar(self):
        self.__altura.set('')
        self.__peso.set('')
        self.__mensaje.set('')
        self.__mensajeRta.set('')
