# Bot-que-baixa-arquivos
***

## Descrição:

Neste projeto, o nosso bot vai navegar até um site de vídeos e baixar um arquivo padrão. Esse projeto simula a situação onde você precisa ficar acessando o mesmo site e baixando o mesmo arquivo.


Esse é o [site](https://file-examples.com/) de onde vamos baixar o arquivo.
***

## Requisitos:

**OBS: AUTOMAÇÕES COM PYAUTOGUI, A BIBLIOTECA QUE USAMOS PARA DESENVOLVER ESSE PROJETO, PRECISAM DESENVOLVIDAS, PREFERENCIALMENTE, NO COMPUTADOR ONDE ELAS SERÃO EXECUTADAS, VISTO QUE A BIBLIOTECA UTILIZA A LOCALIZAÇÃO DOS ELEMENTOS NA SUA TELA. PORTANTO, NÃO HÁ GARANTIAS QUE A AUTOMAÇÃO FUNCIONARÁ NO SEU COMPUTADOR, MAS SE SEGUIR OS REQUISITOS, É POSSÍVEL QUE ELA FUNCIONE SEM A NECESSIDADE DE ALTERAÇÕES NO PROJETO OU MESMO QUE NÃO FUNCIONE, COM POUCAS ALTERAÇÕES NO CÓDIGO FONTE, O PROJETO FUNCIONARÁ.**

* Ter a resolução de tela ajustada em: **1366 x 768**.

* O sistema operacional do computador deve ser o **Windows 10** ou **Windows 11**. 

* Ter o Python 3 instalado no seu computador. 

* Ter habilitado a opção  **Add to Path** na instalação do Python.

* Possuir o navegador **Google Chrome** instalado.

* Deixar habilitada, a janela de inicialização do **Chrome**. 
**OBS: VOCÊ SABE QUE A JANELA DE INICIALIZAÇÃO DO GOOGLE CHROME ESTÁ HABILITADA, SE QUANDO VOCÊ CLICA PARA ABRIR O NAVEGADOR, A TELA NA IMAGEM ABAIXO É MOSTRADA.**

*Imagem de exemplo que mostra a janela de inicialização do Google Chrome:*

![Imagem que mostra uma janela de inicialização no Google Chrome](https://ravel.com.br/blog/wp-content/uploads/2021/12/image-11.png)


***


## Como rodar o projeto?

Assim que clonar este projeto, sugiro que você crie um ambiente virtual isolando os arquivos do seu computador dos arquivos do projeto em si.

#### Criando ambiente virtual com Python:

1. Clone o projeto.

2. Estando dentro da pasta do projeto, abra o seu terminal.

RODE O COMANDO ABAIXO E AGUARDE A CRIAÇÃO:

```
python -m venv nome_do_ambiente_virtual
```

**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.


3. Ative o ambiente virtual através do seu terminal:

RODE:
```
nome_do_ambiente_virtual\Scripts\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

Feito isso, vamos instalar as bibliotecas necessárias através do arquivo requirements.txt.

***

#### Instalando bibliotecas necessárias:

Estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:

```
pip install -r requirements.txt
```

Pronto! Você está apto para rodar o projeto.

***

### Gerando executável:

**OBS: PARA GERAR O EXECUTÁVEL VOCÊ PRECISA BAIXAR O CONTEÚDO DO ARQUIVO requirements.txt. COMO FAZER ISSO FOI EXPLICADO ACIMA.**

Caso você queira um executável do projeto. Você deve ter executado as etapas anteriores. - ATÉ A PARTE DE INSTALAR AS BIBLIOTECAS DO ARQUIVO requirements.txt.

Feito isso, você deve estar com o seu ambiente virtual ativado e abrir o seu terminal na pasta raiz do projeto.

Estando lá, digite o seguinte comando:

```
python setup.py build
```

Uma pasta **build**, com um arquivo **app.exe** deve ser gerada.
O ARQUIVO **app.exe** será o seu executável.

***

## Arquivos:

* **requirements.txt** - Arquivo que contém as bibliotecas necessárias para rodar o programa.
* **app.py** - Arquivo principal que contém a lógica de inicialização do bot.
* **automacao_site.py** - Contém as funções que interagem com seu mouse e teclado. Além de toda lógica para abrir o navegador e baixa o arquivo de vídeo.
* **interface.py** - Contém a lógica da interface gráfica usada para interagir com o usuário.
* **setup.py** - Arquivo contém a lógica para geração de executável.
* **video.ico** - Ícone que é utilizado como imagem do executável.
* **fechar-propaganda.png** - Imagem utilizada para reconhecer uma anúncio e passar por ele.
* **maximizar-janela.png** - Imagem utilizada para reconhecer se a janela do navegador está maximizada ou não.

