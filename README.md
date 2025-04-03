# Sejam muito bem-vindos ao repositório oficial do GE! 🚀  

Olá caro aluno, seja muito bem vindo ao nosso repositório do grupo de estudo de **Introdução a Manipulações de Planilhas e Estatístisca**, Este será o nosso espaço central para **colaboração, aprendizado e desenvolvimento** dentro do grupo de estudos. Aqui, vamos compartilhar conhecimento, construir o projeto final e crescer juntos!  

**IMPORTANTE**: Cada membro terá sua própria **branch**, nomeada conforme o e-mail institucional, garantindo **organização e clareza** no desenvolvimento. Conto com todos para fazermos deste repositório um ambiente **produtivo e enriquecedor**.  

Que seja uma jornada incrível para todos nós! 🚀  

---

## 🌱 Estrutura do Repositório  

- **Branch individual**: Cada participante trabalhará em sua própria branch, seguindo o padrão:  
  ```bash
  git checkout seuemaildaunifor
  ```
- **Branch principal (main)**: Contém a versão oficial e consolidada do projeto.

- **Commits organizados:** É essencial manter boas práticas ao nomear commits e descrever alterações, garantindo um histórico claro e bem documentado.
### 📌 Padronização de Commits  

Manter um padrão nos commits é essencial para um histórico claro e bem organizado. Abaixo está uma tabela com os principais tipos de commits e seus significados:  

| Tipo        | Significado                                      | Exemplo de Uso |
|------------|------------------------------------------------|----------------|
| **feat**   | Adição de uma nova funcionalidade              | `feat: adicionar botão de login` |
| **fix**    | Correção de um bug                             | `fix: corrigir erro no carregamento da página` |
| **docs**   | Alterações na documentação                     | `docs: atualizar README com instruções de setup` |
| **style**  | Mudanças de formatação (espaços, indentação)   | `style: ajustar identação no arquivo main.py` |
| **refactor** | Refatoração de código sem mudança de comportamento | `refactor: otimizar função de busca` |
| **perf**   | Melhorias de performance                       | `perf: reduzir tempo de resposta da API` |
| **test**   | Adição ou modificação de testes                | `test: adicionar testes unitários para validação de login` |
| **chore**  | Tarefas auxiliares que não afetam o código-fonte | `chore: atualizar dependências do projeto` |
| **ci**     | Alterações em configurações de integração contínua | `ci: ajustar pipeline do GitHub Actions` |
| **build**  | Mudanças que afetam o processo de build ou dependências externas | `build: atualizar versão do Node.js no projeto` |
| **revert** | Reversão de um commit                          | `revert: desfazer commit anterior que causava erro` |

**Dica:** Sempre utilize mensagens curtas e diretas, seguidas de uma breve descrição quando necessário.  
Exemplo de commit bem formatado:  
```bash
git commit -m "feat: implementar sistema de autenticação JWT" 
```

## 📝 Checklist Inicial  

Se você acabou de entrar no repositório, siga estes passos para começar:  

1. **Clonar o repositório**  
   ```bash
   git clonehttps://github.com/4lbanes/GEIA-25.1.git
   cd <nome-do-repositorio>
    
Para acessar sua branch e começar a contribuir, utilize:
```bash
  git checkout seuemaildaunifor
```

2. **Instalar as Dependências**<br>
Para configurar o ambiente e instalar as bibliotecas necessárias, basta rodar os seguintes comandos no terminal:  
```bash
  cd build
```
Esse comando entra na pasta <code>build</code> do projeto, nessa pasta existe o arquivo de dependências(<code>requirements.txt</code>) e um arquivo de instalação(<code>venv.sh</code>). Dentro da pasta, digite o comando:
```bash
  bash venv.sh
```
Este script criará e ativará um ambiente virtual na raíz do projeto, além de instalar as dependências essenciais do projeto:

<code>numpy</code> → Operações matemáticas e vetoriais

<code>pandas</code> → Manipulação e análise de dados

Se, após rodar o script, o seu terminal não exibir algo semelhante a <code>(.venv)</code>, significa que o ambiente virtual não foi ativado corretamente. Para ativá-lo manualmente, utilize o comando correspondente ao seu sistema operacional:

| Sistema Operacional | Comando para ativação do Ambiente Virtual|        
|------------|------------------------------------------------|
| **Linux/MacOS**   | <code>source .venv/bin/activate</code>|
| **Windows (CMD)**    | <code>.venv\Scripts\activate.bat</code>| 
| **Windows (PowerShell)**   | <code>.venv\Scripts\activate.ps1</code>|


## 🛠️ Tecnologias Utilizadas
**Este repositório utiliza as seguintes tecnologias e bibliotecas:**

**Linguagem:** Python

**Ferramentas:** Jupyter Notebook

**Bibliotecas:**

pandas → Manipulação e análise de dados.

numpy → Cálculo numérico e operações vetoriais.

matplotlib → Visualização de dados.

Sejam bem-vindos! Um ótimo semestre a todos, contem comigo para tirar as suas dúvidas e bora codar! 🚀