from tkinter import *
import requests
import json


root = Tk()
root.title('Weather App')
root.geometry('400x300')



api_request = requests.get('https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=20001&date=2021-09-25&distance=5&API_KEY=4282249A-2177-46C9-B374-4E05EE9650C4')
api = json.loads(api_request.content)
print('sk')
l_02 = Label(root, text=api).pack()


root.mainloop()