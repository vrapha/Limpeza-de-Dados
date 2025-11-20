# Projeto 01 — Limpeza e Exploração de Dados (Data Cleaning)

Este projeto foi criado para praticar os fundamentos de limpeza e análise inicial de dados.  
A ideia é trabalhar com um arquivo CSV simples, identificar problemas comuns e aplicar técnicas básicas para organizar e preparar os dados para análise.

---

##  Arquivos do projeto

- **sales.csv** → dados brutos
- **analysis.py** → script principal contendo a limpeza e a análise
- **sales_cleaned.csv** → dados após a limpeza


##  Objetivos do projeto

- Ler e entender os dados brutos  
- Identificar problemas como:
  - valores nulos
  - duplicatas
  - preços inválidos (ex: 0)
  - tipos de dados incorretos
- Corrigir esses problemas usando Python e Pandas
- Criar métricas simples
- Gerar um gráfico para visualizar o faturamento por produto

---

##  Etapas realizadas

### 1. Carregamento e visualização inicial
Usei o Pandas para ler o arquivo `sales.csv` e visualizar as primeiras linhas, além de verificar tipos e contagem de valores.

### 2. Remoção de duplicatas
Foi identificado que havia uma linha duplicada, então ela foi removida com `drop_duplicates()`.

### 3. Tratamento de valores nulos
- Valores nulos em **quantity** foram substituídos por 1.  
- Valores nulos em **price** foram preenchidos usando a mediana dos preços válidos.

### 4. Correção de valores inválidos
Um dos produtos tinha preço igual a 0.  
Esse valor foi substituído pela mediana para manter consistência.

### 5. Criação de nova coluna
Foi criada a coluna **total_value**, calculada como:

