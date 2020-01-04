# Tag Filter
Aplicação para acompanhamento de tags do Twitter

## Desafio

* Cadastrar e remover hashtags que queremos acompanhar
* Coletar com frequência mensagens publicadas no Twitter contendo as hashtags (dentro do limite da API)
* Listar as mensagens coletadas mostrando: mensagem, autor, data de publicação
* Filtrar as mensagens listadas por hashtag

## Instalação

* Clone este repositório com o comando ```git clone https://github.com/VGasparini/tag-filter```
* Agora dentro da pasta criada, extraia o arquivo ```static.zip``` com o descompactador de sua preferência.
* Crie um ambiente virtual Python com o comando ```virtualenv venv```. Caso não possua ainda este utilitário, instale via ```python3 -m pip install virtualenv```
* Uma vez criado o ambiente virtual, ative-o através do comando ```source venv/bin/activate```
* Instale todas as dependências do projeto ```pip3 install -r requirements.txt```

## Configuração

* Para utilizar a aplicação é necessário criar um novo app para obter as credenciais de acesso a API. Para isso, acesse o link [Twitter Devolopers](https://developer.twitter.com/).
* Sob posse das credenciais do app, preencha o arquivo ```credentials.sample``` e renomeie para ```credentials.json```.
* Inicie o serviço através do comando ```python3 server.py```

## Testes

* Os testes automatizados foram desenvolvidos utilizando a biblioteca nativa [unittest](https://docs.python.org/3/library/unittest.html)
* Para realizar os testes execute o arquivo ```test.py```
* A rotina de testes verifica:
    * Se o servidor está funcional
    * Se a aplicação inicia sem nenhuma tag
    * Se a inserção de tag funciona
    * Se a inserção de uma tag duplicada é tratada
    * Se a removação da tag funciona

## Documentação auxiliar

* [Twitter API reference](https://developer.twitter.com/en/docs/api-reference-index)
* [Flask](https://www.palletsprojects.com/p/flask/)

## TODO list

### Back
* ~Conectar com a API do Twitter~
* ~Cria uma stream de dados~
* ~Filtrar tweets por um conjunto de hashtags~
* ~Formatar dados para o padrão: mensagem, autor, data de publicação~
* ~Separar rotinas~
* ~Preparar objetos para usar no front~

### Front
* ~Criar um site básico~
* ~Integrar campo de inserção de hashtags~
* ~Exibir mensagens filtradas~
* ~Interagir com filtros (remover)~

## Licença
[MIT](https://choosealicense.com/licenses/mit/)

> Projeto desenvolvido como parte do processo de seleção da [Magrathea Labs](https://www.magrathealabs.com/)
