# Trabalho Final - ELC1035 - 2019/1

O trabalho final consiste em um projeto individual proposto pelo aluno dentro do contexto desta disciplina.

## Descrição

Aplicação Web integrada à um bot no Telegram. Ela deverá permitir a criação e remoção de playlists, a busca de filmes existentes no The Movie Database (TMDb), adição e remoção deles numa playlist e visualização de cada um através de seu título, pôster e outras informações. Ao selecionar um filme tem-se acesso à página do filme no IMDB. E por fim, compartilhar a playlist com todos os usuários inscritos pelo Telegram.

## Instruções

No nível do arquivo [manage.py](manage.py), use os seguintes comandos para executar a aplicação web:
- sudo apt-get install python3-venv
- python3 -m venv venv
- source ./venv/bin/activate
- pip install -r requirements.pip
- python manage.py migrate
- python manage.py runserver

Em outro terminal mas no mesmo nível, use o seguinte comando para deixar o bot do Telegram rodando:
- python3 bot.py

## BOT

- /start: Boas vindas e instruções de uso do bot.
- /help: Instruções de uso do bot.
- /subscribe: Se inscrever para receber playlists de outros usuários.
- /unsubscribe: Cancelar a inscrição para parar de receber playlists.

## Referências

- [TMDb](https://www.themoviedb.org/?language=pt-BR)
- [Telepot API](https://github.com/nickoala/telepot)