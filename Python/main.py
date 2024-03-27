import requests

'''''response = requests.post(url='https://api.pokemonbattle.me/trainers/reg', 
              json={
                 "trainer_token": "16ee55a10077f67c6c06954e20edcc5b",
                 "email": "ustin2202@gmail.com",
                 "password": "Nevergreen2"
                 },                        
                  headers={'Content - Type': 'application/json'})
print(response)'''''

'''response = requests.post(url='https://api.pokemonbattle.me/trainers/confirm_email', 
              json={"trainer_token": "16ee55a10077f67c6c06954e20edcc5b"},                        
                  headers={'Content - Type': 'application/json'})
print(response)'''
TOKEN = '16ee55a10077f67c6c06954e20edcc5b'
HOST = 'https://api.pokemonbattle.me/'

response = requests.post(url=f'{HOST}pokemons', #Создание покемона
              json={
                    "name": "Бульбазавр",
                    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
                   },                        
                     headers={'Content - Type': 'application/json', "trainer_token": "16ee55a10077f67c6c06954e20edcc5b"})

print(response)

response = requests.put(url='https://api.pokemonbattle.me/pokemons',  #изменение покемона
              json={
                     "pokemon_id": "14858",
                     "name": "Kitty",
                     "photo": "https://dolnikov.ru/pokemons/albums/012.png"
                   },                        
                     headers={'Content - Type': 'application/json', "trainer_token": "16ee55a10077f67c6c06954e20edcc5b"})

print(response)

response = requests.post(url=f'{HOST}trainers/add_pokeball',  #Поймать покемона в покебол
              json= {
                     "pokemon_id": "14858"
                     },                        
                     headers={'Content - Type': 'application/json', "trainer_token": "16ee55a10077f67c6c06954e20edcc5b"})
print(response)



print(f'code: {response.status_code} - {response.reason}. Message: {response.text}')

if response.status_code == 200:
    print('Ok!')
else:
    print('Bad')




