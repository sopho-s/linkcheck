import socket
import json
import os
import base64

def installserver(ipport):
    print("Binding...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(ipport)
    s.listen()
    while True:
        print(f"Install server listening on addr {ipport}")
        c, addr = s.accept()
        print(f"request from {addr}")
        certs = {}
        dir_list = os.listdir("/root/.mitmproxy/")
        print(f"FILES: {dir_list}")
        for cert in ["mitmproxy-ca.pem", "mitmproxy-ca-cert.pem", "mitmproxy-ca-cert.p12", "mitmproxy-ca-cert.cer"]:
            with open("/root/.mitmproxy/" + cert, "rb") as f:
                certs[cert] = base64.b64encode(f.read()).decode()
        c.send(json.dumps(certs).encode())
        c.close()

def installclient(ipport):
    s = socket.socket()
    s.connect(ipport)
    data = ""
    while (tmp := s.recv(1024)):
        data += tmp.decode()
    s.close()
    certs: dict = json.loads(data)
    try:
        os.makedirs("/etc/nixos/certs/")
    except:
        pass
    for certname, cert in certs.items():
        with open("/etc/nixos/certs/" + certname, "wb") as f:
            f.write(base64.b64decode(cert))

if __name__ == "__main__":
    installclient(("127.0.0.1", 4321))