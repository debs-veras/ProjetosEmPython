import webbrowser

def abrir_site_no_navegador(url):
    try:
        webbrowser.open(url)
    except Exception as e:
        print("Ocorreu um erro ao abrir o site no navegador:", e)

# Exemplo de uso:
url = "https://www.netflix.com/browse"  # Substitua pela URL do site que deseja abrir
abrir_site_no_navegador(url)

# import subprocess

# def abrir_notebook():
#     try:
#         # Substitua o caminho abaixo pelo caminho completo do executável do seu notebook
#         caminho_do_notebook = r"C:\Users\debor\AppData\Local\Discord\app-1.0.9015\Discord.exe"

#         # Executa o comando para abrir o notebook
#         subprocess.Popen([caminho_do_notebook])
#     except Exception as e:
#         print("Ocorreu um erro ao abrir o notebook:", e)

# # Exemplo de uso:
# abrir_notebook()

