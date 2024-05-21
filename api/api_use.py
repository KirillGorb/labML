from requests import get

age = input('Введите age = ')
education = input('Введите education = ')
sports = input('Введите sports = ')
model_id = input('Введите id = ')

print(get(f'http://localhost:5000/api?age= {age}&education= {education}&sports={sports}&model_id={model_id}').json())