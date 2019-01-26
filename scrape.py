import sys, json, requests, time

url = "https://api.ethermine.org/miner/:4A6944369Cac57436203c9651201b5C1FA63A754/dashboard/"
offline = True
threshold = 25000000

while True:
    try:
        r = requests.get(url=url)
    except requests.ConnectionError as e:
        raise(e)

    data = r.json()
    rate = data["data"]["statistics"][0]["currentHashrate"]
    print("Current Hashrate: " + str(rate))

    if rate < threshold and not offline:
        exit(0)

    if rate > threshold:
        offline = False
        print("Miner is online")

    time.sleep(20)
