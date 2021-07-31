# Escola de Inverno em Computação 2021 - LARCC
## Reprodução de Pesquisas com Docker

Os códigos e dados presentes nesse repositório servem como material de apoio para o módulo "Reprodução de Pesquisas com Docker" da Escola de Inverno em Computação realizada pelo [Laboratório de Pesquisas Avançadas para Computação em Nuvem](https://larcc.setrem.com.br/) em 2021. Mais informações em https://larcc.setrem.com.br/escola-de-inverno-2021/.

Os dados na pasta `data` são um dataset com dados sobre os times da série A do campeonato de futebol brasileiro (veja o README na pasta `data`).
O script `average-attendance.py` usa esses dados para gerar um gráfico de média de público por time, com filtro opcional por ano.
Modo de usar:

```bash
$ python average-attendance.py [<ano>]
```


### Usando imagem do Docker Hub

Para gerar o gráfico usando a imagem [`czentye/matplotlib-minimal`](https://hub.docker.com/r/czentye/matplotlib-minimal) do Docker Hub, use o comando (o argumento do ano é opcional):

```bash
$ docker container run -it --rm -v<pasta>:/home -w/home czentye/matplotlib-minimal python average-attendance.py <ano>
```
A `<pasta>` deve ser substituída pelo caminho completo para a pasta onde está o script (e este README).  
A flag `-it` faz com que as mensagens do script sejam apresentadas na saída do console.  
A flag `--rm` faz com que o container criado para essa execução seja removido assim que a execução termina.  
A flag `-v<pasta>:/home` permite que o container acesse os arquivos do diretório passado em `<pasta>` no caminho `/home` (dentro do container).  
A flag `-w/home` faz com que o container inicie a sua execução (_working directory_) na pasta `/home`.  
Por fim, após o nome da imagem, está o comando que deve ser executado dentro do container.

O script gera uma imagem em `png` com o mesmo nome do script e com o sufixo do ano dos dados que foram gerados, na pasta atual (`/home` do container, que é a pasta mapeada pela flag `-v`).


### Preparando imagem Docker com o script

Para gerar uma imagem Docker contendo os dados, o script, e já configurada para fazer a execução, basta executar o comando:

```bash
$ docker image build -t <imagem>:<tag> .
```
A `<imagem>` deve ser substituída pelo nome da imagem que será gerada.  
A `<tag>` deve ser substituída pela tag da imagem que será gerada. Caso deseje, pode remover os dois pontos e a `<tag>` e o Docker usará a tag padrão (`latest`).  
O `.` ao final do comando referencia a pasta atual, que é onde está o arquivo `Dockerfile` que será compilado para gerar a imagem. Opcionalmente, pode-se usar outro nome para o arquivo e especificar qual este nome através da flag `-f <nome>`
