# TCP Server untuk client keg3_tcpclient.py
# import library, membuat socket TCP, dan membuka server di port 50003
import socket
r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.bind(("", 50003))
r.listen(5)
print("Server penghitung luas jajargenjang otomatis sudah siap")
alas = None
tinggi = None
data = ""
# loop utama server
while True:
    komm, addr = r.accept()
    while True:
        data = komm.recv(1024).decode().strip().lower()
        if not data:
            continue
        print("Perintah:", data)
        # jika perintah keluar
        if data == "keluar":
            r.close()
            break
        # input dan menyimpan parameter alas dan tinggi
        if data.startswith("alas="):
            alas = float(data.split("=")[1])
            komm.send("parameter dicatat".encode())
            continue
        if data.startswith("tinggi="):
            tinggi = float(data.split("=")[1])
            komm.send("parameter dicatat".encode())
            continue
        # jika parameter belum lengkap
        if data == "hitung":
            if alas is None or tinggi is None:
                komm.send("parameter belum lengkap".encode())
            # hitung luas jajargenjang = alas x tinggi
            else:
                luas = alas * tinggi
                pesan = f"luas jajargenjang dengan alas {alas:.0f} dan tinggi {tinggi:.0f} adalah {luas:.0f}"
                komm.send(pesan.encode())
        else:
            komm.send("perintah tidak dimengerti".encode())
    break