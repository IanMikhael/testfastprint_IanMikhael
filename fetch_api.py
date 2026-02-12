import requests
import hashlib
import datetime
import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from app_produk.models import Produk, Kategori, Status

def fetch_data():
    #1. Konfigurasi Auth (soal no 1)
    now = datetime.datetime.now()
    #Format: bisacoding-dd-mm-yy
    username = f"tesprogrammer{now.strftime('%d%m%y')}C{now.strftime('%H')}"
    password_raw = f"bisacoding-{now.strftime('%d-%m-%y')}"
    password_md5 = hashlib.md5(password_raw.encode()).hexdigest()

    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
    
    data = {
        'username': username,
        'password': password_md5
    }

    try:
        print(f"Menarik data dengan username: {username}...")
        response = requests.post(url, data=data)
        response.raise_for_status()
        json_data = response.json()

        if json_data.get('error') == 0:
            produk_list = json_data.get('data', [])
            
            for item in produk_list:
                #2. Simpan/Update Kategori
                kategori_obj, _ = Kategori.objects.get_or_create(
                    nama_kategori=item['kategori']
                )

                #3. Simpan/Update Status
                status_obj, _ = Status.objects.get_or_create(
                    nama_status=item['status']
                )

                #4. Simpan/Update Produk (soal nomor 3)
                Produk.objects.update_or_create(
                    id_produk=item['id_produk'],
                    defaults={
                        'nama_produk': item['nama_produk'],
                        'harga': item['harga'],
                        'kategori': kategori_obj,
                        'status': status_obj
                    }
                )
            print(f"Berhasil! {len(produk_list)} data telah dimasukkan ke database.")
        else:
            print(f"Gagal: {json_data.get('ket')}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    fetch_data()