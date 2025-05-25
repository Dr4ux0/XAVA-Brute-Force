import itertools

def clean_input(prompt):
    inp = input(prompt).strip()
    if not inp:
        return []
    # Remove espaços dentro das palavras compostas e separa por vírgula
    parts = [x.strip().replace(" ", "") for x in inp.split(",") if x.strip()]
    return parts

def capitalize_variations(words):
    variations = set()
    for w in words:
        variations.add(w)
        if len(w) > 1:
            variations.add(w.capitalize())
            variations.add(w.lower())
            variations.add(w.upper())
    return variations

def reversed_variations(words):
    return {w[::-1] for w in words}

def generate_wordlist(data):
    base_words = set()
    for key in data:
        base_words.update(data[key])

    base_words = capitalize_variations(base_words)
    base_words.update(reversed_variations(base_words))

    combined = set(base_words)
    for w in base_words:
        for n in data.get("numeros_comuns", []):
            combined.add(f"{w}{n}")
            combined.add(f"{n}{w}")

    return sorted(combined)

def main():
    print("=== Gerador de Wordlist Personalizada ===\n")

    resposta = input("Deseja criar uma wordlist personalizada? (s/n): ").strip().lower()
    if resposta != "s":
        print("Encerrando.")
        return

    dados = {}
    print("Caso não queira adiciona tal informação teclar Enter para pular")
    dados["nome_principal"] = clean_input("Nome principal: ")
    dados["nome_parceiro"] = clean_input("Nome do parceiro(a): ")
    dados["nome_filho"] = clean_input("Nome do filho(a): ")
    dados["datas_importantes"] = clean_input("Datas importantes (ex: 2001,1012): ")
    dados["palavras_extras"] = clean_input("Palavras extras: ")
    dados["numeros_comuns"] = clean_input("Números comuns (ex: 123,2024): ")
    dados["series"] = clean_input("Nomes de séries, filmes ou palavras específicas: ")
    dados["animes"] = clean_input("Nomes de animes favoritos: ")
    dados["comidas"] = clean_input("Nomes de comidas favoritas: ")
    dados["numeros_telefone"] = clean_input("Números de telefone: ")
    dados["nome_pet"] = clean_input("Nome(s) de pet: ")

    todas_palavras = {}
    chaves_palavras = ["nome_principal", "nome_parceiro", "nome_filho",
                       "palavras_extras", "series", "animes", "comidas", "nome_pet"]
    for chave in chaves_palavras:
        todas_palavras[chave] = dados.get(chave, [])

    todas_palavras["numeros_comuns"] = dados.get("numeros_comuns", []) + dados.get("numeros_telefone", [])

    print("\nGerando combinações...")

    wordlist = generate_wordlist(todas_palavras)

    arquivo = "wordlist_custom.txt"
    with open(arquivo, "w", encoding="utf-8") as f:
        for w in wordlist:
            f.write(w + "\n")

    print(f"Wordlist criada com {len(wordlist)} variações no arquivo {arquivo}")

if __name__ == "__main__":
    main()
