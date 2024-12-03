import time
inicio = time.time()
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
            return (0, 0)

        # Verificar se já calculamos para este nó
        if no in memo:
            return memo[no]

        incluído = no.sociabilidade
        excluído = 0

        filho = no.filho_esquerda
        while filho:
            filho_incluído, filho_excluído = dp(filho)
            incluído += filho_excluído
            excluído += max(filho_incluído, filho_excluído)
            filho = filho.irmao_direita

        # Armazenar resultado no cache
        memo[no] = (incluído, excluído)
        return memo[no]

    return dp(no)


def obter_lista_convidados(no, incluir_no=None):
    if no is None:
        return []

    convidados = []
    if incluir_no is None:
        incluído, excluído = calcular_max_sociabilidade(no)
        incluir_no = incluído > excluído

    if incluir_no:
        convidados.append(no.nome)
        filho = no.filho_esquerda
        while filho:
            convidados += obter_lista_convidados(filho, False)
            filho = filho.irmao_direita
    else:
        filho = no.filho_esquerda
        while filho:
            filho_incluído, filho_excluído = calcular_max_sociabilidade(filho)
            if filho_incluído > filho_excluído:
                convidados += obter_lista_convidados(filho, True)
            else:
                convidados += obter_lista_convidados(filho, False)
            filho = filho.irmao_direita

    return convidados


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

# Cálculo
max_incluído, max_excluído = calcular_max_sociabilidade(presidente)
print("Máxima sociabilidade:", max_incluído, max_excluído)
lista_convidados = obter_lista_convidados(presidente)
print("Lista de convidados:", lista_convidados)
print("Total de convidados:", len(lista_convidados))
fim = time.time()
print(fim-inicio)