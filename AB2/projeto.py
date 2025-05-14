class Lei: # Padrão de Design Observer (o objeto pode notificar outros objetos sobre mudanças em seus estados)
    def __init__(self): # A classe Lei permite que os funcionários sejam notificados sobre mudanças nas leis
        self.nome = "N/D"
        self.termo_logico_1 = "N/D"
        self.condição = "N/D"
        self.termo_logico_2 = "N/D"
        self.observers = []

    def adicionar_observer(self, observer):
        self.observers.append(observer)

    def remover_observer(self, observer):
        self.observers.remove(observer)

    def notificar_observers(self):
        for observer in self.observers:
            observer.atualizar()

    def set_nome(self, nome):
        self.nome = nome
        self.notificar_observers()


class Benefício_Desconto(Lei):
    def __init__(self):
        super().__init__()
        self.tipo_de_aumento = "N/D"
        self.quantia = 0


class Funcionários:
    def __init__(self):
        self.nome = "N/D"
        self.senha = "N/D"
        self.idade = 0
        self.função = "N/D"
        self.salario = 0
        self.salario_total = 0
        self.horas_semanais = 0
        self.status = "N/D"
        self.nota_média = 0
        self.nota_liderança = 0
        self.nota_desempenho = 0
        self.nota_profissionalismo = 0
        self.nota_habilidades_interpessoais = 0
        self.descrição = "N/D"
        self.faltas = 0
        self.benefícios_totais = 0
        self.benefícios = []
        self.descontos_totais = 0
        self.descontos = []
        self.leis = []
        self.prioridade = 0  # Atributo de prioridade

    def Print_Informação_Funcionário_teste(self):
        print(f"""
        Nome: {self.nome}
        Idade: {self.idade}
        Cargo: {self.função}
        Salário Base: {self.salario}
        Salário Total: {self.salario_total}
        Benefícios Totais: {self.benefícios_totais}
        Descontos Totais: {self.descontos_totais}
        Horários: {self.horas_semanais}
        Status: {self.status}\n""")


class FuncionarioObserver: # observador que se inscreve para receber notificações da classe Lei
    def __init__(self, funcionario):
        self.funcionario = funcionario

    def atualizar(self):
        print(f"O funcionário {self.funcionario.nome} foi notificado sobre a mudança na lei.")


class Gerente(Funcionários): # Padrão de Design Singleton (apenas uma instância dessa classe pode existir)
    _instancia = None

    def __new__(cls, *args, **kwargs): # controle da criação da instância. Se a instância já existir, ele retorna. Se não, cria uma nova.
        if not cls._instancia:
            cls._instancia = super(Gerente, cls).__new__(cls)
        return cls._instancia

    def __init__(self):
        super().__init__()
        self.prioridade = 1  # Prioridade do Gerente

    def Atualizar_Informações_teste(self, lista_de_funcionários, indice):
        print(f"As Informações do funcionário {lista_de_funcionários[indice].nome} serão atualizadas\n")
        lista_de_funcionários[indice].nome = input("Nome Funcionário: ")
        lista_de_funcionários[indice].senha = input("Senha do Funcionário: ")
        lista_de_funcionários[indice].idade = int(input("Idade do Funcionário: "))
        lista_de_funcionários[indice].função = input("Função do Funcionário: ")
        lista_de_funcionários[indice].salario = float(input("Salário do Funcionário: "))
        lista_de_funcionários[indice].horas_semanais = int(input("Carga horária do Funcionário (horas/semana): "))
        lista_de_funcionários[indice].status = "Ativo"
        return lista_de_funcionários


class Chefe(Gerente):
    def __init__(self):
        super().__init__()
        self.prioridade = 2  # Prioridade do Chefe


class FuncionarioAdapter: # Padrão de Design Adapter (permite que a classe Funcionários se integre com um sistema de relatórios)
    def __init__(self, funcionario):
        self.funcionario = funcionario

    def obter_dados_relatorio(self): # transforma os dados do funcionário em um formato que pode ser lido pelo sistema de relatórios
        return {
            "nome": self.funcionario.nome,
            "salario": self.funcionario.salario,
            "status": self.funcionario.status
        }


class Relatorio:
    def gerar_relatorio(self, funcionario):
        return f"Relatório: {funcionario.nome}, Salário: {funcionario.salario}"


def input_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: Por favor, digite apenas números inteiros.")


def criar_conta(lista_de_funcionários):
    nome = input("Digite o nome do funcionário: ")
    senha = input("Digite a senha do funcionário: ")
    idade = input_inteiro("Digite a idade do funcionário: ")
    função = input("Digite a função do funcionário (Chefe/Gerente/Funcionário): ")

    novo_funcionário = None
    if função.lower() == "chefe":
        novo_funcionário = Chefe()
    elif função.lower() == "gerente":
        novo_funcionário = Gerente()
    else:
        novo_funcionário = Funcionários()

    novo_funcionário.nome = nome
    novo_funcionário.senha = senha
    novo_funcionário.idade = idade
    novo_funcionário.função = função
    lista_de_funcionários.append(novo_funcionário)
    print(f"Conta criada com sucesso para {nome}!")


def fazer_login(lista_de_funcionários):
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    for funcionário in lista_de_funcionários:
        if funcionário.nome == nome and funcionário.senha == senha:
            print(f"Login bem-sucedido! Bem-vindo, {funcionário.nome}.")
            return funcionário  # Retorna o objeto do funcionário logado

    print("Nome ou senha incorretos.")
    return None


def main():
    lista_de_funcionários = []

    while True:
        print("\nGerenciador de RH\n")
        print("1. Criar conta")
        print("2. Fazer login")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            criar_conta(lista_de_funcionários)
        elif escolha == '2':
            funcionário_logado = fazer_login(lista_de_funcionários)
            if funcionário_logado:
                if isinstance(funcionário_logado, Chefe):
                    print("\nVocê está logado como Chefe.\n")
                    print("1. Adicionar funcionário")
                    print("2. Remover funcionário")
                    print("3. Sair")
                    escolha_chefe = input("\nEscolha uma opção: ")

                    if escolha_chefe == '1':
                        criar_conta(lista_de_funcionários)
                    elif escolha_chefe == '2':
                        pass
                    elif escolha_chefe == '3':
                        print("\nSaindo...")
                        break

                elif isinstance(funcionário_logado, Gerente):
                    print("Você está logado como Gerente.")
                    print("1. Atualizar informações")
                    print("2. Sair")
                    escolha_gerente = input("\nEscolha uma opção: ")

                    if escolha_gerente == '1':
                        funcionario_index = int(input("Digite o índice do funcionário a ser atualizado: "))
                        funcionário_logado.Atualizar_Informações_teste(lista_de_funcionários, funcionario_index)
                    elif escolha_gerente == '2':
                        print("\nSaindo...")
                        break

                elif isinstance(funcionário_logado, Funcionários):
                    print("Você está logado como Funcionário.")
                    print("1. Exibir informações")
                    print("2. Sair")
                    escolha_funcionario = input("\nEscolha uma opção: ")

                    if escolha_funcionario == '1':
                        funcionário_logado.Print_Informação_Funcionário_teste()
                    elif escolha_funcionario == '2':
                        print("\nSaindo...")
                        break

        elif escolha == '3':
            print("\nSaindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()