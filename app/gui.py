import tkinter as tk
from tkinter import ttk
import webbrowser

class MonitorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor de Preços")
        self.root.state("zoomed")

        tk.Label(root, text="Clique duas vezes em um item para abrir no navegador",
                 font=("Arial", 12), fg="gray").pack(pady=5)

        # Estilo
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#f0f0f0", foreground="black",
                        rowheight=30, fieldbackground="#f0f0f0", font=("Arial", 11))
        style.configure("Treeview.Heading", font=("Arial", 13, "bold"),
                        background="#4a7abc", foreground="white")
        style.map("Treeview.Heading",
                  background=[("active", "#4a7abc")],
                  foreground=[("active", "white")])
        style.map("Treeview",
                  background=[("selected", "#347083")],
                  foreground=[("selected", "white")])

        # Tabela
        columns = ("Produtos", "Preço base", "Título", "Preço do produto", "Status", "Link")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "Produtos":
                self.tree.column(col, width=80, anchor="w")
            elif col == "Preço base":
                self.tree.column(col, width=70, anchor="center")
            elif col == "Preço do produto":
                self.tree.column(col, width=90, anchor="center")
            elif col == "Link":
                self.tree.column(col, width=0, stretch=False)
            elif col == "Status":
                self.tree.column(col, width=150, anchor="center")
            else:
                self.tree.column(col, width=360, anchor="w")

        self.tree.tag_configure("green", foreground="green")
        self.tree.tag_configure("red", foreground="red")
        self.tree.pack(expand=True, fill="both", padx=10, pady=10)
        self.tree.bind("<Double-1>", self.abrir_link)

        self.btn_buscar = tk.Button(root, text="Buscar Produtos",
                                    font=("Arial", 12, "bold"), bg="#4a7abc",
                                    fg="white", relief="raised", padx=10, pady=5)
        self.btn_buscar.pack(pady=10)

    def atualizar_tabela(self, resultados):
        self.tree.delete(*self.tree.get_children())
        for r in resultados:
            self.tree.insert(
            "",
            "end",
            values=(
                r["produto"],
                f"R$ {r['preco_base']:.2f}",
                r["titulo"],
                f"R$ {r['preco']}" if r["preco"] else "",
                r["status"],
                r["link"]
            ),
            tags=("green" if "✅" in r["status"] else "red",)
        )

    def abrir_link(self, event): 
        item = self.tree.selection()
        if item:
            link = self.tree.item(item, "values")[5]
            if link:
                webbrowser.open(link)