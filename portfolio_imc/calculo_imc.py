def calcular_imc(peso: float, altura: float) -> float:
    assert peso > 0, "Peso deve ser maior que zero!"
    assert altura > 0, "Altura deve ser maior que zero!"
    
    return peso / altura**2


def classificar(imc: float) -> str:
    assert imc, "IMC deve ser maior que zero!"

    match imc:
        case indice if indice < 18.5:
            return "Magreza"
        case indice if 18.5 <= indice < 25:
            return "Normal"
        case indice if 25 <= indice < 30:
            return "Sobrepeso"
        case indice if 30 <= indice < 35:
            return "Obesidade grau I"
        case indice if 35 <= indice < 40:
            return "Obesidade grau II"
        case _:
            return "Obesidade grau III"


def main(*args, **kwargs):
    print("=== Cálculo do IMC ===")
    print ("* Digite 'x' em um dos campos para sair")

    input_peso = input("Informe o peso (Kg): ")
    if input_peso == "x": return "x"

    input_altura = input("Informe a altura (m): ")
    if input_altura == "x": return "x"

    try:
        peso = float(input_peso)
        altura = float(input_altura)
    except Exception:
        print("###> Peso e/ou altura inválido(s)! <###")
        return

    imc = calcular_imc(peso=peso, altura=altura)
    classificacao = classificar(imc=imc)

    print("\n--- Relatório ---")
    print(f"- Peso: {peso} Kg")
    print(f"- Altura: {altura} metro(s)")
    print(f"- IMC: {round(imc, 2)}")
    print(f"- Classificação: {classificacao}")
    print("-----------------\n")


if __name__ == "__main__":
    sair = ""

    while(sair != "x"):
        sair = main()
    
    print("### Programa finalizado ###")
