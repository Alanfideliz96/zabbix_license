# Zabbix License Expiration Monitor

Projeto para monitorar datas de expiração de licenças no **Zabbix**, utilizando  
**Zabbix Agent + scripts em Python + CSV** como fonte de dados.

O objetivo é gerar alertas automáticos quando licenças estiverem próximas do vencimento
ou já expiradas, organizadas por **cliente**.

## 📌 Visão geral

- As informações de licenças ficam em um arquivo CSV (fácil de manter).
- O Zabbix Agent executa scripts em Python via **UserParameter**.
- Um script faz o **Low Level Discovery (LLD)** dos clientes.
- Outro script calcula quantos dias faltam para a licença mais próxima vencer.
- O Zabbix cria itens e triggers automaticamente por cliente.

## 📁 Estrutura do projeto

zabbix-license-monitor/
├── scripts/

│ ├── license_discovery.py # Discovery de clientes (LLD)

│ └── license_days.py # Retorna dias para expiração

├── data/

│ └── licenses.csv # Base de dados das licenças

├── .gitignore

└── README.md

⚙️ Configuração do Zabbix Agent

Criar um arquivo de UserParameters, por exemplo:

C:\zabbix\conf\userparameters_license.conf

Conteúdo:

# Discovery de clientes
UserParameter=license.discovery,python "C:\zabbix\scripts\license_discovery.py"

# Dias para expiração da licença por cliente
UserParameter=license.days[*],python "C:\zabbix\scripts\license_days.py" "$1"


📊Integração com o Zabbix

No Zabbix Server:

Criar um template
Criar uma Discovery Rule usando a key license.discovery
Criar Item Prototypes
Key: license.days[{#CLIENTE}]

Criar Trigger Prototypes, por exemplo:

⚠️ <= 30 dias
🔥 <= 15 dias
❌ < 0 dias (licença expirada)

O script license_days.py retorna:

Número positivo → dias restantes para a licença mais próxima vencer

0 → vence hoje

Número negativo → licença já expirada

404 → cliente não encontrado 

