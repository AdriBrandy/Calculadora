import customtkinter as ctk

# Configuración de CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class CalculadoraApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("265x350")
        self.resizable(False, False)
        
        self.entrada_texto = ""

        # Pantalla
        self.pantalla = ctk.CTkEntry(self, font=("Arial", 15), justify="right", width=190, height=50)
        self.pantalla.grid(row=0, column=0, columnspan=4, pady=25, padx=5)
        self.actualizar_pantalla()

        # Vinculamos eventos del teclado
        self.bind("<Key>", self.tecla_presionada)
        self.focus_set()

        # Botones 
        botones = [
            ('7', 1, 1), ('8', 1, 2), ('9', 1, 3), ('/', 1, 4),
            ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('*', 2, 4),
            ('1', 3, 1), ('2', 3, 2), ('3', 3, 3), ('-', 3, 4),
            ('.', 4, 1), ('0', 4, 2), ('+', 4, 3), ('=', 4, 4)
        ]
        for (texto, fila, columna) in botones:
            boton = ctk.CTkButton(self, text=texto, font=("Arial", 20), width=60, height=60, command=lambda t=texto: self.boton_click(t))
            boton.grid(row=fila, column=columna, padx=1, pady=1)

        boton_clear = ctk.CTkButton(self, text="C", font=("Arial", 20), width=60, height=50, fg_color="red", command=self.boton_clear)
        boton_clear.grid(row=0, column=4, columnspan=5, padx=1, pady=1)

    def actualizar_pantalla(self):
        self.pantalla.delete(0, ctk.END)
        self.pantalla.insert(ctk.END, self.entrada_texto)

    def boton_click(self, texto):
        if texto == "=":
            try:
                resultado = eval(self.entrada_texto)
                self.entrada_texto = str(resultado)
            except:
                self.entrada_texto = "Error"
        else:
            self.entrada_texto += str(texto)
        self.actualizar_pantalla()

    def boton_clear(self):
        self.entrada_texto = ""
        self.actualizar_pantalla()

    def tecla_presionada(self, evento):
        tecla = evento.char
        if tecla in "0123456789.+-*/":
            self.entrada_texto += tecla
        elif evento.keysym == "Return":
            try:
                resultado = eval(self.entrada_texto)
                self.entrada_texto = str(resultado)
            except:
                self.entrada_texto = "Error"
        elif evento.keysym == "BackSpace":
            self.entrada_texto = self.entrada_texto[:-1]
        self.actualizar_pantalla()

if __name__ == "__main__":
    app = CalculadoraApp()
    app.mainloop()


# basic calculator