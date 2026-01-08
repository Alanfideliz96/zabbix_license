import csv
import json
from pathlib import Path


CSV_FILE = Path("data/licenses.csv")

def load_licenses():
    """
    Vamos ler o CSV e devolver uma lista de dicionários com cliente,
    produto e data de expiração
    """

    licenses = []

    #esse encoding latin-1 é para ler corretamente se vier com caracteres com acento ou especiais br
    with open(CSV_FILE, encoding="latin-1") as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            licenses.append({
                "cliente": row["cliente"].strip(),
                "produto": row["produto"].strip(),
                "expiracao": row["expiracao"].strip()
            })
            
    return licenses

if __name__ == "__main__":
    for lic in load_licenses()[:5]:
        print(lic)