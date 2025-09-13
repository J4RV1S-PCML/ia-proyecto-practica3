
import tkinter as tk
from tkinter import ttk
from Calculadora import CalculadoraUnidades

class ConversionRow(ttk.Frame):
    def __init__(self, parent, label_izq, func, label_der, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.func = func
        self.configure(style='Custom.TFrame')
        self.valor_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.valor_var.trace_add('write', self.convertir)

        ttk.Label(self, text=label_izq, style='Custom.TLabel').grid(row=0, column=0, padx=(10,5), pady=10, sticky='e')
        entry = ttk.Entry(self, textvariable=self.valor_var, width=18, font=("Segoe UI", 11))
        entry.grid(row=0, column=1, padx=5, pady=10)
        ttk.Label(self, text=label_der, style='Custom.TLabel').grid(row=0, column=2, padx=(20,5), pady=10, sticky='e')
        result = ttk.Entry(self, textvariable=self.result_var, width=18, font=("Segoe UI", 11), state='readonly', foreground='#e67e22')
        result.grid(row=0, column=3, padx=5, pady=10)

    def convertir(self, *args):
        valor = self.valor_var.get()
        if valor.strip() == "":
            self.result_var.set("")
            return
        try:
            res = self.func(valor)
            if res is not None:
                self.result_var.set(f"{res}")
            else:
                self.result_var.set("Error")
        except Exception:
            self.result_var.set("Error")

class CalculadoraMedidasGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora de Medidas")
        self.configure(bg="#8fd0fa")
        self.resizable(False, False)
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure('Custom.TFrame', background="#b3e0ff")
        self.style.configure('Custom.TLabel', background="#b3e0ff", font=("Segoe UI", 12, "bold"), foreground="#1a3c5a")
        self.style.configure('Title.TLabel', background="#8fd0fa", font=("Segoe UI", 16, "bold"), foreground="#1a3c5a")
        self._build_ui()

    def _build_ui(self):
        # Título
        ttk.Label(self, text="CALCULADORA DE MEDIDAS", style='Title.TLabel').pack(pady=(20,10))
        main_frame = ttk.Frame(self, padding=15, style='Custom.TFrame')
        main_frame.pack(padx=20, pady=(0,20), fill='both', expand=True)

        # Filas de conversión
        rows = [
            ("Metros", CalculadoraUnidades.metros_a_centimetros, "Centímetros"),
            ("Centímetros", CalculadoraUnidades.centimetros_a_metros, "Metros"),
            ("Metros", CalculadoraUnidades.metros_a_milimetros, "Milímetros"),
            ("Milímetros", CalculadoraUnidades.milimetros_a_metros, "Metros"),
            ("Metros", CalculadoraUnidades.metros_a_kilometros, "Kilómetros"),
            ("Kilómetros", CalculadoraUnidades.kilometros_a_metros, "Metros"),
            ("Millas", CalculadoraUnidades.millas_a_kilometros, "Kilómetros"),
            ("Kilómetros", CalculadoraUnidades.kilometros_a_millas, "Millas"),
        ]
        for i, (izq, func, der) in enumerate(rows):
            row = ConversionRow(main_frame, izq, func, der)
            row.grid(row=i, column=0, pady=5, sticky='ew')

        # Botón salir
        ttk.Button(self, text="Salir", command=self.destroy, style='TButton').pack(pady=(0,15))

if __name__ == "__main__":
    app = CalculadoraMedidasGUI()
    app.mainloop()
