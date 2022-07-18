import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

url = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_KEY = 'apikey'
APP_ID = 'id'


sheety_post_url = 'https://api.sheety.co/63dc0dcdc7380c2fcb76470680d6e21c/myWorkouts/workouts'

workout_done = input('what are the workout done for today?')

header = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

parameters = {
 "query": workout_done,
 "gender": "male",
 "weight_kg": 72.5,
 "height_cm": 158.64,
 "age": 28
}


response = requests.post(url=url, headers=header, json=parameters)
print(response.text)
list_of_exercise = response.json()['exercises']
print(list_of_exercise)
full_date = datetime.now()
date = full_date.strftime('%d/%m/%y')
time = full_date.strftime('%H:%M:%S')


for i in range(0, len(list_of_exercise)):
    sheety_parameters = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': list_of_exercise[i]['user_input'].title(),
            'duration': list_of_exercise[i]['duration_min'],
            'calories': list_of_exercise[i]['nf_calories']
        }
    }
    response1 = requests.post(url=sheety_post_url, auth=('username', 'password'), json=sheety_parameters)
    print(response1.text)


