# Boas vindas ao repositório do projeto Job Insights!

Este repositório comtém um projeto desenvolvido enquanto estudante da Trybe.

---

## Sumário

- [Sumário](#sumário)
- [Habilidades](#habilidades)
- [O que foi desenvolvido](#o-que-foi-desenvolvido)
- [Estrutura](#estrutura)
- [Instruções para entregar seu projeto](#instruções-para-entregar-seu-projeto)
  - [Data de Entrega](#data-de-entrega)
  - [Para executar os scripts](#para-executar-os-scripts)
    - [Linter](#linter)
    - [Testes](#testes)
  - [Requisitos](#requisitos)
    - [1 - Implemente a função `read`](#1---implemente-a-função-read)
    - [2 - Implemente a função `get_unique_job_types`](#2---implemente-a-função-get_unique_job_types)
    - [3 - Implemente a função `get_unique_industries`](#3---implemente-a-função-get_unique_industries)
    - [4 - Implemente a função `get_max_salary`](#4---implemente-a-função-get_max_salary)
    - [5 - Implemente a função `get_min_salary`](#5---implemente-a-função-get_min_salary)
    - [6 - Implemente a função `filter_by_job_type`](#6---implemente-a-função-filter_by_job_type)
    - [7 - Implemente a função `filter_by_industry`](#7---implemente-a-função-filter_by_industry)
    - [8 - Implemente a função `matches_salary_range`](#8---implemente-a-função-matches_salary_range)
    - [9 - Implemente a função `filter_by_salary_range`](#9---implemente-a-função-filter_by_salary_range)
    - [10 - Implemente um teste para a função `sort_by`](#10---implemente-um-teste-para-a-função-sort_by)
    - [11 - Implemente a página de um job](#11---implemente-a-página-de-um-job)

---

## Habilidades

- Utilizar o terminal interativo do Python.
- Utilizar estruturas condicionais e de repetição.
- Utilizar funções built-in do Python.
- Utilizar tratamento de exceções.
- Realizar a manipulação de arquivos.
- Escrever funções.
- Escrever testes com Pytest.
- Escrever seus próprios módulos e importá-los em outros códigos.

---

### O que foi desenvolvido

Neste projeto você implementou análises a partir de um conjunto de dados sobre empregos. Suas implementações serão incorporadas a um aplicativo Web desenvolvido com Flask. Também foram escritos testes para a implementação de uma análise de dados. Por fim, foi escrita uma rota e view para um recurso novo usando Flask!

Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

---

### Estrutura

Estrutura de diretórios e arquivos:

```
.
├── README.md
├── dev-requirements.txt
├── requirements.txt
├── src
│   ├── app.py
│   ├── insights.py
│   ├── jobs.csv
│   ├── jobs.py
│   ├── more_insights.py
│   ├── routes_and_views.py
│   ├── sorting.py
│   └── templates
│       ├── base.jinja2
│       ├── includes
│       │   └── nav.jinja2
│       ├── index.jinja2
│       ├── job.jinja2
│       └── list_jobs.jinja2
├── tests
│   ├── __init__.py
│   ├── mocks  (PASTA EXCLUIDA POR CONTER CONTEÚDO COM DIREITOS AUTORAIS)
│   │   ├── job_1.html
│   │   ├── jobs.csv
│   │   ├── jobs_with_industries.csv
│   │   ├── jobs_with_salaries.csv
│   │   └── jobs_with_types.csv
│   ├── sorting
│   │   ├── conftest.py            (ARQUIVO EXCLUIDO POR CONTER CONTEÚDO COM DIREITOS AUTORAIS)
│   │   ├── mocks.py               (ARQUIVO EXCLUIDO POR CONTER CONTEÚDO COM DIREITOS AUTORAIS)
│   │   └── test_sorting.py
│   ├── test_flask_app.py          (PASTA EXCLUIDA POR CONTER CONTEÚDO COM DIREITOS AUTORAIS)
│   ├── test_insights.py           (PASTA EXCLUIDA POR CONTER CONTEÚDO COM DIREITOS AUTORAIS)
│   ├── test_jobs.py               (PASTA EXCLUIDA POR CONTER CONTEÚDO COM DIREITOS AUTORAIS)
│   ├── test_more_insights.py      (PASTA EXCLUIDA POR CONTER CONTEÚDO COM DIREITOS AUTORAIS)
│   └── test_routes_and_views.py   (PASTA EXCLUIDA POR CONTER CONTEÚDO COM DIREITOS AUTORAIS)
```

### Data de Entrega

- Data de entrega do projeto: `30/03/2022`.

---

### Para executar os scripts

1. Clone o repositório

2. Crie o ambiente virtual para o projeto

- `python3 -m venv .venv && source .venv/bin/activate`

3. Instale as dependências

- `python3 -m pip install -r dev-requirements.txt`

---

#### Linter

Para verificar a qualidade do código, utilizamos neste projeto o linter `Flake8`.
Para rodá-lo localmente no projeto, execute o comandos abaixo:

```bash
python3 -m flake8
```

---

#### Testes

Para executar os testes certifique-se de que os seguintes passos foram realizados;

1. **criar o ambiente virtual**

```bash
$ python3 -m venv .venv
```

2. **ativar o ambiente virtual**

```bash
$ source .venv/bin/activate
```

3. **instalar as dependências no ambiente virtual**

```bash
$ python3 -m pip install -r dev-requirements.txt
```

Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

Com esta preparação feita, podemos executar os testes:

**Executar os testes**

```bash
$ python3 -m pytest
```

O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso queira explicitamente uma saída completa, o comando é:

```bash
python3 -m pytest -s -vv
```

Caso precise executar apenas um arquivo de testes basta executar o comando:

```bash
python3 -m pytest tests/nomedoarquivo.py
```

Caso precise executar apenas uma função de testes basta executar o comando:

```bash
python3 -m pytest -k nome_da_func_de_tests
```

Além dos testes com o Pytest, você pode (e vai ser bem bacana) rodar a aplicação flask para visualizar no navegador o resultado do desenvolvimento das funções.
Para isso, digite o comando `flask run`, e acesse o site gerado pelo Flask em `http://localhost:5000`. No começo do desenvolvimento, você verá que muitas coisas não funcionam, mas conforme você for implementando os requisitos, perceberá que a aplicação web começa a utilizar suas implementações e passa a ganhar vida.

---

## Requisitos

### 1 - Implemente a função `read`
local: `src/jobs.py`

Para começarmos a processar os dados, devemos antes carregá-los em nossa aplicação. Esta função será responsável por abrir o arquivo CSV e retornar os dados no formato de uma lista de dicionários.

### 2 - Implemente a função `get_unique_job_types`
local: `src/insights.py`

Agora que temos como carregar os dados, podemos começar a extrair informação deles. Primeiro, vamos identificar quais tipos de empregos existem.

### 3 - Implemente a função `get_unique_industries`
local: `src/insights.py`

Da mesma forma, agora iremos identificar quais indústrias estão representadas nesse conjunto de dados.

### 4 - Implemente a função `get_max_salary`
local: `src/insights.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o maior valor de todas as faixas.

### 5 - Implemente a função `get_min_salary`
local: `src/insights.py`

Os dados apresentam faixas salariais para cada emprego exibido. Vamos agora encontrar o maior valor de todas as faixas.

### 6 - Implemente a função `filter_by_job_type`
local: `src/insights.py`

Os empregos estão listados em um aplicativo web. Para permitir que a pessoa usuária possa filtrar os empregos por tipo de emprego, vamos precisar implementar esse filtro.

### 7 - Implemente a função `filter_by_industry`
local: `src/insights.py`

Do mesmo modo, o aplicativo precisa permitir uma filtragem por indústria. Vamos precisar implementar esse filtro também.

### 8 - Implemente a função `matches_salary_range`
local: `src/insights.py`

O aplicativo vai precisar filtrar os empregos por salário também. Como uma função auxiliar, implemente `matches_salary_range` para conferir que o salário procurado está dentro da faixa salarial daquele emprego. Vamos aproveitar também para conferir se a faixa salarial faz sentido -- isto é, se o valor mínimo é menor que o valor máximo.

### 9 - Implemente a função `filter_by_salary_range`
local: `src/insights.py`

Agora vamos implementar o filtro propriamente dito. Para esta filtragem, podemos usar a função auxiliar implementada no requisito anterior -- tomando o cuidado de descartar os empregos que apresentarem faixas salariais inválidas.

### 10 - Implemente um teste para a função `sort_by`
local: `tests/sorting/test_sorting.py`

Por fim, espera-se que a pessoa usuária possa escolher um critério de ordenação para exibir os empregos. Já temos uma implementação para essa ordenação em `src/sorting.py`, mas queremos ter certeza de que ela funciona e, principalmente, que não deixará de funcionar conforme vamos implementando novos recursos. Precisamos então escrever um *teste*!

Esse teste deve se chamar `test_sort_by_criteria` e garantir que a função funciona segundo esta especificação:

- A função `sort_by` recebe dois parâmetros:
  - `jobs` uma lista de dicionários com os detalhes de cada emprego;
  - `criteria` uma string com uma chave para ser usada como critério de ordenação.
- O parâmetro `criteria` deve ter um destes valores: `min_salary`, `max_salary`, `date_posted`
- A ordenação para `min_salary` deve ser crescente, mas para `max_salary` ou `date_posted` devem ser decrescentes.
- Os empregos que não apresentarem um valor válido no campo escolhido para ordenação devem aparecer no final da lista.

### 11 - Implemente a página de um job
local: `src/routes_and_views.py`

Para fechar com chave de ouro, que tal testar o quanto você aprendeu de Flask apenas vendo como fizemos as páginas de `index` e de `jobs`, e tentar criar uma página que irá exibir todas as informações de um job em específico?

- A função deve ser decorada com a rota `/job/<index>`.
- A função deve receber um parâmetro `index`.
- A função deve chamar a `read` para ter uma lista com todos os jobs.
- A função deve chamar a `get_job`, declarada no arquivo `src/more_insights.py`, para selecionar um job específico pelo `index`.
- A função deve renderizar o template `job.jinja2`, passando um parâmetro `job` contendo o job retornado pela `get_job`.
