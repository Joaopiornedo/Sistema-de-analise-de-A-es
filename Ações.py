import yfinance 
import tkinter as tk
from tkinter import messagebox

def Sistema():
    # Ação a ser avaliada:
    ticker = entrada_acao.get()
    # Definindo a data inicio e fim:
    data_start = entrada_data_inicio.get()
    data_end = entrada_data_fim.get()

    # Utilizando .ticker para buscar a ação na base de dados e o history para passar as datas que queremos buscar:
    dados = yfinance.Ticker(f"{ticker}").history(start=data_start, end=data_end)
    
    # Construindo a mensagem com os valores calculados
    mensagem = (
        f"Valores Mínimos:\n"
        f"Open: {round(dados.Open.min(), 2)}\n"
        f"High: {round(dados.High.min(), 2)}\n"
        f"Low: {round(dados.Low.min(), 2)}\n"
        f"Close: {round(dados.Close.min(), 2)}\n"
        f"Volume: {round(dados.Volume.min(), 2)}\n\n"

        f"Valores Médios:\n"
        f"Open: {round(dados.Open.mean(), 2)}\n"
        f"High: {round(dados.High.mean(), 2)}\n"
        f"Low: {round(dados.Low.mean(), 2)}\n"
        f"Close: {round(dados.Close.mean(), 2)}\n"
        f"Volume: {round(dados.Volume.mean(), 2)}\n\n"

        f"Valores Máximos:\n"
        f"Open: {round(dados.Open.max(), 2)}\n"
        f"High: {round(dados.High.max(), 2)}\n"
        f"Low: {round(dados.Low.max(), 2)}\n"
        f"Close: {round(dados.Close.max(), 2)}\n"
        f"Volume: {round(dados.Volume.max(), 2)}"
    )

    # Exibindo os resultados em uma caixa de mensagem
    messagebox.showinfo("Resultados", mensagem)

# Configurando a interface gráfica
janela = tk.Tk()
janela.title("Sistema de Fechamento de Ações")
janela.geometry("400x300")

# Criando campos de entrada para o ticker e as datas
label_acao = tk.Label(janela, text="Digite o código da ação (ex: PETR4.SA):")
label_acao.pack(pady=10)
entrada_acao = tk.Entry(janela)
entrada_acao.pack(pady=5)

label_data_inicio = tk.Label(janela, text="Digite a data de início (formato: YYYY-MM-DD):")
label_data_inicio.pack(pady=10)
entrada_data_inicio = tk.Entry(janela)
entrada_data_inicio.pack(pady=5)

label_data_fim = tk.Label(janela, text="Digite a data final (formato: YYYY-MM-DD):")
label_data_fim.pack(pady=10)
entrada_data_fim = tk.Entry(janela)
entrada_data_fim.pack(pady=5)

# Botão para iniciar o sistema
botao = tk.Button(janela, text="Iniciar", command=Sistema)
botao.pack(pady=20)

# Iniciando o loop principal da interface gráfica
janela.mainloop()
