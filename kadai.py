import ipaddress

def calc_network_address():
    ip = input("IPアドレスを入力してください: ")
    mask = input("ネットマスクを入力してください: ")

    # IPアドレスとネットマスクからネットワークを作成
    network = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)

    print("ネットワークアドレス:", network.network_address)

# 実行
calc_network_address()
