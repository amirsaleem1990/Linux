#!/home/amir/.venv_base/bin/python3

def check_internet():
	import requests
	import subprocess
	try:
		# First, try pinging 8.8.8.8 once, with 1s timeout
		ping_result = subprocess.run(
			['ping', '-q', '-c', '1', '-W', '1', '8.8.8.8'],
			stdout=subprocess.DEVNULL,
			stderr=subprocess.DEVNULL
		)
		if ping_result.returncode != 0:
			return False

		# Then try accessing https://google.com with 5s timeout
		response = requests.get('https://google.com', timeout=5)
		return response.status_code == 200
	except Exception:
		return False

if __name__ == "__main__":
	print(check_internet())