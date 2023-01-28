# :partly_sunny: Weather Forecast

Weather Forecast using python

## :octocat: Installation

Clone the repository

```bash

git@github.com:LuizaAlanis/weather-forecast.git

```

## :cloud: Usage

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

## :sunny: Output example

<kbd>![Example of output](https://github.com/LuizaAlanis/weather-forecast/blob/main/output_example.png)</kbd>

## :rocket: Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
