import requests
import random

def dog_request():
    url = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(url)

    data = response.json()

    print(data['message'])
    #print(data['message'][30])
    i = 30
    dog_race = ""
    for letter in data['message']:
        if data['message'][i] != '/':
            dog_race += data['message'][i]
            i += 1
        else:
            break

    num = random.randint(0, 100)
    print(dog_race)
    print(random.choice([1, 2, 3]))
    print(num)

    if 'random' in globals():
        print("SIM")
    else:
        print("NAO")

