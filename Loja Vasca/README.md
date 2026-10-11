# Loja Vasca

Projeto pessoal desenvolvido em Python para simular um sistema de gerenciamento de uma loja, com foco no desenvolvimento de lógica de programação, manipulação de dados, integração com banco de dados e organização de código.

O projeto está em desenvolvimento e será expandido gradualmente, incorporando funcionalidades de gestão comercial e análise de dados.

## Objetivos

- Praticar lógica de programação e modularização em Python.
- Implementar operações de cadastro, consulta e gerenciamento de produtos.
- Trabalhar com persistência de dados utilizando SQLite.
- Desenvolver uma estrutura que permita implementar o controle de estoque e o registro de vendas.
- Explorar análise de dados e previsão de vendas em etapas futuras.

## Tecnologias utilizadas

- **Python** — desenvolvimento da aplicação e implementação das regras de negócio.
- **SQLite** — armazenamento persistente dos dados.
- **SQL** — criação de tabelas, inserção e consulta de registros.

## Funcionalidades implementadas

- [x] Criação e estruturação do banco de dados.
- [x] Modelagem inicial das tabelas de produtos, vendedores, vendas e itens de venda.
- [x] Cadastro de produtos.
- [x] Listagem de produtos cadastrados.
- [x] Busca de produtos por ID.
- [x] Persistência dos produtos no banco de dados.

## Próximas etapas

- [ ] Alteração e remoção de produtos.
- [ ] Validação e tratamento de erros nas entradas.
- [ ] Controle de estoque.
- [ ] Cadastro e gerenciamento de vendedores.
- [ ] Registro de vendas com múltiplos produtos.
- [ ] Cálculo de descontos e comissões.
- [ ] Análise de dados com Pandas.
- [ ] Desenvolvimento de um modelo de Machine Learning para previsão de vendas.
- [ ] Evolução da arquitetura e desenvolvimento de uma interface para o sistema.

## Estrutura atual do projeto

```text
Loja-Vasca/
├── DataBase.py
├── Produtos.py
└── Loja_Vasca.db
```

- `DataBase.py`: configura a conexão com o SQLite e cria as tabelas do banco de dados.
- `Produtos.py`: implementa as operações de cadastro, listagem e busca de produtos, além do menu interativo.
- `Loja_Vasca.db`: banco de dados SQLite utilizado para armazenar as informações localmente.

## Como executar

1. Instale o Python 3.
2. Clone este repositório.
3. Acesse a pasta do projeto.
4. Execute o arquivo principal atual:

```bash
python Produtos.py
```

O banco de dados será criado ou reutilizado conforme a configuração de `DataBase.py`.

## Status do projeto

**Em desenvolvimento.**

A Loja Vasca está sendo construída por etapas, priorizando a compreensão da lógica, a modelagem dos dados e a evolução gradual da arquitetura.

## Autor

Vitor Vasca

- GitHub: [@vitorvasca-ux](https://github.com/vitorvasca-ux)
