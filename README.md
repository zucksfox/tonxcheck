
# 🧾 TON Wallet Checker

> Script Python sederhana untuk memeriksa informasi wallet TON (The Open Network) dari file `.txt`.

## ✅ Fitur Utama

- Baca alamat dari file teks (`wallets.txt`)
- Cek saldo dan status wallet
- Simpan hasil ke file (`results.txt`)
- Output jelas dan mudah dibaca

---

## 🛠️ Install Library

Pastikan kamu sudah menginstal Python dan library berikut:

```bash
pip install requests
```

---

## 📁 Struktur Proyek

```
ton-wallet-checker/
│
├── ton_wallet_checker_from_file.py   # Script utama
├── wallets.txt                       # Daftar alamat wallet
├── results.txt                       # Hasil output setelah eksekusi
└── README.md                         # Dokumentasi ini
```

---

## 📥 Cara Penggunaan

1. **Buat file `wallets.txt`** dengan 1 alamat per baris:

   ```
   UQDAef5AW-JFJ7n9cXSnEA14ehhIadBm7rF7DVcpnRIKT9Fc
   EQD8zlqVszMOAuykfolEoJsxzhPCmpvCzZgxVgjAKXYazWV_
   ```

2. **Jalankan script:**

   ```bash
   python ton_wallet_checker_from_file.py
   ```

3. **Lihat hasil di file `results.txt`.**

---

## 📝 Contoh Output di Terminal

```
TON Wallet Checker - Dari File
-------------------------------
Memeriksa: UQDAef5AW-JFJ7n9cXSnEA14ehhIadBm7rF7DVcpnRIKT9Fc
Status: uninitialized | Saldo: 0.0 TON

Memeriksa: EQD8zlqVszMOAuykfolEoJsxzhPCmpvCzZgxVgjAKXYazWV_
Status: active | Saldo: 1.23 TON

✅ Hasil disimpan ke results.txt
```

---

## 📄 Format Output di `results.txt`

```
UQDAef5AW-JFJ7n9cXSnEA14ehhIadBm7rF7DVcpnRIKT9Fc | Balance: 0.0 TON | Status: uninitialized
EQD8zlqVszMOAuykfolEoJsxzhPCmpvCzZgxVgjAKXYazWV_ | Balance: 1.23 TON | Status: active
```

---


🎉 Semoga bermanfaat!
