import pandas as pd

# 1. EXTRAÇÃO: O Python lê o seu arquivo da loja
dados = pd.read_csv('dados_brutos.csv')

# 2. TRANSFORMAÇÃO: Filtrar apenas vendas do setor Feminino (simulando uma regra de negócio)
vendas_femininas = dados[dados['setor'] == 'Feminino']

# 3. CARGA: Salva um novo arquivo apenas com o que você filtrou
vendas_femininas.to_csv('relatorio_final_feminino.csv', index=False)

print("Processamento concluído! O relatório final foi gerado.")