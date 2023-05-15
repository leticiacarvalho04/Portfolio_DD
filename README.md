# Portfolio_DD
![](https://user-images.githubusercontent.com/110743347/226479544-f2f4afac-29d2-4368-beae-c41fa0aca80e.png)

Aluna: Letícia Helena <br>
Turma: 1° DSM <br>
Descrição: Portfólio da disciplina de Design Digital <br>


# Visualização do protótipo:
* Para visualizar o protótipo navegável, acesse o [Figma](https://www.figma.com/file/8IOS4u3CK5xcWMWnHQ2Zui/PORTF%C3%93LIO?node-id=62-30&t=pTVGe2MZknH7Tnv9-0)

* Para visualizar o protótipo estático (wireframe) acesse à pasta doc e ao pdf incluso nela

Avaliação ok

# Portfolio_DD
![](https://user-images.githubusercontent.com/110743347/226479544-f2f4afac-29d2-4368-beae-c41fa0aca80e.png)

Aluna: Letícia Helena <br>
Turma: 1° DSM <br>
Descrição: Portfólio da disciplina de Design Digital <br>


# Visualização do protótipo:
* Para visualizar o protótipo navegável, acesse o [Figma](https://www.figma.com/file/8IOS4u3CK5xcWMWnHQ2Zui/PORTF%C3%93LIO?node-id=62-30&t=pTVGe2MZknH7Tnv9-0)

* Para visualizar o protótipo estático (wireframe) acesse à pasta doc e ao pdf incluso nela

Avaliação ok

<h1>🚀 Passo a passo para executar o projeto</h1>

<h2>Baixando o repositório</h2>
<br>

<h3>🚨 Passo 1: configurar sua credencial</h3>
<br>

<p>1- Primeiramente é necessário criar seu Token. Para isso abra seu github, vá em "Settings" depois "Developer settings".</p>
<p>2- Clique em "Personal Access tokens" e depois "Tokens(classic)".</p>
<p>3- Vá em "Generete new token" e "Generete new token classic".</p>
<p>4- Coloque um nome em "Note" e um prazo de expiração (é recomendado 7 dias).</p>
<p>5- Selecione todas as caixinhas e depois clique em "Generete token". Em seguida você copia o seu Token e guarda-o em algum lugar (recomenda-se o email ou bloco de notas)</p>
<p>6- Em seguida, pesquise na barra de tarefas do windows "gerenciador de credenciais"</p>
<p>7- Clique em "credenciais do windows" e depois em "adicionar uma credencial genérica"</p>
<p>8- Em "endereço de rede ou internet" coloque:</p>
      
      git:https://github.com
      
<p>9- Em "nome de usuário" coloque o seu nome de usuário do github</p>
<p>10- Em senha coloque seu Token que você gerou e copiou</p>
<br>

<h3>📥 Passo 2: Clonar o repositório</h3>
<br>

*Caso você já tenha o git instalado no seu computador siga o passo a passo abaixo

<p>1- Crie na área de trabalho uma pasta</p>
<p>2- Digite "cmd" na barra de endereço da pasta</p>

<p>3- Para iniciar:</p>

    git init
    
<p>4- Para colocar sua branch na main:</p>

    git checkout -b main
    
<p>5- Para configurar o usuário:</p>

    git config --local user.name "SEU NOME"
    
<p>6- Para configurar seu E-mail:</p>

    git config --local user.email "seu@email.com"

<p>7- Digite os seguinte comandos no terminal para clonar:</p>

    git clone https://github.com/LeticiaHelena/Portfolio_DD.git

<br>

*Caso você não tenha o git em seu computador execute este passo a passo antes do anterior 

<p>1- Clique no link abaixo para instalar o git: </p>

    https://git-scm.com/downloads

<p>2- Selecione o sistema do seu computador (Linux, Windows ou Mac) para fazer o download</p>
<p>3- Selecione a opção que condiz com a quantidade de bits do seu computador</p>
<p>4- Após a instalação basta seguir o passo a passo acima 🔝</p>

<br>
    
<h2>🛠 Executando o site</h2>
<br>

<h3>💻 Criando o ambiente virtual</h3>
<br>

<p>1 - Abra a pasta "src" do repositório clonado pelo VS code</p>


<p>2 - Clique em "terminal" e para criar um ambiente virtual:</p>

      python -m venv env
      
<p>3 - Para baixar todos os arquivos que precisamos para rodar com o arquivo Requirements:</p>

      pip install -r requirements.txt

<p>4 - Por ultimo para a aplicação rodar digite:</p>

      flask run
      
<p>5- Para ver o site rodando basta segurar a tecla "Ctrl" do seu teclado e clicar no link</p>