import requests

url = "https://www.eventbriteapi.com/v3/categories/"

payload = {}
headers = {
  'Authorization': '••••••',
  'Cookie': 'AS=36f9c3c1-f578-43f6-8f09-614e10850096; G=v%3D2%26i%3D0b921078-c035-473d-a6b0-9ee1b5cf3f02%26a%3D12c1%26s%3Df6f783842956cd7fac29e683a4d890404c7ca907; SP=AGQgbbkTxniauCIjdg7YrrrLF7ReFJReU7BKRIvfa9KX8827yqBojVI6e0CQyimdUOKUC47dGqWxnibvHrctqFdGKvF0FZvcO41ve28DgB2H8FZcFPS9l7VQC3Ews_r4KgNVv6hYcByVtsag3qql6ulYVF2qVH0a_H1_7aAvG-ERzv43YjhcrSxfgppN8nsqdTZ-1clC72hAEsXGB1dq1iouLIu7XCFdd2eyVZJRHp315QTYORYiB1Q; SS=AE3DLHTQ8Cu1ySXFdQdRX8Q2PTSxckj1Bw; eblang=lo%3Den_US%26la%3Den-us; mgref=typeins; mgrefby=; stableId=40d9b927-a592-4f89-9748-356e4e7e593b'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
