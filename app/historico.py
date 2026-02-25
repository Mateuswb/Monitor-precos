import csv
from datetime import datetime
import os

ARQUIVO = "data/historico.csv"

def salvar_historico(resultados):
    precisa_cabecalho = (
        not os.path.isfile(ARQUIVO) or
        os.path.getsize(ARQUIVO) == 0
    )

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if precisa_cabecalho:
            writer.writerow(["data", "produto", "titulo", "preco", "link"])

        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")

        for r in resultados:
            if r["preco"] != "":
                writer.writerow([
                    data_atual,
                    r["produto"],
                    r["titulo"],
                    r["preco"],
                    r["link"]
                ])