import cinema as sala

sala1 = (150, [], "Twilight")
sala2 = (200, [], "Hannibal")
cinema1 = []

# Inserir salas
cinema1 = sala.inserirSala(cinema1, sala1)
cinema1 = sala.inserirSala(cinema1, sala2)

# Listar filmes
sala.listar(cinema1)

# Verificar disponibilidade (corrigido: usar nome do filme)
print("\nLugar 2 disponível em Twilight?")
print(sala.disponivel(cinema1, "Twilight", 2))

# Vender vários bilhetes para Twilight
for lugar in range(1, 151):
    cinema1 = sala.vendebilhete(cinema1, "Twilight", lugar)

# Mostrar disponibilidade após vendas
sala.listardisponibilidades(cinema1)

# Listar novamente para confirmar
sala.listar(cinema1)