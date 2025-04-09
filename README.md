# Sejam muito bem-vindos ao repositório oficial do GE! 🚀  

Olá, caro aluno! Seja muito bem-vindo ao repositório oficial do nosso grupo de estudos: **Introdução à Manipulação de Planilhas e Estatística**.
Este será o nosso espaço central de colaboração, aprendizado e desenvolvimento, onde vamos compartilhar conhecimento, construir nosso projeto final e crescer juntos. 

**IMPORTANTE**: Cada membro terá sua própria **branch**, nomeada conforme o e-mail institucional, garantindo **organização e clareza** no desenvolvimento. Conto com todos para fazermos deste repositório um ambiente **produtivo e enriquecedor**.  

Que seja uma jornada incrível para todos nós! 🚀  

---

## 📚 Sumário

- [Boas-vindas](#-sejam-muito-bem-vindos-ao-repositório-oficial-do-ge-)
- [🌱 Estrutura do Repositório](#-estrutura-do-repositório)
- [📌 Padronização de Commits](#-padronização-de-commits)
- [📝 Checklist Inicial](#-checklist-inicial)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [🔗 Links Úteis](#-links-úteis)
- [🆘 Ajuda](#-Ajuda)

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
|-------------|--------------------------------------------------|----------------|
| ✨ **feat**     | Nova funcionalidade                              | `feat: adicionar botão de login` |
| 🐛 **fix**      | Correção de bug                                  | `fix: corrigir erro no carregamento da página` |
| 📝 **docs**     | Mudanças na documentação                         | `docs: atualizar README` |
| 💄 **style**    | Ajustes visuais ou de formatação                 | `style: ajustar identação` |
| ♻️ **refactor** | Refatoração sem alterar funcionalidade           | `refactor: otimizar função` |
| ⚡ **perf**     | Melhorias de performance                         | `perf: reduzir tempo de resposta` |
| ✅ **test**     | Adição/modificação de testes                     | `test: adicionar testes unitários` |
| 🔧 **chore**    | Tarefas de suporte que não afetam o produto final| `chore: atualizar dependências` |
| 🚀 **build**    | Ajustes no processo de build ou dependências     | `build: configurar Dockerfile` |
| 🔁 **revert**   | Reverter um commit anterior                      | `revert: desfazer mudança` |


**Dica:** Sempre utilize mensagens curtas e diretas, seguidas de uma breve descrição quando necessário.  
Exemplo de commit bem formatado:  
```bash
git commit -m "✨feat: implementar sistema de autenticação JWT" 
```

## 📝 Checklist Inicial  

Se você acabou de entrar no repositório, siga estes passos para começar:  

1. **Clonar o Repositório**  
   ```bash
   git clone https://github.com/4lbanes/GEIA-25.1.git
   cd GEIA-25.1
   ``` 
Para acessar sua branch e começar a contribuir, utilize:
```bash
  git checkout seuemaildaunifor
```

2. **Estruturação de Diretórios**
- 📁 build/<br>
  -📄requirements.txt<br>
  -📄venv.sh
- 📁 docs/
   - 📁 classes/
   - 📁 works/
- 📁 data/<br>
  -📁 processed/<br>
  -📁 raw/
- 📁 notebooks/<br>
  -📄into.ipynb<br>
- 📁 submissions/

- 📄 .gitignore
- 📄 README.md
  
**Explicação dos arquivos:**<br>
📁 build/
- requirements.txt: Lista todas as dependências necessárias para o projeto, garantindo que todos os pacotes essenciais sejam instalados corretamente.
- venv.sh: Script de automação responsável por criar e ativar o ambiente virtual do Python, além de instalar automaticamente as dependências definidas no requirements.txt.

- 📁 docs/
- classes: Pasta de documentação das aulas, aqui vai conter o conteúdo dado no dia, os slides e a presença do dia.
- works: Pasta de documentação dos entregáveis de cada nível, aqui vai conter a documentação de cada trabalho.

📁 data/
- 📁 processed: Armazena os dados já limpos, transformados ou tratados, prontos para análise, modelagem ou visualização.
- 📁 raw: Armazena os dados brutos, exatamente como foram obtidos de fontes externas (bases públicas, web scraping, APIs, etc).

📁 notebooks/
- intro.ipynb: Notebook introdutório explicando como utilizar o Jupyter Notebook, incluindo exemplos práticos para facilitar o uso da ferramenta.

📁 submissions/
- Pasta utilizada para as entregas dos trabalhos de acompanhamento.

📄 .gitignore: Define os arquivos e diretórios que devem ser ignorados pelo Git, evitando que arquivos desnecessários ou sensíveis sejam versionados.<br>
📄 README.md: Documento principal do repositório, contendo informações sobre o projeto, instruções de instalação, uso e contribuições.
  

3. **Instalação das Dependências**<br>
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

4.**Entrega dos Trabalhos**
Durante o grupo de estudos (GE), teremos alguns pequenos trabalhos com o objetivo de acompanhar o aprendizado de cada participante.

Cada integrante possui sua própria branch. Portanto, para cada novo entregável, basta criar uma pasta dentro do diretório `submissions/` com o seguinte padrão:

### 📌 Exemplo de nome da pasta:
📁<code>ent-1 (seu-nome)</code>

**IMPORTANTE:** Use seu primeiro nome ou nome identificável (sem espaços).

### 📁 Estrutura esperada:

📁 submissions/<br>
  - 📁ent-1 arthur/<br>
     - main.py
     - 📄README.md

### ✅ Regras:
- Os arquivos do projeto devem ser nomeados de forma clara e coerente com o conteúdo.
- Utilize extensões apropriadas (<code>.ipynb</code>, <code>.py</code>, <code>.md</code>, etc.).
- Sempre que possível, adicione um `README.md` dentro da sua pasta explicando brevemente o que foi feito.

Essa organização ajuda na revisão, no versionamento e na troca de conhecimento entre os membros do grupo.

## 🛠️ Tecnologias Utilizadas
**Este repositório utiliza as seguintes tecnologias e bibliotecas:**

| Categoria   | Tecnologia             |
|-------------|------------------------|
| Linguagem   | Python                 |
| Ferramentas | Jupyter Notebook       |
| Bibliotecas | pandas, numpy, matplotlib |


## 🔗 Links Úteis

- [Documentação Oficial do Git](https://git-scm.com/doc)
- [Curso gratuito de Git e GitHub (Rocketseat)](https://www.rocketseat.com.br/discover)
- [Documentação do Jupyter Notebook](https://jupyter.org/)
- [Documentação do pandas](https://pandas.pydata.org/docs/)


## 🆘 Ajuda

Problemas comuns e soluções:

❌ Erro ao ativar o ambiente virtual<br>
👉 Verifique se o Python 3.10+ está instalado com <code>python --version</code><br>
👉 Certifique-se de que você está no diretório raiz do projeto ao executar o comando de ativação<br>
👉 No Windows, execute o terminal como administrador, se necessário<br>

❌ Dependências não instaladas<br>
👉 Execute <code>pip install -r build/requirements.txt</code> manualmente<br>
👉 Verifique se o ambiente virtual está **ativado** antes de instalar as dependências<br>
👉 Tente atualizar o pip com <code>pip install --upgrade pip</code><br>

❌ Erro: <code>comando ‘bash’ não encontrado</code> (Windows)<br>
👉 O Windows **não** possui o interpretador bash nativo. Use o <code>Git Bash</code> ou o <code>WSL</code> (Windows Subsystem for Linux) para rodar o <code>venv.sh</code><br>
👉 Alternativamente, crie o ambiente manualmente:

```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r build/requirements.txt
```

❌ Erro ao abrir notebooks no Jupyter<br>
👉 Verifique se o Jupyter está instalado (<code>pip show notebook</code>)<br>
👉 Caso não esteja, instale com:

```bash
  pip install notebook
```
🧠 Está perdido(a)? Precisa de ajuda com Git, Python ou o projeto em geral?<br>
👉 Não hesite em abrir uma issue aqui no repositório ou chamar alguém no grupo do WhatsApp<br>

Toda dúvida é válida. Estamos aqui para aprender juntos!