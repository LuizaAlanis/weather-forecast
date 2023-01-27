import requests

#input the city name
city = input('input the city name')

weather(city)

def weather(city)
  # display the message!
  print('Displaying Weater report for: ' + city)
  
  # fetch the weater details
  url = 'https://wttr.in/{}'.format(city)
  res = requests.get(url)

  #display the result!
  print(res.text)
