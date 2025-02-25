def escolher_cultura():
    """
    Permite ao usuário selecionar duas culturas distintas para trabalhar.

    O usuário deve inserir os nomes das culturas desejadas (exemplo: soja, milho).
    Se uma cultura já tiver sido escolhida, será solicitado que escolha uma diferente.
    O processo continua até que duas culturas distintas sejam selecionadas.

    Returns:
        list: Uma lista contendo as duas culturas escolhidas pelo usuário.
    """
    culturas = []
    while len(culturas) < 2:
        cultura = input("Digite a cultura que deseja trabalhar (soja/milho ou qualquer outra): ").lower()
        if cultura not in culturas:
            culturas.append(cultura)
        else:
            print("Cultura já escolhida. Por favor, escolha uma cultura diferente.")
    print(f"As culturas escolhidas foram: {culturas}")
    return culturas
