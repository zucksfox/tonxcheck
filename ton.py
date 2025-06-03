import requests

def check_ton_wallet(address):
    url = f"https://toncenter.com/api/v3/addressInformation?address={address}&use_v2=true"
    
    try:
        response = requests.get(url)
        data = response.json()

        balance = int(data.get("balance", 0)) / 1e9  # Konversi ke TON 
        status = data.get("status", "unknown")
        last_tx_hash = data.get("last_transaction_hash", "")
        last_tx_lt = data.get("last_transaction_lt", "")

        return {
            "address": address,
            "balance": balance,
            "status": status,
            "last_tx_hash": last_tx_hash,
            "last_tx_lt": last_tx_lt
        }

    except Exception as e:
        print(f"[ERROR] Gagal cek {address}: {str(e)}")
        return None

def read_wallets_from_file(filename):
    try:
        with open(filename, "r") as file:
            wallets = [line.strip() for line in file if line.strip()]
        return wallets
    except FileNotFoundError:
        print(f"[ERROR] File {filename} tidak ditemukan.")
        return []

def save_results_to_file(results, output_file="results.txt"):
    with open(output_file, "w") as file:
        for res in results:
            line = f"{res['address']} | Balance: {res['balance']} TON | Status: {res['status']}\n"
            file.write(line)
    print(f"\n✅ Hasil disimpan ke {output_file}")

def main():
    input_file = "wallets.txt"
    print("TON Wallet Checker")
    print("-------------------------------")

    addresses = read_wallets_from_file(input_file)

    if not addresses:
        print("[INFO] Tidak ada alamat untuk diproses.")
        return

    results = []

    print(f"\n🔍 Memeriksa {len(addresses)} wallet...\n")
    for addr in addresses:
        print(f"Memeriksa: {addr}")
        info = check_ton_wallet(addr)
        if info:
            results.append(info)
            print(f"Status: {info['status']} | Saldo: {info['balance']} TON\n")
        else:
            print("Gagal mendapatkan informasi.\n")

    save_results_to_file(results)

if __name__ == "__main__":
    main()