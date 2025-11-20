import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados
df = pd.read_csv("sales.csv")

print("===== DADOS BRUTOS (primeiras linhas) =====")
print(df.head(), "\n")

print("===== INFO INICIAL =====")
print(df.info(), "\n")

print("===== ESTATÍSTICAS INICIAIS DE PREÇO =====")
print(df["price"].describe(), "\n")

# 2. Ajustar tipos de dados
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 3. Remover duplicatas exatas
linhas_antes = len(df)
df = df.drop_duplicates()
linhas_depois = len(df)
print(f"Removidas {linhas_antes - linhas_depois} linhas duplicadas.\n")

# 4. Tratar valores nulos
df["quantity"] = df["quantity"].fillna(1)

mediana_preco = df["price"].median()
df["price"] = df["price"].fillna(mediana_preco)

# 5. Corrigir preços inválidos (0 ou negativos)
df.loc[df["price"] <= 0, "price"] = mediana_preco

print("===== ESTATÍSTICAS APÓS TRATAMENTO DE PREÇO =====")
print(df["price"].describe(), "\n")

# 6. Criar coluna total de venda
df["total_value"] = df["price"] * df["quantity"]

print("===== AMOSTRA DOS DADOS APÓS LIMPEZA =====")
print(df.head(), "\n")

# 7. Agrupar por produto
revenue_by_product = df.groupby("product")["total_value"].sum().sort_values(ascending=False)
print("===== FATURAMENTO POR PRODUTO =====")
print(revenue_by_product, "\n")

# 8. Gráfico
revenue_by_product.plot(kind="bar")
plt.title("Faturamento total por produto")
plt.xlabel("Produto")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.show()

# 9. Salvar CSV limpo
df.to_csv("sales_cleaned.csv", index=False)
print("Arquivo 'sales_cleaned.csv' salvo com sucesso.")
