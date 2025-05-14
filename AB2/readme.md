# Projeto de Software - 2024.2

Discente: Athisson Alberto Lima Marques\
Docente: Baldoino Fonseca dos Santos Neto


# Apresentação

Projeto final refatorado com implementações dos padrões de design.


# Padrões

Para elaboração do projeto, os seguintes padrões de design foram implementados:

- Criacional (Singleton):
  -  Utilizado na classe Gerente;
  -  Garantia de que apenas uma instância da classe Gerente exista durante a execução do programa.

- Estrutural (Adapter):
  - Utilizado na classe Funcionario;
  - Permite que a classe Funcionários se integre com um sistema de relatórios, transformando dados em um formato utilizável.

- Comportamental (Observer):
  - Utilizado nas classes Leis e FuncionarioObserver;
  - Facilita a notificação de funcionários sobre mudanças nas leis, permitindo um sistema reativo e dinâmico.
