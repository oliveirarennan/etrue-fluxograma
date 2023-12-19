# coding=utf-8
from graphviz import Digraph
from PIL import Image

# Cria um novo grafo direcionado
fluxograma = Digraph(comment='Fluxograma de Requisitos')

# Adiciona nós e arestas ao fluxograma
fluxograma.node('A', 'Início')
# fluxograma.node('B', 'Processo 1')
# fluxograma.node('C', 'Decisão')
# fluxograma.node('D', 'Processo 2')
# fluxograma.node('E', 'Fim')
# fluxograma.node('F', 'Processo 3')

# fluxograma.edges(['AB', 'BC'])
# fluxograma.edges(['DF', 'FE'])
# fluxograma.edge('C', 'D', label='Sim')
# fluxograma.edge('C', 'E', label='Não')

fluxograma.node('B', 'PASSO 1')
fluxograma.node('C', 'PASSO 2')
fluxograma.node('D', 'ISSO FUNCIONA ?')
fluxograma.edges(['BC', 'CD'])
fluxograma.edge('D', 'E', label='NÃO')
fluxograma.edge('E', 'C')

# Renderiza o fluxograma para um arquivo
fluxograma.render('./fluxograma', format='pdf', cleanup=True)
