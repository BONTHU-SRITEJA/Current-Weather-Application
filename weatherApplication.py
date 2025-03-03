import requests
city_name = input("Enter city name :")
API = 'f07127c496527e8215dc89942a18d5cc'
url = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+API+"&units=metric"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Weather of ",city_name," is :",data['weather'][0]['description'])
    print("Current temperature :",data['main']['temp'])
    print("Current temperature feels like :",data['main']['feels_like'])
    print("Humidity is :",data['main']['humidity'])
else:
    print("Error:", response.status_code, response.text)
