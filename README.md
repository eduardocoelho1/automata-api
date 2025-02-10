# Trabalho Prático: Construção de uma API REST Utilizando a Biblioteca Automata
Este projeto permite criar, ver informações, visualizar e verificar a aceitação de palavras em três tipos de autômatos: DFA (Deterministic Finite Automaton), DPDA (Deterministic Pushdown Automaton) e DTM (Deterministic Turing Machine). 

## Configuração do ambiente
- Crie um ambiente virtual.
- Instale as dependências a seguir:
```
pip install "fastapi[standard]" automata-lib pygraphviz coloraide
```
Caso tenha dificuldade em instalar a biblioteca `pygraphviz`, obtenha mais informações em https://pygraphviz.github.io/documentation/stable/install.html.

## Como executar
- Na raiz do diretório, use o comando `fastapi run`.
- Use `ctrl+c` para parar a execução.

## Documentação
A documentação da API pode ser encontrada em http://127.0.0.1:8000/docs.

## Exemplos
No diretório `/examples` existe um exemplo para cada tipo de autômato.

- `dfa.json` representa um DFA que aceita palavras formadas por 0's e 1's terminadas em um número ímpar de 1's
- `dpda.json` representa um DPDA que aceita palavras da linguagem $L = \\{a^ib^i \mid i > 0\\}$
- `dtm.json` representa uma DTM que aceita palavras da linguagem $L = \\{a^ib^i \mid i > 0\\}$

## Testes
### Testando entradas para o autômato gerado por `dfa.json`:
- `01101` => `accepted`
- `100000111` => `accepted`
- `000011` => `rejected`
- `1111` => `rejected`

### Testando entradas para o autômato gerado por `dpda.json`:
- `ab` => `accepted`
- `aaaaabbbbb` => `accepted`
- `aaaaabbb` => `rejected`
- `bbbaaa` => `rejected`

### Testando entradas para o autômato gerado por `dtm.json`:
- `00000001111111` => `accepted`
- `00001111` => `accepted`
- `000011` => `rejected`
- `0101010101` => `rejected`

## Front-end
Pode-se acessar a página inicial do front-end em http://127.0.0.1:8000/static/index.html.

## Limitações e pressupostos
- A biblioteca `automata` não possui um método para visualizar máquinas de Turing, então não foi possível implementar a funcionalidade de visualização para DTM.
- O armazenamento dos autômatos é feito em memória, então não possuem armazenamento permanente.
- Apenas um autômato de cada tipo pode ser armazenado por vez.