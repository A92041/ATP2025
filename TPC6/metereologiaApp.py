import matplotlib.pyplot as plt

def medias(tabMeteo):
    return [(data, (temp_min + temp_max) / 2) for (data, temp_min, temp_max, _) in tabMeteo]

def guardaTabMeteo(t, fnome):
    f = open(fnome,'w',encoding='utf-8')
    for registo in t:
        f.write(f"{registo}\n")
    return

def carregaTabMeteo(fnome):
    res = []
    f = open(fnome,"r",encoding = 'utf-8')
    for linha in f:
        res.append(eval(linha.strip()))
    return res

def minMin(tabMeteo):
    return min(temp_min for (_, temp_min, _, _) in tabMeteo)

def amplTerm(tabMeteo):
    return [(data, temp_max - temp_min) for (data, temp_min, temp_max, _) in tabMeteo]

def maxChuva(tabMeteo):
    max_prec = max(prec for (_, _, _, prec) in tabMeteo)
    max_data = next(data for (data, _, _, prec) in tabMeteo if prec == max_prec)
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    return [(data, precipitacao) for (data, _, _, precipitacao) in tabMeteo if precipitacao > p]

def maxPeriodoCalor(tabMeteo, p):
    max_consecutivo = 0
    atual_consecutivo = 0

    for (_, _, _, precipitacao) in tabMeteo:
        if precipitacao < p:
            atual_consecutivo += 1
        else:
            max_consecutivo = max(max_consecutivo, atual_consecutivo)
            atual_consecutivo = 0

    max_consecutivo = max(max_consecutivo, atual_consecutivo)
    return max_consecutivo

def grafTabMeteo(t):
    datas = [f"{data[0]}-{data[1]:02d}-{data[2]:02d}" for (data, _, _, _) in t]
    temp_min = [temp_min for (_, temp_min, _, _) in t]
    temp_max = [temp_max for (_, _, temp_max, _) in t]
    precipitacao = [prec for (_, _, _, prec) in t]

    plt.figure(figsize=(10, 6))

    plt.plot(datas, temp_min, label='Temperatura Mínima (°C)', color='blue', marker='o')
    plt.plot(datas, temp_max, label='Temperatura Máxima (°C)', color='red', marker='o')
    plt.bar(datas, precipitacao, label='Precipitação (mm)', color='lightblue', alpha=0.5)

    plt.xlabel("Data")
    plt.ylabel("Temperatura / Precipitação")
    plt.title("Gráficos de Temperatura e Precipitação")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
    return

def menu():
    tabMeteo = []
    continuar = True
    while continuar:
        print("\nMenu de Operações:")
        print("1: Criar Tabela Meteorológica")
        print("2: Inserir Dados Meteorológicos")
        print("3: Listar Dados Meteorológicos")
        print("4: Calcular Temperatura Média")
        print("5: Calcular Temperatura Mínima")
        print("6: Calcular Amplitude Térmica")
        print("7: Calcular Máxima Precipitação")
        print("8: Listar Dias Chuvosos")
        print("9: Calcular Maior Período de Calor")
        print("10: Mostrar Gráficos de Temperatura e Precipitação")
        print("11: Guardar Tabela em Ficheiro")
        print("12: Carregar Tabela de Ficheiro")
        print("0: Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            tabMeteo = []
            print("Tabela meteorológica criada.")
        elif opcao == "2":
            data = tuple(map(int, input("Insire a data (ano/ mês/ dia): ").split("/")))
            temp_min = float(input("Insire a temperatura mínima: "))
            temp_max = float(input("Insire a temperatura máxima: "))
            precipitacao = float(input("Insire a precipitação: "))
            tabMeteo.append((data, temp_min, temp_max, precipitacao))
            print("Dados inseridos com sucesso.")
        elif opcao == "3":
            if tabMeteo:
                for reg in tabMeteo:
                    print(reg)
            else:
                print("Nenhum dado meteorológico registrado.")
        elif opcao == "4":
            print("Temperaturas médias:", medias(tabMeteo))
        elif opcao == "5":
            print("Temperatura mínima mais baixa:", minMin(tabMeteo))
        elif opcao == "6":
            print("Amplitude térmica:", amplTerm(tabMeteo))
        elif opcao == '7':
            print("Máxima precipitação:", maxChuva(tabMeteo))
        elif opcao == '8':
            p = float(input("Informe o valor da precipitação para listar os dias chuvosos: "))
            print("Dias chuvosos:", diasChuvosos(tabMeteo, p))
        elif opcao == '9':
            p = float(input("Informe o valor de precipitação para calcular o maior período de calor: "))
            print("Maior período de calor:", maxPeriodoCalor(tabMeteo, p))
        elif opcao == '10':
            grafTabMeteo(tabMeteo)
        elif opcao == '11':
            fnome = input("Informe o nome do arquivo para guardar os dados: ")
            guardaTabMeteo(tabMeteo, fnome)
        elif opcao == '12':
            fnome = input("Informe o nome do arquivo para carregar os dados: ")
            tabMeteo = carregaTabMeteo(fnome)
            print(f"Dados carregados de {fnome}.")
        elif opcao == '0':
            print("Saindo da aplicação...")
            continuar = False  # Condição para sair do loop
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()



