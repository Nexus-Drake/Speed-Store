automoveis = ["fusca", "civic","kawasaki ninja"]
velocidades = [130, 220, 400]
ceos = ["Joice", "Victor", "Nathan","Kayke"]

while True:
    print("\n")
    print("🚗  🏍️  " * 6)
    print("         BEM-VINDO(S) A SPEED STORE!")
    print("🚗  🏍️  " * 6)
    print('\nComo podemos te ajudar hoje? \n')
    print('1. Cadastrar veículos.')
    print('2. Pesquisar veículos.')
    print('3. Remover veículos.')
    print('4. Alterar veículos.')
    print('5. Mostrar veículos.')
    print('6. CEOs da SPEED STORE.')
    print('7. Encerrar Atendimento.')

    try:
      opcao = int(input("\n🚗 Digite a opção desejada: "))
    except ValueError:
        print("​❌ OPÇÃO INVÁLIDA! Por favor, digite um número válido.")
        continue

    if opcao == 1:  # Cadastrar Veículos

        while True:
            try:
                novo_veiculo = input("\nInforme o nome do novo automóvel: ").lower()
                if novo_veiculo in automoveis:
                    print("\n ⚠️  Esse automóvel já está no nosso Sistema!\n​​​​​")
                    continue
                else:
                    automoveis.append(novo_veiculo)
                    while True:
                        try:
                            velocidade = int(input("\nDigite a velocidade máxima do automóvel: "))
                            velocidades.append(velocidade)
                            print("\n Veículo Cadastrado com Sucesso! ✔️ \n​")
                            break
                        except ValueError:
                            print("​\n ​❌ Entrada inválida! Por favor, digite um número válido para a velocidade.\n")
                    break
            except ValueError:
                print("\n ​​❌ Entrada inválida! Por favor, digite um número válido para o nome do automóvel.\n")


    elif opcao == 2:  # Pesquisar Veículos

        try:
            termo_pesquisa = input("\nDigite o nome do automóvel ou a velocidade que deseja pesquisar: ").lower()

            encontrados = []
            for i in range(len(automoveis)):
                if termo_pesquisa in automoveis[i].lower() or termo_pesquisa == str(velocidades[i]):
                    encontrados.append(f"{automoveis[i]} - Velocidade: {velocidades[i]} km/h")

            if encontrados:
                print("\nAutomóveis encontrados:")
                for automoveis in encontrados:
                    print(f"- {automoveis}")
            else:
                print("\n ❌ Nenhum resultado encontrado.\n")
        except ValueError:
            print("\n ❌ Entrada inválida! Certifique-se de digitar corretamente.\n")

    elif opcao == 3:  # Remover Veículos

        while True:
            print("\nEscolha o veículo que deseja remover:")
            for i in range(len(automoveis)):
                print(f"{i + 1}. {automoveis[i]}")
            try:
                indice_remover = int(input("\nDigite o número do veículo que deseja remover: "))
                item_removido = automoveis.pop(indice_remover - 1)
                velocidades.pop(indice_remover- 1 )
                print(f'O item "{item_removido}" foi removido com sucesso! ✔️')
                break
            except IndexError:
                print("\n ❌ Opção inválida! Tente novamente.")
            except ValueError:
                print("\n ❌ Entrada inválida! Por favor, digite um número válido.")

    elif opcao == 4:  # Alterar Veículos

        print("\n O que você deseja alterar?")
        print("1. Automóvel")
        print("2. Velocidade")

        try:
            escolha = int(input("\nDigite a opção desejada: "))

            if escolha == 1:
                for i in range(len(automoveis)):
                    print(f"{i + 1}. {automoveis[i]}")

                while True:
                    try:
                        indice = int(input("\nDigite o número do automóvel que deseja alterar: ")) - 1
                        if indice < 0 or indice >= len(automoveis):
                            print("\n ❌ O número do automóvel não existe. Tente novamente.")
                            continue
                        automoveis[indice] = input("\nDigite o novo nome do automóvel: ")
                        print("\n Automóvel alterado com sucesso! ✔️")
                        print("\nVeículos Atualizados:")
                        for i in range(len(automoveis)):
                            print(f"{automoveis[i]} - Velocidade: {velocidades[i]} km/h")
                        break
                    except (ValueError, IndexError):
                        print("\n ❌ Entrada inválida! O número do automóvel não existe ou entrada não numérica. Tente novamente.")

            elif escolha == 2:

                for i in range(len(velocidades)):
                    print(f"{i + 1}. {automoveis[i]} | {velocidades[i]} km/h")
                while True:
                    try:
                        indice = int(input("\nDigite o número da velocidade que deseja alterar: ")) - 1
                        if indice < 0 or indice >= len(velocidades):
                            print("\n ❌ O número da velocidade não existe. Tente novamente.")
                            continue
                        velocidades[indice] = int(input("\nDigite a nova velocidade máxima: "))
                        print("\n Velocidade alterada com sucesso! ✔️")
                        print("\n Veículos Atualizados:")
                        for i in range(len(automoveis)):
                            print(f"{automoveis[i]} - Velocidade: {velocidades[i]} km/h")
                        break
                    except (ValueError, IndexError):
                        print("\n ❌ Entrada inválida! O número da velocidade não existe ou entrada não numérica. Tente novamente.")

            else:
                print("\n ❌ Opção inválida! Tente novamente.")

        except (ValueError, IndexError):
            print("\n ❌ Entrada inválida! Tente novamente.")

    elif opcao == 5:  # Mostrar veiculos

        print("\nVeículos cadastrados:\n")
        for i in range(len(automoveis)):
            print(f"{automoveis[i]} - Velocidade: {velocidades[i]} km/h\n")

    elif opcao == 6:  # CEOs
        print(" / ".join(ceos))

    elif opcao == 7: # Sair
        print("\n 🚗 Obrigado por usar a Speed Store! Até logo! 🚗\n")
        break

    else:
        print("\n ​❌ OPÇÃO INVÁLIDA! Por favor, digite um número válido.")