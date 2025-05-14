# 📚 Sistema de Gerenciamento de Biblioteca

Este é um projeto desenvolvido para o Grupo de Estudos  **Introdução à Ciência de Dados**, com o objetivo de criar um sistema de gerenciamento de uma biblioteca
utilizando **Programação Orientada a Objetos (POO)** e **Estruturas de dados**

---

## 🧠 Conceitos abordados

O projeto utiliza os principais pilares da Programação Orientada a Objetos:

- **Herança:** Classes específicas como `LivroFisico`, `LivroDigital`, `UsuarioRegular` e `UsuarioVIP` herdam de classes genéricas (`Livro` e `Usuario`).
- **Polimorfismo:** Cada tipo de livro e usuário pode sobrescrever métodos como `exibir_detalhes`.
- **Encapsulamento:** Os atributos das classes são protegidos por convenção (`_atributo`) e acessados por métodos específicos (`get_`/`set_`).
- **Abstração:** As classes `Livro` e `Usuario` são **abstratas** e servem apenas como base para as demais.

Também utilizei uma **Lista Encadeada Simples** para armazenar livros e usuários, simulando um tipo de banco de dados leve sem usar bibliotecas externas.

---

## 🏗️ Estrutura do Projeto

- `Livro`: Classe abstrata para livros
  - `LivroFisico`: Livro que pode ser emprestado
  - `LivroDigital`: Livro que não pode ser emprestado , pelo acesso ser digital
- `Usuario`: Classe abstrata para usuários
  - `UsuarioRegular`: Pode pegar até 3 livros emprestados
  - `UsuarioVIP`: Pode pegar até 10 livros emprestados
- `ListaEncadeada`: Implementação de lista encadeada para armazenar livros e usuários
- `Biblioteca`: Classe principal que gerencia todos os dados e operações
- `menu()`: Interface via terminal para interação com o usuário
