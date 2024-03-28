import networkx as nx
import matplotlib.pyplot as plt

# Criar um grafo
G = nx.Graph()

# Adicionar arestas
G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'A')

# Plotar o grafo
nx.draw(G, with_labels=True, font_weight='bold')

# Exibir o gráfico
plt.show()

# para vc instalar alan "pip install networkx matplotlib" so colar no terminal