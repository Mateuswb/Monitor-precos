from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Função de filtro inteligente
def titulo_valido(titulo, busca):
    titulo = titulo.lower()
    palavras_busca = busca.lower().split()

    palavras_obrigatorias = []
    palavras_normais = []

    for palavra in palavras_busca:
        if any(c.isdigit() for c in palavra):
            palavras_obrigatorias.append(palavra)
        elif len(palavra) <= 3:
            palavras_obrigatorias.append(palavra)
        else:
            palavras_normais.append(palavra)

    for palavra in palavras_obrigatorias:
        if palavra not in titulo:
            return False

    correspondencias = 0
    for palavra in palavras_normais:
        if palavra in titulo:
            correspondencias += 1

    if palavras_normais:
        return correspondencias >= len(palavras_normais) // 2

    return True

# Função de pesquisa
def pesquisar_produto(busca, driver, preco_max):
    driver.get("https://www.mercadolivre.com.br/")

    try:
        WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Aceitar")]'))
        ).click()
    except:
        pass

    caixa = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.NAME, "as_word"))
    )
    caixa.clear()
    caixa.send_keys(busca)
    caixa.submit()

    produtos_container = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ol.ui-search-layout"))
    )

    produtos = produtos_container.find_elements(By.CSS_SELECTOR, "li.ui-search-layout__item")
    resultados = []
    titulos_vistos = set()

    for p in produtos:
        try:
            titulo_elem = p.find_element(By.CSS_SELECTOR, "a.poly-component__title")
            link = titulo_elem.get_attribute("href")
            titulo = titulo_elem.text.strip()

            #  evitar produtos duplicados pelo título
            if titulo in titulos_vistos:
                continue
            titulos_vistos.add(titulo)

            preco_elem = p.find_element(By.CSS_SELECTOR, "span.andes-money-amount__fraction")
            preco = int(preco_elem.text.replace(".", "").replace(",", ""))

            if titulo_valido(titulo, busca):
                resultados.append({
                    "titulo": titulo,
                    "preco": preco,
                    "link": link
                })

        except:
            continue

    # Produtos abaixo do preço ou mais próximos
    abaixo = [p for p in resultados if p["preco"] <= preco_max]
    acima = [p for p in resultados if p["preco"] > preco_max]

    if abaixo:
        abaixo.sort(key=lambda x: abs(preco_max - x["preco"]))
        return abaixo[:3]
    else:
        acima.sort(key=lambda x: x["preco"])
        return acima[:3]