import tkinter as tk


def calcular():
    nivel_atual = int(nivel_atual_entry.get())
    nivel_desejado = int(nivel_desejado_entry.get())

    # Código de calculo aqui

    
    #   *DICIONARIO DINAMICO OCM ADESÃO DE VALORES NA INICIALIZAÇÃO DO PROGRAMA.
    niveis = {
        f'nivel {nivel}': nivel * 100 for nivel in range(0, 100)
    }



    #   Verificação se o nivel atual e o niviel desejado são validos
    if f'nivel {nivel_atual}' in niveis and f'nivel {nivel_desejado}' in niveis:
        xp_necessario = sum(niveis[f'nivel {nivel}'] for nivel in range(nivel_atual + 1, nivel_desejado + 1))
        

        dados_necessarios = 0

        for nivel in range(nivel_atual, nivel_desejado):
            if nivel < 10:
                dados_necessarios += 5
            elif nivel < 20:
                dados_necessarios += 6
            elif nivel < 30:
                dados_necessarios += 8
            elif nivel < 40:
                dados_necessarios += 10
            elif nivel < 50:
                dados_necessarios += 12
            elif nivel < 90:
                dados_necessarios += 15
            else:
                dados_necessarios += 20

        # Calculos para a quantidade de dados adicionais para membros ofensivos
        dados_braço = 3 * (nivel_desejado - nivel_atual)
        dados_perna = 4 * (nivel_desejado - nivel_atual)
        dados_cabeça = 2 * (nivel_desejado - nivel_atual)

        resultado_label.config(text=f"Para chegar do nivel {nivel_atual} ao nivel desejado {nivel_desejado}, você precisará de {xp_necessario} XP.")
        dados_necessarios_label.config(text=f"Você precisará jogar {dados_necessarios} d6's para aumentar seu HP.")
        resultado_braco_label.config(text=f"Você terá que jogar {dados_braço} d6's de aumento de dano do seu membro ofensivo Braço")
        resultado_perna_label.config(text=f"Você terá que jogar {dados_perna} d6's de aumento de dano do seu membro ofensivo Perna")
        resultado_cabeca_label.config(text=f"Você terá que jogar {dados_cabeça} d6's de aumento de dano do seu membro ofensivo Cabeça")

       
    else:
        print("Nível atual ou nivel desejado invalido. Certifique-se de que ambos os niveis estão no intervalo de 1 a 100.")



def on_nivel_atual_entry_return(event):
    # Quando Enter é pressionado no campo Nível atual, mudo o foco para o campo nível desejado.
    nivel_desejado_entry.focus_set()

def on_nivel_desejado_entry_return(event):
    calcular()



#Criando a janela Principal
root = tk.Tk()
root.title("Calculadora de XP")

# Tamanho BASE da janela (largura x altura)
root.geometry("450x450")

# Centralize a janela no monitor
largura_janela = root.winfo_reqwidth()
altura_janela = root.winfo_reqheight()
largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()
posicao_x = (largura_tela - largura_janela) // 2
posicao_y = (altura_tela - altura_janela) // 2
root.geometry(f"+{posicao_x}+{posicao_y}")

#Criar os elementos da interface (rotulos, campos de entrada, botão e rotulos de resultados).
nivel_atual_label = tk.Label(root, text="Nível Atual: ")
nivel_atual_entry = tk.Entry(root)
nivel_desejado_label = tk.Label(root, text="Nível Desejado:")
nivel_desejado_entry = tk.Entry(root)
calcular_button = tk.Button(root, text="Calcular", command=calcular)
resultado_label = tk.Label(root, text="")
dados_necessarios_label = tk.Label(root, text="")
resultado_braco_label = tk.Label(root, text="")
resultado_perna_label = tk.Label(root, text="")
resultado_cabeca_label = tk.Label(root, text="")

#Posiciona os Elementos na janela usando o metodo grid
nivel_atual_label.pack(anchor="center", pady=5)
nivel_atual_entry.pack(anchor="center", pady=5)

nivel_desejado_label.pack(anchor="center", pady=5)
nivel_desejado_entry.pack(anchor="center", pady=5)

nivel_atual_label.pack(pady=10)
nivel_atual_entry.pack(pady=10)
nivel_desejado_label.pack(pady=10)
nivel_desejado_entry.pack(pady=10)
calcular_button.pack(pady=20)
resultado_label.pack(pady=10)
dados_necessarios_label.pack(pady=10)
resultado_braco_label.pack(pady=10)
resultado_perna_label.pack(pady=10)
resultado_cabeca_label.pack(pady=10)


#   Aplicando Evento de retorno utilizando a tecla Enter.
nivel_atual_entry.bind("<Return>", on_nivel_atual_entry_return)
nivel_desejado_entry.bind("<Return>", on_nivel_desejado_entry_return)

#   Iniciando a Interface
root.mainloop()




""" 


nivel_atual = int(input("Qual é o seu nível atual?  "))
nivel_desejado = int(input("Qual nivel você deseja alcançar? "))


print(f"Para chegar do nivel {nivel_atual} ao nivel {nivel_desejado}, você precisa de {xp_necessario} XP.")
print(f"Você precisará jogar {dados_necessarios} d6's para aumentar seu HP")
print(f"Você terá que jogar {dados_braço} d6's de aumento de dano do seu membro ofensivo Braço")
print(f"Você terá que jogar {dados_perna} d6's de aumento de dano do seu membro ofensivo Perna")
print(f"Você terá que jogar {dados_cabeça} d6's de aumento de dano do seu membro ofensivo Cabeça")


"""