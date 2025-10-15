# Aplicação para gerir um cinema
# ----------------------
# Modelo:
# Cinema = [Sala]
# Sala = [nlugares, Vendidos, filme]
# nlugares = Int
# filme = String 
# Vendidos = [Int]


def inserirSala( cinema, sala ):
    return cinema + [sala] 

def listar( cinema ):
    for sala in cinema:
        print(f" {sala[2]}")
    return

def disponivel( cinema, filme, lugar ):
    for sala in cinema:
        if sala[2] == filme:
            return lugar not in sala[1]
    return False

def vendebilhete( cinema, filme, lugar ):
    for sala in cinema:
        if sala[2] == filme:
            if lugar not in sala[1]:
                sala[1].append(lugar)
                print(f"Bilhete vendido para o lugar {lugar} em '{filme}'")
            else:
                print("Lugar já ocupado.")
            return cinema
    print("Filme não encontrado.")
    return cinema

def listardisponibilidades( cinema ):
    for sala in cinema:
        disponiveis = sala[0] - len(sala[1])
        print(f"{sala[2]} :: {disponiveis} lugares disponíveis")
    return


def menu():
    print(""" 
    (1) Reset
    (2) Criar Sala
    (3) Listar filmes em exibição
    (4) Consultar Disponibilidade de Lugar
    (5) Vender Bilhete
    (6) Listar Disponibilidades
    (7) Alterar Filme em Exibição
    ...
    (0) Sair
    """)