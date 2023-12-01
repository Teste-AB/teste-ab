# Teste_AB

## Configuração do seu banco de dados
Entre no seu servidor mysql e execute o  seguinte comando

```
CREATE DATABASE <nome do banco>;
USE <nome do banco>;
```
ou apenas use o arquivo .sql que deixamos como base.

A seguir, um breve guia sobre como configurar e executar este projeto.

## Configuração do Ambiente Virtual (venv)

1. Abra um terminal na raiz do seu projeto.

2. Execute o seguinte comando para criar um ambiente virtual:

    ```bash
    python -m venv venv
    ```

    ou, se você estiver usando o Python 3.x:

    ```bash
    python3 -m venv venv
    ```

3. Ative o ambiente virtual:

    - No Windows:

        ```bash
        .\venv\Scripts\activate
        ```
    Você verá o nome do ambiente virtual no prompt do terminal, indicando que o ambiente virtual está ativo.

## Instalação das Dependências

Depois de ativar o ambiente virtual, você pode instalar as dependências do projeto a partir do arquivo `requirements.txt`. Certifique-se de que o ambiente virtual está ativo antes de prosseguir.

1. Execute o seguinte comando:

    ```bash
    pip install -r requirements.txt
    ```

    Isso instalará todas as dependências listadas no arquivo `requirements.txt`.

## Adaptanddo seu codigo
Para que o programa se conecte ao seu banco de dados faça a seguinte configuração nos dois arquivos .py:
```
config = {
    'user':'seu usuario',
    'password':'sua senha',
    'host':'localhost',
    'database':'seu banco  de dados',
    'raise_on_warnings': True
}
```

## Executando o Projeto

Agora que o ambiente virtual está configurado e as dependências estão instaladas, você pode executar o projeto. Certifique-se de estar com o ambiente virtual ativo.

1. Execute o seu script principal ou o comando necessário para iniciar o projeto.

    ```bash
    python magaiver.py
    ```
2. O projeto deve agora estar em execução.
   2.1 Faça o cadastro dos usuarios de acordo com as exigencias.
```bash
    python highlander.py
    ```
3 Entre no link gerado localmente e fique a vontade para fazer seus testes.

## Desativando o Ambiente Virtual

Quando você terminar de trabalhar no projeto, desative o ambiente virtual:

```bash
deactivate
