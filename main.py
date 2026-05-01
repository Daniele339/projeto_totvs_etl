import pandas as pd

# Lê o CSV
df = pd.read_csv('data/clientes.csv')

# Converte para lista de dicionários
users = df.to_dict(orient='records')

# Garante estrutura
for user in users:
    user['news'] = []
    
    
def generate_news(user):
    name = user.get('name', 'cliente')
    user_id = user.get('UserID', 'sem_id')

    if user.get('job') == 'ninja especialista':
        return f"Você tem Perfil Premium, invista hoje para aposentadoria, {user_id}: {name}!"
    
    if user.get('job') == 'ninja':
        return f"Você tem Perfil Comum, invista em um seguro de vida simples, {user_id}:{name}!"
    
    if user.get('job') == 'ninja renegado':
        return f"{name}, no momento não é possível investir devido a restrições."

    return f"{name}, descubra oportunidades de investimento no nosso banco!"
     
for user in users:
    news = generate_news(user)
    
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })
    
# Convertendo de volta para DataFrame
df_final = pd.DataFrame(users)

# Salvando resultado
df_final.to_csv('output/resultado.csv', index=False)

print("ETL com pandas finalizado!")