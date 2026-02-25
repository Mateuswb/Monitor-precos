# 🛒 Monitor de Preços — Automação de Produtos

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python) ![Selenium](https://img.shields.io/badge/Selenium-Automation-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

Python  
License: [MIT](https://opensource.org/licenses/MIT)

Um sistema em Python que automatiza a pesquisa e acompanhamento de produtos em sites de e-commerce como o **Mercado Livre**. Ideal para monitorar preços, comparar produtos e manter histórico sem esforço manual.

---

🔍 **Visão Geral**  
O **Monitor de Preços** coleta informações de produtos automaticamente, incluindo **título, preço e link**, filtrando resultados relevantes e evitando duplicados. Ele salva todas as buscas em um arquivo **JSON** para consulta futura, oferecendo uma forma prática de acompanhar produtos e suas variações de preço.

O foco é:  
- Automatizar pesquisas de produtos sem precisar acessar manualmente os sites.  
- Organizar resultados com dados limpos e confiáveis.  
- Manter um histórico completo de produtos pesquisados.

---

✅ **Funcionalidades**  
- 🔎 Pesquisa automatizada de produtos no Mercado Livre  
- ✅ Filtragem inteligente por relevância e correspondência de título  
- 💰 Ordenação por preço próximo ao valor máximo definido  
- ⚠️ Evita produtos duplicados  
- 💾 Histórico de produtos salvo em `data/produtos.json`  

---

🛠 **Como usar / Setup**  

Execute tudo em sequência no terminal:

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/monitor_precos.git
cd monitor_precos

# Criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # Linux/macOS

# Instalar dependências
pip install -r requirements.txt

# Rodar o sistema
python -m app.main
# ou
python app/main.py
