import time

class Funcionario:
    def __init__(self, nome, sociabilidade, filho_esquerda=None, irmao_direita=None):
        self.nome = nome
        self.sociabilidade = sociabilidade
        self.filho_esquerda = filho_esquerda
        self.irmao_direita = irmao_direita

def calcular_max_sociabilidade(no):
    memo = {}

    def dp(no):
        if no is None:
            return (0, [], 0, [])

        # Verificar se já calculamos para este nó
        if no in memo:
            return memo[no]

        # Caso 1: Incluir o nó atual
        incluído = no.sociabilidade
        convidados_incluídos = [no.nome]

        # Caso 2: Excluir o nó atual
        excluído = 0
        convidados_excluídos = []

        # Processar os filhos
        filho = no.filho_esquerda
        while filho:
            filho_incluído, lista_incluídos, filho_excluído, lista_excluídos = dp(filho)

            # Atualizar valores para o caso de inclusão e exclusão
            incluído += filho_excluído
            convidados_incluídos += lista_excluídos

            excluído += max(filho_incluído, filho_excluído)
            if filho_incluído > filho_excluído:
                convidados_excluídos += lista_incluídos
            else:
                convidados_excluídos += lista_excluídos

            filho = filho.irmao_direita

        # Armazenar no cache
        memo[no] = (incluído, convidados_incluídos, excluído, convidados_excluídos)
        return memo[no]

    # Executar o algoritmo na raiz
    incluído, convidados_incluídos, excluído, convidados_excluídos = dp(no)

    return (incluído, convidados_incluídos, excluído, convidados_excluídos)
    
def obter_lista_convidados(raiz):
    incluído, convidados_incluídos, excluído, convidados_excluídos = calcular_max_sociabilidade(raiz)
    if incluído > excluído:
        return (convidados_incluídos, incluído)
    else:
        return (convidados_excluídos, excluído)

inicio = time.time()

# Criação da árvore com 15 níveis
presidente = Funcionario("Presidente", 20)


# Função para criar níveis recursivamente
def criar_nivel(nivel_atual, max_niveis, sociabilidade_base):
    if nivel_atual >= max_niveis:
        return None

        # Increase branching - now 5 nodes per level instead of 3
    pessoa = Funcionario(f"Nivel{nivel_atual}", sociabilidade_base + nivel_atual * 2)
    pessoa.irmao_direita = Funcionario(f"Nivel{nivel_atual}B", sociabilidade_base + nivel_atual * 2 + 1)
    pessoa.irmao_direita.irmao_direita = Funcionario(f"Nivel{nivel_atual}C",
                                                         sociabilidade_base + nivel_atual * 2 + 2)
    pessoa.irmao_direita.irmao_direita.irmao_direita = Funcionario(f"Nivel{nivel_atual}D",
                                                                       sociabilidade_base + nivel_atual * 2 + 3)
    pessoa.irmao_direita.irmao_direita.irmao_direita.irmao_direita = Funcionario(f"Nivel{nivel_atual}E",
                                                                                     sociabilidade_base + nivel_atual * 2 + 4)

        # More complex recursion
    pessoa.filho_esquerda = criar_nivel(nivel_atual + 1, max_niveis, sociabilidade_base + 10)

    return pessoa


# Construir árvore com 15 níveis
presidente.filho_esquerda = criar_nivel(1, 900, 10)
presidente.filho_esquerda.irmao_direita = criar_nivel(10, 900, 20)
presidente.filho_esquerda.irmao_direita.irmao_direita = criar_nivel(10, 900, 30)



(lista_convidados, soma_max) = obter_lista_convidados(presidente)
print("Lista de convidados:", lista_convidados)
print("Soma máxima de sociabilidade:", soma_max)
fim = time.time()
print(fim-inicio)