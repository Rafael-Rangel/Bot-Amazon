import sys
from playwright.sync_api import sync_playwright

# Recebe o código passado como argumento
codigo = sys.argv[1] if len(sys.argv) > 1 else None

with sync_playwright() as p:
    # Modo headless para produção
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.google.com", wait_until="domcontentloaded")
    
    # Espera o campo de busca carregar usando xpath
    page.wait_for_selector('xpath=//*[@id="APjFqb"]')
    
    if codigo:
        page.locator('xpath=//*[@id="APjFqb"]').fill(codigo)
        page.keyboard.press("Enter")
    
    print(f"✅ Pesquisa feita no Google com o código: {codigo}")
    page.wait_for_timeout(5000)
    browser.close()
