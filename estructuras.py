import tkinter as tk
from math import factorial

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Estructuras Dinámicas Calculadora")

        # Crear un marco para el menú de operaciones
        self.operation_frame = tk.Frame(root, padx=50, pady=50, borderwidth=2, relief="solid", bg="lightgray")
        self.operation_frame.pack()

        # Crear etiquetas
        self.label1 = tk.Label(self.operation_frame, text="Seleccione una operación:", font=("Arial", 12))
        self.label1.pack()

        # Crear botones de radio
        self.var = tk.StringVar()
        
        self.radio_var = tk.Radiobutton(self.operation_frame, text="Variación", variable=self.var, value="Variación", font=("Arial", 10))
        self.radio_comb = tk.Radiobutton(self.operation_frame, text="Combinación", variable=self.var, value="Combinación", font=("Arial", 10))
        self.radio_perm_circular = tk.Radiobutton(self.operation_frame, text="Permutación Circular", variable=self.var, value="Permutación Circular", font=("Arial", 10))
        self.radio_perm_sin_rep = tk.Radiobutton(self.operation_frame, text="Permutación sin Repetición", variable=self.var, value="Permutación sin Repetición", font=("Arial", 10))
        

        self.radio_var.pack()
        self.radio_comb.pack()
        self.radio_perm_circular.pack()
        self.radio_perm_sin_rep.pack()
        

        # Crear campos de entrada con color
        self.label2 = tk.Label(root, text="Ingrese el valor de n:", font=("Arial", 12))
        self.entry_n = tk.Entry(root, font=("Arial", 10), bg="lightyellow")
        self.label3 = tk.Label(root, text="Ingrese el valor de r:", font=("Arial", 12))
        self.entry_r = tk.Entry(root, font=("Arial", 10), bg="lightyellow")
        

        self.label2.pack()
        self.entry_n.pack()
        self.label3.pack()
        self.entry_r.pack()
        

        # Crear botón de cálculo con bordes
        self.calculate_button = tk.Button(root, text="Calcular", command=self.calculate, font=("Arial", 12), bg="lightblue", relief="solid", borderwidth=2)
        self.calculate_button.pack()

        # Crear etiqueta de resultado
        self.result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
        self.result_label.pack()

    def calculate(self):
        n = int(self.entry_n.get())
        r = int(self.entry_r.get())
        operation = self.var.get()

        if n < 0 or r < 0:
            self.result_label.config(text="Los valores deben ser no negativos.", fg="red")
            return

        if operation == "Variación":
            result = factorial(n) // factorial(n - r)
        elif operation == "Combinación":
            result = factorial(n) // (factorial(r) * factorial(n - r))
        elif operation == "Permutación Circular":
            result = factorial(n - 1)
        elif operation == "Permutación sin Repetición":
            result = factorial(n)

        self.result_label.config(text=f"Resultado: {result}", fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
