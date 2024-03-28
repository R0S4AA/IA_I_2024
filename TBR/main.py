import PySimpleGUI as sg
import funcoes_auxiliares as fa
import busca_sem_peso_UNITAU as bs


# Funções de busca disponíveis
FUNCOES_BUSCA = {
  'Amplitude': 'amplitude',
  'Profundidade': 'profundidade',
  'Profundidade Limitada': 'prof_limitada',
  'Aprofundamento Iterativo': 'aprof_iterativo'
}

# Layout da janela
layout = [
  [sg.Text('Origem:'), sg.InputText(key='-ORIGEM-')],
  [sg.Text('Destino:'), sg.InputText(key='-DESTINO-')],
  [sg.Text('Escolha a função de busca:')],
  [sg.Combo(list(FUNCOES_BUSCA.keys()), key='-FUNCAO_BUSCA-')],
  [sg.Button('Buscar'), sg.Button('Sair')],
  [sg.Text('Resultado da busca:')],
  [sg.Output(size=(70, 30))]
]

# Criar a janela
window = sg.Window('Busca em Grafo', layout)

# Loop para interação com a janela
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == 'Buscar':
        origem = str(values['-ORIGEM-'])
        destino = str(values['-DESTINO-'])
        if origem.strip() == '' or destino.strip() == '':
            print('Por favor, insira a origem e o destino.')
            continue
        if values['-FUNCAO_BUSCA-'] not in FUNCOES_BUSCA:
            print('Por favor, selecione uma função de busca válida.')
            continue

        # Carregar o grafo
        nos, grafo = fa.Gera_Problema("grafo_teste.txt")

        # Verificar se a origem e o destino estão na lista de nós
        if origem not in nos or destino not in nos:
            print("Origem e ou Destino fora do servidor")
            continue

        # Realizar a busca selecionada
        sol = bs.busca()
        if values['-FUNCAO_BUSCA-'] == 'Amplitude':
            print('Aplicando Amplitude')
            caminho = sol.amplitude(origem, destino, nos, grafo)
        
        elif values['-FUNCAO_BUSCA-'] == 'Profundidade':
            print('Aplicando Profundidade')
            caminho = sol.profundidade(origem, destino, nos, grafo)
        
        elif values['-FUNCAO_BUSCA-'] == 'Profundidade Limitada':
            limite = sg.popup_get_text('Insira o limite:')
            if limite is None:
                continue 
            print('Aplicando Profundidade limitada, com limite = ', limite)
            caminho = sol.prof_limitada(origem, destino, nos, grafo, int(limite))
        
        elif values['-FUNCAO_BUSCA-'] == 'Aprofundamento Iterativo':
            profundidade_maxima = sg.popup_get_text('Insira a profundidade máxima:')
            if profundidade_maxima is None:
                continue 
            print('Aplicando Aprofundamento Iterativo com limite máximo de: ', profundidade_maxima)
            caminho = sol.aprof_iterativo(origem, destino, nos, grafo, int(profundidade_maxima))

        # Exibir o resultado
        print("\nResultado da busca:")
        print("Caminho encontrado:", caminho)
        print("Custo do caminho:", len(caminho) - 1)
        print("\n\n")
        

# Fechar a janela ao finalizar
window.close()
