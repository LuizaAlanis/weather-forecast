# Weather Forecast

Weather Forecast using python

## Installation

Clone the repository

```bash

git@github.com:LuizaAlanis/weather-forecast.git

```

## Usage

```python

# implement the function with the request
def weather(city):
    url = 'https://wttr.in/{}'.format(city)
    res = requests.get(url)

    # display
    print(res.text)


# call the function and enter a city
weather(city)

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
