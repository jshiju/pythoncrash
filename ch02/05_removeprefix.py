url = "https://google.com"

site = url.removeprefix("http:/")   # error prefix
print(site)

site = url.removeprefix("https:/")  # partial prefix
print(site)

site = url.removeprefix("https://")  # corect prefix
print(site)

site = url.removeprefix("ttps://")  # wrong prefix
print(site)