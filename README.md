# kabum-api

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a6fea9090e5d42128bf33002fcba3766)](https://www.codacy.com/gh/leandrocorreasantos/kabum-api/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=leandrocorreasantos/kabum-api&amp;utm_campaign=Badge_Grade)

API para cálculo de frete desenvolvido para **KaBuM**.

## Instalação

O sistema foi desenvolvido utilizando **Docker**, onde os comandos para sua execução
foram colocados em um arquivo **Makefile**, sendo assim os únicos
requisitos obrigatórios para a execução do sistema em ambiente de testes são:
- Docker
- make


Verifique se o comando **make** e o ambiente **docker**, juntamente com o utilitário
**docker-compose** estão instalados em sua máquina antes de prosseguir.


Para o ambiente de produção, é necessário substituir os valores das variáveis
que constam no arquivo *.env.sample* para os valores corretos no ambiente em que
ele será executado.


Na primeira execução, o arquivo *.env.sample* será utilizado para gerar o arquivo
*.env*, que será utilizado pelo sistema.


## Inicializando o Sistema

Para inicializar a aplicação em sua máquina, basta utilizar o comando
**make build**. Ele inicializará os containers docker necessários.

```bash
make build
```

Em seguida, utilizamos o comando **make setup**, que cria o arquivo *.env* da
aplicação e instala as dependências listadas no arquivo *requirements.txt* e
*requirements-local.txt*, sendo este segundo um conjunto de ferramentas para
a realização de testes.

```bash
make setup
```

Após o término das instalações, utilize o comando **make start** para inicializar
a API. Os seguintes endpoints estarão disponíveis:

- **/v1/frete**: Responsável pelo cálculo do frete a partir dos dados referentes
ao tamanho e peso do pacote a ser transportado. O cálculo é feito através da
função **calcula_frete**, localizada no arquivo */api/utils.py*.

- **/apidocs**: contém a documentação produzida pelo utilitário **flasgger**, que
baseia-se em swagger para a produção da mesma.

```bash
make start
```

Por padrão, a API estará disponível no endereço
[http://localhost:5001](http://localhost:5001).

A documentação pode ser acessada através do endpoint [http://localhost:5001/apidocs](http://localhost:5001/apidocs).

O endpoint **/v1/frete** pode ser testado através do endpoint **/apidocs**, bastando
preencher o corpo da requisição com os dados necessários e clicando no botão
**executar**. Segue abaixo um exemplo de informação válida a ser enviada:

```json
{
    "dimensao":
    {
        "largura": 30,
        "altura": 30
    },
    "peso": 400
}
```

Para interromper a execução, utilize o atalho **Ctrl + C**.

## Testes

Para realizar os testes unitários, utiliza-se o comando **make test**. Ele executa
testes unitários através do utilitário **pytest**. As funções de testes da
aplicação encontram-se na pasta **/tests** e verificam se as regras de negócio
estão sendo cumpridas pela aplicação.

```bash
make test
```

## Validação do Código

Para a validação, utiliza-se o **flake8**, que realiza validações a fim de melhorar
a legibilidade e o desempenho da aplicação, reduzindo custos de operação e
manutenção do código.

```bash
make flake8
```
