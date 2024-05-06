import tkinter as tk

def mostrar_texto():
    texto_digitado = entrada.get()  # Obter o texto digitado pelo usuário
    label_resultado.config(text="Texto digitado: " + texto_digitado)  # Atualizar o rótulo com o texto digitado

janela_principal = tk.Tk()
janela_principal.title("Exemplo de Entry")

# Criar um Entry
entrada = tk.Entry(janela_principal, width=30)
entrada.pack()

# Criar um botão para exibir o texto digitado
botao = tk.Button(janela_principal, text="Mostrar Texto", command=mostrar_texto)
botao.pack()

# Criar um rótulo para exibir o texto digitado
label_resultado = tk.Label(janela_principal, text="")
label_resultado.pack()

janela_principal.mainloop()
