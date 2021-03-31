import requests, json

class Temperature(object):
    def __init__(self,place):
        self.place=place
    
    def __repr__(self):
        temperature=self.weather()
        return str(f"It's currently{temperature} in {self.place}")

    def weather(self):
        url=f"https://openweathermap.org/" in {self.place}
        req=requests.get(url)
        return temperature

if __name__=="__main__":
    print(Temperature("Chicago"))