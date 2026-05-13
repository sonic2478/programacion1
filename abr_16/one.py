import requests
ans = requests.get(f'https://api.pwnedpasswords.com/range/40bdf')
print(ans.json())