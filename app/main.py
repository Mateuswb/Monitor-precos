from historico import salvar_historico
import threading
import json
from selenium import webdriver
from search import pesquisar_produto
from gui import MonitorGUI
import tkinter as tk

def buscar_produtos_thread(gui):
    gui.root.iconify()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    resultados = []

    with open("data/produtos.json", "r", encoding="utf-8") as f:
        produtos = json.load(f)

    for produto in produtos:
        r = pesquisar_produto(produto["busca"], driver, produto["preco_max"])
        if not r:
            resultados.append({"produto": produto["nome"], "titulo": "Nenhum resultado",
                               "preco": "", "status": "", "link": ""})
        else:
            for p in r:
                status = "✅ Abaixo do preço!" if p["preco"] <= produto["preco_max"] else "❌ Acima do preço"
                resultados.append({"produto": produto["nome"], "titulo": p["titulo"],
                                   "preco": p["preco"], "status": status, "link": p["link"]})

    driver.quit()
    gui.root.deiconify()
    gui.atualizar_tabela(resultados)
    salvar_historico(resultados)

def buscar_produtos(gui):
    threading.Thread(target=buscar_produtos_thread, args=(gui,)).start()

if __name__ == "__main__":
    root = tk.Tk()
    gui = MonitorGUI(root)

    with open("data/produtos.json", "r", encoding="utf-8") as f:
        produtos = json.load(f)
    for produto in produtos:
        gui.tree.insert("", "end", values=(produto["nome"], "", "", "", ""))

    gui.btn_buscar.config(command=lambda: buscar_produtos(gui))

    root.mainloop()