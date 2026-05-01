💻 Projeto DIO - ETL com Python
🎯 Objetivo

Demonstrar, na prática, os conhecimentos adquiridos no curso Fundamentos de ETL (Extract, Transform, Load) com Python, da DIO.

📀 Estrutura do Projeto

O projeto é composto pelos seguintes arquivos e diretórios:

main.py → Script principal em Python
clientes.csv → Base de dados de entrada
README.md → Documentação do projeto
Diretórios:
data/ → Dados de entrada
output/ → Dados processados (saída do ETL)
projeto_dio_totvs_etl/ → Organização do projeto
💡 Funcionalidades

O script main.py executa um processo completo de ETL:

🔍 Extract

Realiza a leitura dos dados a partir do arquivo clientes.csv, convertendo-os para estruturas manipuláveis (dicionários).

🔄 Transform

Processa os dados gerando mensagens personalizadas de investimento, com base na profissão (job) do cliente.
Caso a profissão não esteja mapeada, é gerada uma mensagem padrão.

📦 Load

Após a transformação, os dados são exportados para o arquivo:

output/resultado.csv

💎 Melhorias Futuras
Integração com APIs públicas externas
Uso da API do ChatGPT para geração de mensagens mais inteligentes
Implementação de testes automatizados (QA 👀)
Validação de dados de entrada
🕵️‍♀️ Sobre

Olá! Eu sou Daniele Rodrigues Martins, bacharel em Engenharia da Computação pela UNIVESP (São Paulo).

Atualmente estou em transição para a área de Quality Assurance (QA) e venho desenvolvendo projetos práticos para fortalecer meu portfólio. Estou participando do Bootcamp da DIO em parceria com a TOTVS e aprofundando meus conhecimentos em dados, automação e testes.
