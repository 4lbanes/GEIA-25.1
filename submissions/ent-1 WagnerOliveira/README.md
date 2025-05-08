Desafio - Sistema de Biblioteca com Programação Orientada a
Objetos e Estruturas de Dados
===


Descrição do Desafio
===

Você será responsável por criar um sistema de gerenciamento de uma biblioteca
utilizando Programação Orientada a Objetos (POO) e as estruturas de dados que
você aprendeu, como listas encadeadas e filas. O sistema deverá ser capaz de
realizar as seguintes operações:

1. Cadastro de Livros:
Cada livro possui um título, autor, ano de publicação e um status que
indica se está disponível ou emprestado.
2. Empréstimo e Devolução de Livros:
O sistema deve ser capaz de emprestar um livro a um usuário ou registrar
a devolução de um livro. Antes de realizar o empréstimo, é necessário
verificar se o livro está disponível. Quando o livro é devolvido, o status
deve ser alterado para disponível novamente.
3. Gerenciamento de Usuários:
Cada usuário terá informações como nome, e-mail e uma lista de livros
emprestados. Será necessário implementar funcionalidades para adicionar
e remover livros dessa lista de acordo com os empréstimos e devoluções.
4. Busca de Livros:
O sistema deve permitir que o usuário busque livros por título ou autor. A
busca deve ser eficiente e retornar uma lista com todos os livros que
correspondem ao critério de busca.
5. Relatório de Livros Emprestados:
O sistema deve gerar um relatório com todos os livros que estão
emprestados, juntamente com o nome do usuário que os pegou. Esse
relatório pode ser exibido em formato de lista ou tabela.


Requisitos Técnicos:
===

1. Utilização de Classes:
○ Livros: Cada livro será representado por uma classe Livro que
possui os atributos título, autor, ano de publicação e status
(disponível ou emprestado).
○ Usuários: Cada usuário será representado por uma classe Usuario
com atributos como nome, email e lista de livros emprestados.
○ Biblioteca: A classe Biblioteca gerenciará a coleção de livros e os
usuários, fornecendo métodos para adicionar, buscar e emprestar
livros.
2. Estruturas de Dados:
Utilize listas encadeadas ou filas para organizar os livros e usuários. Essas
estruturas são ideais para gerenciar a coleção de livros e os registros dos
usuários de forma eficiente.S
3. Polimorfismo e Herança:
○ Polimorfismo: Aplique polimorfismo criando diferentes tipos de
livros, como "livros físicos" e "livros digitais". Cada tipo de livro pode
ter comportamentos específicos, mas todos devem compartilhar a
interface comum de livro.
○ Herança: Crie diferentes tipos de usuários (como "usuário regular" e
"usuário VIP"). O usuário VIP pode ter privilégios adicionais, como a
capacidade de emprestar mais livros ou ter prazos de devolução
mais longos. Ambos os tipos de usuários devem herdar de uma
classe base Usuario.
4. Encapsulamento:
○ Aplique o encapsulamento nos atributos das classes Livro e Usuario.
Os dados internos devem ser protegidos e acessados através de
métodos públicos. Por exemplo, o status de um livro pode ser
alterado apenas por métodos que realizem verificações de
disponibilidade.
5. Abstração:
Use a abstração para criar interfaces para as operações de empréstimo e
devolução. Defina um método abstrato para as operações de empréstimo
e devolução nas classes relevantes, garantindo que cada tipo de livro ou
usuário implemente esses métodos de forma específica.

Indice
---
<!--ts-->   
   * [Tecnologias](#🛠-tecnologias-utilizadas)
   * [Criação Virtualenv](#criação-virtualenv)
   * [Instalação Pacotes](#instalação-de-pacotes)
   * [Acessando Virtualenv](#acessando-virtualenv---wsl-linux)
   * [Código](#código)
     * [Classe Biblioteca](#documentação-da-classe-biblioteca)
     * [Classe Livro](#documentação-das-classes-de-livros-livro-livrofisico-livrodigital)
     * [Classe Usuario](#documentação-das-classes-de-usuários-usuario-usuarioregular-usuariovip)
     * [Web Interface](#)
   * [Referências](#referências)
   * [Contribuição](#contribuição)
   * [Autor](#autores)
   * [Licença](#licença)
<!--te-->

🛠 Tecnologias Utilizadas
---
As seguintes ferramentas foram usadas na construção do projeto:

- [Python 3.13.0](https://docs.python.org/pt-br/3/)
- [Flask 3.1.0](https://flask.palletsprojects.com/en/stable/installation/)


Criação Virtualenv
---


~~~bash
python3 -m venv .venv
~~~


Acessando Virtualenv - WSL, Linux
---


~~~bash
source .venv/bin/activate
~~~


Acessando Virtualenv - Windows
---


~~~bash
.venv/Scripts/activate.bat
~~~


Instalação de Pacotes
---


~~~bash
python -m pip install -r requirements.txt
~~~


Código
===

Dentro do diretório compomentes contem 3 arquivos: 
 
* biblioteca.py resposavel pela classe Biblioteca
* livro.py resposavel pela classe Livro
* usuario.py resposavel pela classe Usuario


Documentação da Classe Biblioteca
---

Este documento descreve a funcionalidade da classe Biblioteca, que é a parte central do sistema de gerenciamento da sua biblioteca. Esta classe orquestra as operações envolvendo livros e usuários, permitindo adicionar itens, buscar, emprestar e devolver livros, além de gerar relatórios.

1. Visão Geral

A classe Biblioteca atua como o ponto de controle principal do sistema. Ela mantém registros de todos os livros e usuários e fornece os métodos necessários para interagir com eles de forma organizada. Ela depende de outras classes, Livro e Usuario, que representam os objetos individuais de livros e usuários, respectivamente.

2. Inicialização (Constutor __init__)

Quando você cria uma nova instância da classe Biblioteca, ela é inicializada vazia, pronta para gerenciar livros e usuários.

Como funciona:
Ao executar o comando para criar uma Biblioteca, o sistema prepara duas listas vazias internamente: uma para armazenar todos os objetos Livro adicionados e outra para armazenar todos os objetos Usuario adicionados.
3. Adicionar Livro (adicionar_livro)

Este método permite incluir um novo livro no acervo da biblioteca.

Como funciona:
Você fornece um objeto que represente um livro (uma instância da classe Livro).
O sistema verifica se o objeto fornecido é de fato um livro válido.
Se for válido, o livro é adicionado à lista interna de livros da biblioteca.
O que esperar: O livro é registrado no sistema e fica disponível para busca e empréstimo.
Em caso de erro: Se você tentar adicionar algo que não seja um objeto Livro, o sistema informará com um erro.
4. Adicionar Usuário (adicionar_usuario)

Este método permite cadastrar um novo usuário no sistema da biblioteca.

Como funciona:
Você fornece um objeto que represente um usuário (uma instância da classe Usuario).
O sistema verifica se o objeto fornecido é de fato um usuário válido.
Se for válido, o usuário é adicionado à lista interna de usuários da biblioteca.
O que esperar: O usuário é registrado no sistema e pode agora interagir com os livros (emprestar/devolver).
Em caso de erro: Se você tentar adicionar algo que não seja um objeto Usuario, o sistema informará com um erro.
5. Buscar Livro (buscar_livro)

Este método permite encontrar livros no acervo da biblioteca com base no título ou autor.

Como funciona:
Você fornece um texto (uma string) como termo de busca.
O sistema percorre todos os livros registrados e verifica se o termo de busca aparece no título ou no nome do autor de cada livro (ignorando diferenças entre letras maiúsculas e minúsculas).
O que esperar: O método retorna uma lista contendo todos os livros que corresponderam ao termo de busca. Se nenhum livro for encontrado, a lista estará vazia.
Em caso de erro: Se o termo de busca não for um texto, o sistema informará com um erro.
6. Emprestar Livro (emprestar_livro)

Este método registra o empréstimo de um livro para um usuário.

Como funciona:
Você fornece o título do livro a ser emprestado e o email do usuário que está pegando o livro.
O sistema primeiro busca o livro pelo título fornecido.
Em seguida, busca o usuário pelo email fornecido.
Verifica se o livro está disponível (ou seja, se não está emprestado para outra pessoa).
Se o livro e o usuário forem encontrados e o livro estiver disponível:
O status do livro é atualizado para indicar que ele foi emprestado.
O livro é adicionado à lista de livros que o usuário tem emprestado.
Uma mensagem de confirmação é exibida.
O que esperar: O livro é marcado como emprestado e associado ao usuário.
Em caso de erro:
Se o título do livro ou o email do usuário não forem fornecidos como texto, o sistema informará com um erro.
Se o livro com o título especificado não for encontrado, o sistema informará que o livro não foi encontrado.
Se o usuário com o email especificado não for encontrado, o sistema informará que o usuário não foi encontrado.
Se o livro não estiver disponível (já estiver emprestado), o sistema informará que o livro não está disponível.
7. Devolver Livro (devolver_livro)

Este método registra a devolução de um livro por um usuário.

Como funciona:
Você fornece o título do livro a ser devolvido e o email do usuário que está devolvendo o livro.
O sistema busca o livro pelo título e o usuário pelo email.
Se o livro e o usuário forem encontrados:
O sistema tenta marcar o livro como disponível novamente.
O sistema tenta remover o livro da lista de livros que o usuário tem emprestado.
Uma mensagem de confirmação é exibida se a devolução for bem-sucedida.
O que esperar: O livro é marcado como disponível e removido da lista de livros do usuário.
Em caso de erro:
Se o título do livro ou o email do usuário não forem fornecidos como texto, o sistema informará com um erro.
Se o livro com o título especificado não for encontrado, o sistema informará que o livro não foi encontrado.
Se o usuário com o email especificado não for encontrado, o sistema informará que o usuário não foi encontrado.
Se o livro, por algum motivo, não puder ser devolvido (por exemplo, se a lógica interna da classe Livro ou Usuario impedir, o que é tratado pelo try...except no código), o sistema exibirá a mensagem de erro correspondente.
8. Relatório de Livros Emprestados (relatorio_livros_emprestados)

Este método gera uma lista de todos os livros que estão atualmente emprestados, indicando para qual usuário cada livro foi emprestado.

Como funciona:
O sistema percorre todos os usuários cadastrados.
Para cada usuário, ele verifica quais livros este usuário tem emprestado.
Ele coleta as informações relevantes (título do livro, autor, nome do usuário e email do usuário) para cada empréstimo ativo.
O que esperar: O método retorna uma lista onde cada item é um texto descrevendo um empréstimo ativo (por exemplo, "Livro: Título do Livro, Autor: Nome do Autor, Usuário: Nome do Usuário, Email: email@usuario.com"). Se nenhum livro estiver emprestado, a lista estará vazia.
Espero que esta documentação seja útil para o seu cliente! Lembre-se de incluir também a documentação das classes Livro e Usuario para uma visão completa do sistema.

Documentação das Classes de Livros (Livro, LivroFisico, LivroDigital)
---

Este documento descreve as classes responsáveis por representar os livros dentro do sistema da biblioteca. A classe principal é Livro, e existem variações (LivroFisico e LivroDigital) para representar diferentes tipos de livros.

1. Classe Principal: Livro

A classe Livro é o modelo básico para qualquer livro no sistema. Ela armazena as informações fundamentais sobre um livro e gerencia seu estado (se está disponível ou emprestado).

Informações Armazenadas:

Título: O nome do livro (texto).
Autor: O nome do autor do livro (texto).
Ano de Publicação: O ano em que o livro foi publicado (número inteiro).
Status: Indica se o livro está "disponível" (pronto para ser emprestado) ou "emprestado".
Como um Livro é Criado (Inicialização __init__):

Ao adicionar um novo livro, você precisa fornecer o Título, Autor e Ano de Publicação.
O sistema verifica se essas informações são válidas (por exemplo, se o ano de publicação não é no futuro).
Inicialmente, todo livro novo é criado com o Status definido como "disponível".
Como Ver as Informações do Livro (__str__ e __repr__):

O sistema pode gerar uma descrição simples do livro (Título, Autor, Ano e Status) sempre que for necessário mostrá-lo em formato de texto.
Emprestando um Livro (emprestar):

Este método é usado para mudar o Status de um livro de "disponível" para "emprestado".
Só é possível emprestar um livro se ele estiver atualmente "disponível".
Devolvendo um Livro (devolver):

Este método é usado para mudar o Status de um livro de "emprestado" para "disponível".
Só é possível devolver um livro se ele estiver atualmente "emprestado".
Gerenciamento do Status (Encapsulamento):

O código inclui uma forma de garantir que o Status de um livro só possa ser definido como "disponível" ou "emprestado", evitando que um livro fique com um estado inválido no sistema.
2. Tipos Específicos de Livros (Abstração e Herança)

O sistema foi projetado para lidar com diferentes tipos de livros (físicos e digitais), aproveitando as informações básicas da classe Livro e adicionando detalhes específicos para cada tipo.

LivroFisico:

Representa um livro que existe fisicamente na biblioteca.
Além das informações básicas de um Livro (Título, Autor, etc.), um LivroFisico armazena a Localização na Prateleira onde ele pode ser encontrado.
Quando as informações de um LivroFisico são mostradas, a localização na prateleira também é incluída.
LivroDigital:

Representa um livro que está disponível em formato digital.
Além das informações básicas de um Livro (Título, Autor, etc.), um LivroDigital armazena um Link de Download para acessar o arquivo.
Quando as informações de um LivroDigital são mostradas, o link de download também é incluído.
Em resumo, estas classes definem como os livros são representados, quais informações eles contêm e como seu estado de disponibilidade é gerenciado dentro do sistema da biblioteca. A estrutura com LivroFisico e LivroDigital permite flexibilidade para expandir o sistema e incluir outros tipos de materiais no futuro, se necessário.

Documentação das Classes de Usuários (Usuario, UsuarioRegular, UsuarioVIP)
---

Este documento descreve as classes responsáveis por representar os usuários que interagem com o sistema da biblioteca. A classe principal é Usuario, e existem variações (UsuarioRegular e UsuarioVIP) para representar diferentes tipos de usuários com regras específicas.

1. Classe Principal: Usuario

A classe Usuario é o modelo básico para qualquer pessoa que se cadastra no sistema da biblioteca. Ela armazena as informações de identificação do usuário e mantém um registro dos livros que ele pegou emprestado.

Informações Armazenadas:

Nome: O nome completo do usuário (texto).
Email: O endereço de email do usuário (texto). Este email é usado como um identificador único no sistema.
Livros Emprestados: Uma lista interna que guarda todos os livros que o usuário pegou emprestado no momento.
Como um Usuário é Criado (Inicialização __init__):

Ao cadastrar um novo usuário, você precisa fornecer o Nome e o Email.
O sistema verifica se o Nome e o Email são fornecidos como texto e se o Email parece ter um formato válido (contém '@' e '.').
Inicialmente, a lista de Livros Emprestados do novo usuário está vazia.
Como Ver as Informações do Usuário (__str__ e __repr__):

O sistema pode gerar uma descrição simples do usuário (Nome, Email e a quantidade de livros emprestados) sempre que for necessário mostrá-lo em formato de texto.
Pegando um Livro (pegar_livro):

Este método é usado para adicionar um livro à lista de Livros Emprestados do usuário.
Ele registra que o usuário agora possui este livro em seu poder.
Devolvendo um Livro (devolver_livro):

Este método é usado para remover um livro da lista de Livros Emprestados do usuário.
O sistema verifica se o livro que está sendo devolvido realmente consta na lista de livros que o usuário pegou emprestado.
2. Tipos Específicos de Usuários (Abstração e Herança)

O sistema permite definir diferentes categorias de usuários com regras ou privilégios distintos, usando as informações básicas da classe Usuario e adicionando funcionalidades específicas.

UsuarioRegular:

Representa um usuário padrão da biblioteca.
Define um limite máximo de livros que este tipo de usuário pode ter emprestado ao mesmo tempo (max_livros). Atualmente, este limite é 3.
Possui um método (pode_emprestar) para verificar se o usuário já atingiu seu limite de livros emprestados e, portanto, se ele ainda pode pegar mais livros.
UsuarioVIP:

Representa um usuário com privilégios especiais (por exemplo, um membro VIP).
Define um limite máximo de livros maior que o UsuarioRegular. Atualmente, este limite é 5.
Pode incluir outros benefícios específicos, como um prazo de devolução mais longo (mencionado no código como exemplo, prazo_devolucao).
Também possui um método (pode_emprestar) para verificar se o usuário VIP ainda pode pegar mais livros, baseado no seu limite maior.
Em resumo, estas classes definem como os usuários são representados no sistema, quais informações são armazenadas sobre eles e como os livros que pegam emprestado são registrados. A estrutura com UsuarioRegular e UsuarioVIP demonstra como o sistema pode gerenciar diferentes tipos de usuários com regras de empréstimo variadas.


Web Interface
---


Para facilitar o acesso e a interação com o sistema de gerenciamento da biblioteca, foi desenvolvida uma interface web que permite utilizá-lo através de um navegador (como Chrome, Firefox, Edge, etc.).

Essa interface foi construída utilizando o Flask, um framework leve e flexível para criar aplicações web em Python. O Flask atua como o "motor" que processa as requisições do usuário (como clicar em um botão ou preencher um formulário) e entrega as páginas web correspondentes para visualização no navegador.

A estrutura da interface web é organizada em arquivos HTML, onde cada arquivo tem uma responsabilidade específica:

O arquivo **base.html** serve como o modelo principal ou "esqueleto" de todas as páginas. Ele contém os elementos comuns (como cabeçalho, rodapé, menu de navegação) que se repetem em todo o site, garantindo que todas as telas tenham um visual consistente e uma navegação unificada.
Os demais arquivos HTML são as páginas específicas que cuidam da exibição de informações e da interação para cada parte do sistema:
1. index.html: A página inicial que serve como porta de entrada para a aplicação web.
2. livros.html: Exibe a lista completa dos livros cadastrados na biblioteca.
3. usuarios.html: Exibe a lista dos usuários cadastrados no sistema.
4. adicionar_livro.html: Contém o formulário para inserir os dados de um novo livro e adicioná-lo ao acervo.
5. adicionar_usuario.html: Contém o formulário para inserir os dados de um novo usuário e cadastrá-lo no sistema.
6. relatorio_emprestimos.html: Apresenta o relatório detalhado de todos os livros que estão atualmente emprestados e para quais usuários.
7. erro.html: Uma página genérica para informar ao usuário caso ocorra algum problema ou erro inesperado durante a navegação ou operação no sistema.


Essa organização permite que a interface seja intuitiva, fácil de usar e manter, separando claramente a lógica de exibição (HTML) do processamento (Flask/Python).


### Referências
---

- [Python Documentação](https://docs.python.org/pt-br/3/)
- [Flask 3.1.0](https://flask.palletsprojects.com/en/stable/installation/)


### Contribuições
---

- Wagner da Costa Oliveira 

### Autores
---

- Wagner da Costa Oliveira

### Licença
---

- [GNU General Public License (GPL)](https://www.gnu.org/licenses/gpl-3.0.html)