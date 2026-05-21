import time
import requests
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Nome do tópico que criaste no ntfy
TOPIC = "come_solutions_sinais"

# Servidor minúsculo para enganar o Render e evitar erros de porta
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot esta vivo!")

def run_server():
    port = int(os.environ.get("PORT", 8080))
    httpd = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    httpd.serve_forever()

def enviar_notificacao(mensagem):
    try:
        requests.post(f"https://ntfy.sh/{TOPIC}", data=mensagem.encode('utf-8'))
    except Exception as e:
        print(f"Erro ao enviar notificacao: {e}")

def run_bot():
    print("O Robo Come Solutions esta operando...")
    enviar_notificacao("O robo iniciou com sucesso!")
    while True:
        # Aqui podes adicionar a logica de monitoramento depois
        print("Monitorando a plataforma...")
        time.sleep(300)

if __name__ == "__main__":
    # Inicia o servidor web em segundo plano para o Render nao dar erro
    threading.Thread(target=run_server, daemon=True).start()
    # Inicia o bot
    run_bot()
    
