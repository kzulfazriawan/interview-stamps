from datetime import datetime

import requests

def soal_test_1(arr: list) -> None:
    result = []
    for i in arr:
        try:
            res = str(i)
            if i % 3 == 0 or i % 5 == 0:
                res = ""
                if i % 3 == 0:
                    res += "Foo"
                if i % 5 == 0:
                    res += "Bar"
            result.append(res)
        except ValueError:
            print("list is not numeric")
    print(", ".join(result))


def soal_test_2(hour: str = "12:00:00") -> None:
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": "Jakarta",
        "appid": "778b4e84968cc6919c048076f35b406d",
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    for entry in data['list']:
        timestamp = datetime.utcfromtimestamp(entry.get("dt"))
        str_date  = timestamp.strftime("%a, %d %b %Y")
        hour_pick = timestamp.strftime("%H:%M:%S")

        if hour_pick == hour:
            temperature = entry['main']['temp']
            description = entry['weather'][0]['description']

            print(f"{str_date}: {temperature}°C, Description: {description}")

if __name__ == "__main__":
    soal_test_1([*range(1, 101)])
    soal_test_2()
