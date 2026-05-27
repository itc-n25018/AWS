def calc_network_address(ip, netmask):
    # IPアドレスとネットマスクを分割
    ip_parts = list(map(int, ip.split(".")))
    mask_parts = list(map(int, netmask.split(".")))

    # AND演算でネットワークアドレスを計算
    network_parts = []

    for i in range(4):
        network_parts.append(ip_parts[i] & mask_parts[i])

    # 文字列に戻す
    return ".".join(map(str, network_parts))


# 使用例
ip = "192.168.1.10"
netmask = "255.255.255.0"

print(calc_network_address(ip, netmask))

