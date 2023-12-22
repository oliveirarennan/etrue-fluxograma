# coding=utf-8
from graphviz import Digraph
from PIL import Image

# Cria um novo grafo direcionado
fluxograma = Digraph(comment='Fluxograma de Requisitos')

# Adiciona nós e arestas ao fluxograma
fluxograma.node('A', 'Início')
fluxograma.node('B', 'Solicitar Reserva')
fluxograma.node('C', 'E-mail existe na base de dados ?')
fluxograma.edges(['AB', 'BC'])

fluxograma.edge('C', 'D', label='Não')
fluxograma.node('D', 'Solicitar dados Para cadastro')
fluxograma.node('E', 'Dados estão corretos ?')
fluxograma.edges(['DE'])
fluxograma.node('F', 'Cadastrar Usuário')
fluxograma.edge('E', 'F', label='Sim')
fluxograma.node('G', 'Enviar e-mail de confirmação de cadastro')
fluxograma.node('H', 'Precisa de pagamento antecipado ?')
fluxograma.edges(['FG', 'GH'])
fluxograma.node('I', 'Enviar e-mail com instruções de pagamento')
fluxograma.edge('H', 'I', label='Sim')
fluxograma.node('J', 'Cliente efetuou o pagamento ?')
fluxograma.edge('J', 'L', label='Sim')
fluxograma.edges(['IJ'])
fluxograma.node('L', 'Enviar e-mail de confirmação de pagamento')
fluxograma.node('M', 'Ainda Está no prazo ?')
fluxograma.node('N', 'Aguardar')
fluxograma.node('O', 'Cancelar Reserva')
fluxograma.edge('J', 'M', label='Não')
fluxograma.edge('M', 'N', label='Sim')
fluxograma.edge('M', 'O', label='Não')
fluxograma.edges(['NJ'])
fluxograma.node('P', 'Enviar e-mail de confirmação de reserva')
fluxograma.edge('H', 'P', label='Não')
fluxograma.edges(['LP'])

fluxograma.edge('E', 'Q', label='Não')
fluxograma.node('Q', 'Informar error nos dados informados')
fluxograma.edges(['QE'])

fluxograma.edge('C', 'H', label='Sim')

fluxograma.node('R', 'Fim')
fluxograma.edges(['PR', 'OR'])


# Renderiza o fluxograma para um arquivo
fluxograma.render('./fluxograma', format='pdf', cleanup=True)
