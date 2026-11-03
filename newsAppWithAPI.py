import requests
x = requests.get('https://gnews.io/api/v4/search?apikey=e3caeee64055e0ab6c8628cfe8416717&q=YouTube&lang=en&country=in&max=10&in=titlehttps://gnews.io/api/v4/search?apikey=e3caeee64055e0ab6c8628cfe8416717&q=National+news&lang=en&country=in&max=10&in=title')
data = x.json()
print("Headlines: ")
print(data["articles"][0]["title"])
x = requests.get('https://gnews.io/api/v4/search?apikey=e3caeee64055e0ab6c8628cfe8416717&q=International+news&lang=en&country=in&max=10&in=title')
data = x.json()
print(data["articles"][0]["title"])

print('''1. YouTube News
2. National News
3. International News
4. Educational News''')

choice = int(input("Enter the choice [1/2/3/4/5(EXIT)]: "))
if choice == 1:
    print("YouTube News")
    x = requests.get('https://gnews.io/api/v4/search?apikey=e3caeee64055e0ab6c8628cfe8416717&q=YouTube&lang=en&country=in&max=10&in=title')
    data = x.json()
    print("Title:")
    print(data["articles"][0]["title"])
    print("Description:")
    print(data["articles"][0]["description"])
    print("Content:")
    print(data["articles"][0]["content"])
elif choice == 2:
    print("National News")
    x = requests.get('https://gnews.io/api/v4/search?apikey=e3caeee64055e0ab6c8628cfe8416717&q=YouTube&lang=en&country=in&max=10&in=titlehttps://gnews.io/api/v4/search?apikey=e3caeee64055e0ab6c8628cfe8416717&q=National+news&lang=en&country=in&max=10&in=title')
    data = x.json()
    print("Title:")
    print(data["articles"][0]["title"])
    print("Description:")
    print(data["articles"][0]["description"])
    print("Content:")
    print(data["articles"][0]["content"])
elif choice == 3:
    print("International News")
    x = requests.get('https://gnews.io/api/v4/search?apikey=e3caeee64055e0ab6c8628cfe8416717&q=International+news&lang=en&country=in&max=10&in=title')
    data = x.json()
    print("Title: ",data["articles"][0]["title"])
    print()
    print("Description: ",data["articles"][0]["description"])
    print()
    print("Content: ",data["articles"][0]["content"])
    print()
elif choice == 4:
    print("Educational News")
    x = requests.get('https://gnews.io/api/v4/search?apikey=e3caeee64055e0ab6c8628cfe8416717&q=Educational+news&lang=en&country=in&max=10&in=title')
    data = x.json()
    print("Title:")
    print(data["articles"][0]["title"])
    print("Description:")
    print(data["articles"][0]["description"])
    print("Content:")
    print(data["articles"][0]["content"])
else:
    print("Not a valid choice!")
    print("Exiting...\nThank you!")