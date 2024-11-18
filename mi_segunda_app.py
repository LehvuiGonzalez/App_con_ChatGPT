import tkinter as tk
from tkinter import ttk

# Funciones para las conversiones
def convertir():
    categoria = categoria_combobox.get()
    conversion = conversion_combobox.get()
    valor = float(entry_valor.get())
    resultado = None

    # Conversiones
    if categoria == "Temperatura":
        if conversion == "Celsius a Fahrenheit":
            resultado = valor * 9/5 + 32
        elif conversion == "Fahrenheit a Celsius":
            resultado = (valor - 32) * 5/9
        elif conversion == "Celsius a Kelvin":
            resultado = valor + 273.15
        elif conversion == "Kelvin a Celsius":
            resultado = valor - 273.15
    elif categoria == "Longitud":
        if conversion == "Pies a metros":
            resultado = valor * 0.3048
        elif conversion == "Metros a pies":
            resultado = valor / 0.3048
        elif conversion == "Pulgadas a centímetros":
            resultado = valor * 2.54
        elif conversion == "Centímetros a pulgadas":
            resultado = valor / 2.54
    elif categoria == "Peso/Masa":
        if conversion == "Libras a kilogramos":
            resultado = valor * 0.453592
        elif conversion == "Kilogramos a libras":
            resultado = valor / 0.453592
        elif conversion == "Onzas a gramos":
            resultado = valor * 28.3495
        elif conversion == "Gramos a onzas":
            resultado = valor / 28.3495
    elif categoria == "Volumen":
        if conversion == "Galones a litros":
            resultado = valor * 3.78541
        elif conversion == "Litros a galones":
            resultado = valor / 3.78541
        elif conversion == "Pulgadas cúbicas a centímetros cúbicos":
            resultado = valor * 16.3871
        elif conversion == "Centímetros cúbicos a pulgadas cúbicas":
            resultado = valor / 16.3871
    elif categoria == "Tiempo":
        if conversion == "Horas a minutos":
            resultado = valor * 60
        elif conversion == "Minutos a segundos":
            resultado = valor * 60
        elif conversion == "Días a horas":
            resultado = valor * 24
        elif conversion == "Semanas a días":
            resultado = valor * 7
    elif categoria == "Velocidad":
        if conversion == "Millas por hora a kilómetros por hora":
            resultado = valor * 1.60934
        elif conversion == "Kilómetros por hora a metros por segundo":
            resultado = valor / 3.6
        elif conversion == "Nudos a millas por hora":
            resultado = valor * 1.15078
        elif conversion == "Metros por segundo a pies por segundo":
            resultado = valor * 3.28084
    elif categoria == "Área":
        if conversion == "Metros cuadrados a pies cuadrados":
            resultado = valor * 10.7639
        elif conversion == "Pies cuadrados a metros cuadrados":
            resultado = valor / 10.7639
        elif conversion == "Kilómetros cuadrados a millas cuadradas":
            resultado = valor * 0.386102
        elif conversion == "Millas cuadradas a kilómetros cuadrados":
            resultado = valor / 0.386102
    elif categoria == "Energía":
        if conversion == "Julios a calorías":
            resultado = valor / 4.184
        elif conversion == "Calorías a kilojulios":
            resultado = valor * 0.004184
        elif conversion == "Kilovatios-hora a megajulios":
            resultado = valor * 3.6
        elif conversion == "Megajulios a kilovatios-hora":
            resultado = valor / 3.6
    elif categoria == "Presión":
        if conversion == "Pascales a atmósferas":
            resultado = valor / 101325
        elif conversion == "Atmósferas a pascales":
            resultado = valor * 101325
        elif conversion == "Barras a libras por pulgada cuadrada":
            resultado = valor * 14.5038
        elif conversion == "Libras por pulgada cuadrada a bares":
            resultado = valor / 14.5038
    elif categoria == "Tamaño de datos":
        if conversion == "Megabytes a gigabytes":
            resultado = valor / 1024
        elif conversion == "Gigabytes a Terabytes":
            resultado = valor / 1024
        elif conversion == "Kilobytes a megabytes":
            resultado = valor / 1024
        elif conversion == "Terabytes a petabytes":
            resultado = valor / 1024

    # Mostrar resultado
    if resultado is not None:
        label_resultado.config(text=f"Resultado: {resultado:.2f}")
    else:
        label_resultado.config(text="Conversión no válida.")

# Interfaz gráfica
app = tk.Tk()
app.title("Conversor Universal")

# Categoría
tk.Label(app, text="Categoría:").grid(row=0, column=0, padx=5, pady=5)
categoria_combobox = ttk.Combobox(app, values=[
    "Temperatura", "Longitud", "Peso/Masa", "Volumen",
    "Tiempo", "Velocidad", "Área", "Energía",
    "Presión", "Tamaño de datos"
])
categoria_combobox.grid(row=0, column=1, padx=5, pady=5)

# Conversión
tk.Label(app, text="Conversión:").grid(row=1, column=0, padx=5, pady=5)
conversion_combobox = ttk.Combobox(app)
conversion_combobox.grid(row=1, column=1, padx=5, pady=5)

def actualizar_opciones(event):
    categoria = categoria_combobox.get()
    opciones = {
        "Temperatura": ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"],
        "Longitud": ["Pies a metros", "Metros a pies", "Pulgadas a centímetros", "Centímetros a pulgadas"],
        "Peso/Masa": ["Libras a kilogramos", "Kilogramos a libras", "Onzas a gramos", "Gramos a onzas"],
        "Volumen": ["Galones a litros", "Litros a galones", "Pulgadas cúbicas a centímetros cúbicos", "Centímetros cúbicos a pulgadas cúbicas"],
        "Tiempo": ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"],
        "Velocidad": ["Millas por hora a kilómetros por hora", "Kilómetros por hora a metros por segundo", "Nudos a millas por hora", "Metros por segundo a pies por segundo"],
        "Área": ["Metros cuadrados a pies cuadrados", "Pies cuadrados a metros cuadrados", "Kilómetros cuadrados a millas cuadradas", "Millas cuadradas a kilómetros cuadrados"],
        "Energía": ["Julios a calorías", "Calorías a kilojulios", "Kilovatios-hora a megajulios", "Megajulios a kilovatios-hora"],
        "Presión": ["Pascales a atmósferas", "Atmósferas a pascales", "Barras a libras por pulgada cuadrada", "Libras por pulgada cuadrada a bares"],
        "Tamaño de datos": ["Megabytes a gigabytes", "Gigabytes a Terabytes", "Kilobytes a megabytes", "Terabytes a petabytes"]
    }
    conversion_combobox.config(values=opciones.get(categoria, []))
    conversion_combobox.set("")

categoria_combobox.bind("<<ComboboxSelected>>", actualizar_opciones)

# Valor a convertir
tk.Label(app, text="Valor:").grid(row=2, column=0, padx=5, pady=5)
entry_valor = tk.Entry(app)
entry_valor.grid(row=2, column=1, padx=5, pady=5)

# Botón convertir
boton_convertir = tk.Button(app, text="Convertir", command=convertir)
boton_convertir.grid(row=3, column=0, columnspan=2, pady=10)

# Resultado
label_resultado = tk.Label(app, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

# Ejecutar aplicación
app.mainloop()
