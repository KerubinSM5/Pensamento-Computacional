import tkinter as tk

def botao_clicado():
    print(f"Botão clicado! Digito: {entrada.get()}") #função de resposta do botão

janela = tk.Tk()
janela.title('Primeira Janela')

rotulo = tk.Label(janela, text='Olá mundo')
rotulo.pack()

botao = tk.Button(janela, text="Clique aqui", command=botao_clicado) #chama a função botão
botao.pack()

entrada = tk.Entry(janela) #caixa de texto para entrada de dados
entrada.pack()

janela.mainloop() #inicia, aparecendo a janela