import requests

# API URL

url = "https://live.staticflickr.com/3ee5137177558399f200bd2858771cff/27adf5699966df27_500px.jpg"



# Send Get Request
response = requests.get(url)

print(response.content)
