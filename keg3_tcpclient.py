# TCP Server untuk client keg3_tcpclient.py
# import library, membuat socket TCP, dan membuka server di port 50003
import socket
hostname = "localhost"
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect((hostname, 50003))
print("Program perhitungan luas jajargenjang")
pesan = ""
# loop selama pesannya bukan "keluar"
while pesan.lower() != "keluar":
    pesan = input("Pesan: ")
    r.send(pesan.encode())
    if pesan.lower() != "keluar":
        response = r.recv(1024).decode()
        print("Respon:", response)
# apabila "keluar" maka tutup koneksi
r.close()