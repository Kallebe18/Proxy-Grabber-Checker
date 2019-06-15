import requests

url = "https://www.youtube.com.br"

good = open("good_ones.txt", "w")

with open("teste.txt", "r") as proxies:
	for proxy in proxies:
		proxy = proxy.split("\n", 1)[0]
		addr = proxy
		proxy = {"http": "http://"+addr}
		try:
			req = requests.get(url, proxies=proxy)
		except:
			print(addr+": FAIL")
		else:
			print(addr+": GOOD")
			good.write(addr+"\n")
