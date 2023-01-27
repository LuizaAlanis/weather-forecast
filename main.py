import requests


def weather(city):
    # display the message
    print('Displaying Weater report for: ' + city)

    # fetch the weather details
    url = 'https://wttr.in/{}'.format(city)
    res = requests.get(url)

    # display the result!
    print(res.text)


if __name__ == '__main__':
    # input the city name
    city = input('input the city name: ')
    # call function
    weather(city)
