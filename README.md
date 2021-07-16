# Escola de Inverno em Computação 2021 - LARCC
## Reprodução de Pesquisas com Docker

Os códigos e dados presentes nesse repositório servem como material de apoio para o módulo "Reprodução de Pesquisas com Docker" da Escola de Inverno em Computação realizada pelo [Laboratório de Pesquisas Avançadas para Computação em Nuvem](https://larcc.setrem.com.br/) em 2021. Mais informações em https://larcc.setrem.com.br/escola-de-inverno-2021/.


### Comandos

Para gerar o gráfico de média de público por time (`average-attendance`), use o comando (o argumento do ano é opcional):

```bash
$ docker run --rm -v<pasta>:/home -w/home czentye/matplotlib-minimal:3.1.2 python average-attendance.py <ano>
```

O script gera uma imagem em `png` com o mesmo nome do script e com o sufixo do ano dos dados que foram gerados, na pasta atual.
