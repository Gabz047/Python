# Passo a passo do projeto

# Passo 1 - Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login



#clicar - pyautogui.click
#escrever - pyautogui.write
#apertar - pyautogui.press

# Passo 2 - Fazer login

# Passo 3 - Importar a base de dados
 
# Passo 4 - Cadastrar um produto

# Passo 5 - Repetir isso até acabar a base de dados

import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pandas.read_csv("produtos.csv")
print(tabela)


pyautogui.PAUSE = 0.5
pyautogui.press("win");
time.sleep(1)
pyautogui.write("opera");
time.sleep(1)
pyautogui.press("enter");
time.sleep(1)
pyautogui.write(link);
time.sleep(1)
pyautogui.press("enter");
time.sleep(2)
pyautogui.click(x=-1290, y=357);
time.sleep(1)
pyautogui.write("qualquercoisa");
time.sleep(1)
pyautogui.click(x=-1529, y=457);
time.sleep(1)
pyautogui.write("qualquercoisa");
time.sleep(1)
pyautogui.press("enter");
time.sleep(2)

for linha in tabela.index:

    pyautogui.click(x=-1360, y=242);
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo);
    pyautogui.press("tab");
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca);
    pyautogui.press("tab");
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo);
    pyautogui.press("tab");
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria));
    pyautogui.press("tab");
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco));
    pyautogui.press("tab");
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo));
    pyautogui.press("tab");
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs);
    
    pyautogui.press("tab");
    pyautogui.press("enter");
    pyautogui.scroll(5000)


