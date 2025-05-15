def unidades(n):
    return [
        "", "um", "dois", "três", "quatro", "cinco",
        "seis", "sete", "oito", "nove"
    ][n]

def dezenas(n):
    dez = [
        "", "dez", "vinte", "trinta", "quarenta", "cinquenta",
        "sessenta", "setenta", "oitenta", "noventa"
    ]
    especiais = [
        "dez", "onze", "doze", "treze", "quatorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove"
    ]
    if 10 <= n <= 19:
        return especiais[n-10]
    else:
        d = n // 10
        u = n % 10
        if d == 0:
            return unidades(u)
        elif u == 0:
            return dez[d]
        else:
            return f"{dez[d]} e {unidades(u)}"

def centenas(n):
    cent = [
        "", "cem", "duzentos", "trezentos", "quatrocentos",
        "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"
    ]
    if n == 100:
        return "cem"
    c = n // 100
    r = n % 100
    if c == 0:
        return dezenas(r)
    elif r == 0:
        return cent[c]
    else:
        return f"{cent[c][:-1]}entos e {dezenas(r)}" if c == 1 else f"{cent[c]} e {dezenas(r)}"

def milhares(n):
    m = n // 1000
    r = n % 1000
    if m == 0:
        return centenas(r)
    elif m == 1:
        if r == 0:
            return "mil"
        else:
            return f"mil e {centenas(r)}"
    else:
        if r == 0:
            return f"{unidades(m)} mil"
        else:
            return f"{unidades(m)} mil e {centenas(r)}"

def numero_por_extenso(n):
    if not (0 <= n <= 9999):
        return "Número fora do intervalo suportado (0-9999)."
    if n == 0:
        return "zero"
    return milhares(n)

def main():
    print("=== Conversor de Números para Extenso ===")
    while True:
        entrada = input("Digite um número inteiro entre 0 e 9999 (ou 'sair' para encerrar): ").strip().lower()
        if entrada == 'sair':
            print("Até a próxima!")
            break
        if not entrada.isdigit():
            print("Por favor, digite apenas números inteiros.")
            continue
        n = int(entrada)
        print(f"\n🔢 {n} por extenso: {numero_por_extenso(n)}\n")

if __name__ == "__main__":
    main()
