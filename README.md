# Tag Filter

Aplicação para acompanhamento de tags do Twitter

![](https://github.com/VGasparini/tagfilter/blob/master/tagfilter.gif)

> Projeto desenvolvido como parte da avaliação para a disciplina de Engenharia de Software

## Escopo

- Cadastrar e remover hashtags
- Coletar com frequência mensagens publicadas no Twitter contendo as hashtags (dentro do limite da API)
- Listar as mensagens coletadas mostrando: mensagem, autor, data de publicação
- Filtrar as mensagens listadas por hashtag

## Instalação

- Clone este repositório com o comando `git clone https://github.com/VGasparini/tag-filter`
- Agora dentro da pasta criada, extraia o arquivo `static.zip` com o descompactador de sua preferência.
- Crie um ambiente virtual Python com o comando `virtualenv venv`. Caso não possua ainda este utilitário, instale via `python3 -m pip install virtualenv`
- Uma vez criado o ambiente virtual, ative-o através do comando `source venv/bin/activate`
- Instale todas as dependências do projeto `pip3 install -r requirements.txt`

## Configuração

- Para utilizar a aplicação é necessário criar um novo app para obter as credenciais de acesso a API. Para isso, acesse o link [Twitter Devolopers](https://developer.twitter.com/).
- Sob posse das credenciais do app, preencha o arquivo `credentials.sample` e renomeie para `credentials.json`.
- Inicie o serviço através do comando `python3 server.py`

## Testes

- Os testes automatizados foram desenvolvidos utilizando a biblioteca nativa [unittest](https://docs.python.org/3/library/unittest.html)
- Para realizar os testes execute `python3 test.py -v`
- A rotina de testes verifica:
  - Se o servidor está funcional
  - Se a aplicação inicia sem nenhuma tag
  - Se a inserção de tag funciona
  - Se a inserção de uma tag duplicada é tratada
  - Se a removação da tag funciona

## Deploy

- A aplicação está disponivel para uso no endereço [http://tagfilter.herokuapp.com/](http://tagfilter.herokuapp.com/)
- Está sendo utilizado o plano gratuito da plataforma de cloud [Heroku](https://dashboard.heroku.com/)

## Documentação auxiliar

- [Twitter API reference](https://developer.twitter.com/en/docs/api-reference-index)
- [Flask](https://www.palletsprojects.com/p/flask/)

## Code formatting

Foi utilizado a ferramenta [Black](https://black.readthedocs.io/en/stable/) para a formatação do código.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
