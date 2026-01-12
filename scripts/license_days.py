import sys
from datetime import datetime

# importa a função do outro script
from license_discovery import load_licenses

def days_to_expire(cliente):
    """
    Retorna o menor número de dias para expiração 
    dentre todas as licenças de um cliente

    """
    today = datetime.today()
    days_list = []

    for lic in load_licenses():
        if lic["cliente"] == cliente:
            exp = datetime.strptime(lic["expiracao"], "%d/%m/%Y")
            days_list.append((exp - today).days)
    
    if not days_list:
        return "Cliente não encontrado" #cliente não encontrado

    return min(days_list)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Precisa passar o cliente meu amigo, desse jeito abaixo:\n python license_days.py cliente ")
        sys.exit(0)
    

    cliente = sys.argv[1]
    print(days_to_expire(cliente))

