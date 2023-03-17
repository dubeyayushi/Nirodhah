import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'FRUITS_VEGGIES':2, 'PLACES_VISITED':9, 'CORE_CIRCLE':6, 'SUPPORTING_OTHERS': 6, 'SOCIAL_NETWORK': 5, 'ACHIEVEMENT': 4, 'DONATION': 3, 'BMI_RANGE': 1 , 'TODO_COMPLETED': 7 , 'FLOW': 5, 'DAILY_STEPS': 9, 'LIVE_VISION': 4, 'SLEEP_HOURS': 7, 'LOST_VACATION': 1, 'DAILY_SHOUTING': 3, 'SUFFICIENT_INCOME': 2, 'PERSONAL_AWARDS': 3, 'TIME_FOR_PASSION': 6, 'WEEKLY_MEDITATION': 7, 'GENDER': 'Male', 'WORK_LIFE_BALANCE_SCORE': 550.3})

print(r.json())
