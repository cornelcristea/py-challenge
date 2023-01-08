# 6. Send an e-mail every time you start your PC with the weather details from the city you are in.<br>
# To access weather details you can make a request to this API/endpoint: [openweathermap - API]
# (https://openweathermap.org/api)<br>
# To send e-mail you can use the smtplib library<br>
# To access the city you are in, you can make a request using [this API] (api.ipstack.com)


from smtplib  import SMTP
from requests import get
from geocoder import ip

def get_location():
   info = ip('me')
   lat = info.lat
   lon = info.lng
   name = info.city
   return lat, lon, name

def get_weather(lat, lon, name):
   api_url = 'api.openweathermap.org/data/2.5/wheater'
   api_key = 'bd5e378503939ddaee76f12ad7a97608'
   url = api_url + "?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key
   
   response = get(url)
 
   if response.status_code == 200:
      data = response.json()
      main = data['main']
      temperature = main['temp']
      humidity = main['humidity']
      pressure = main['pressure']
      report = data['weather']
      n = f'{name:-^30}'
      t = f'Temperature: {temperature}'
      h = f'Humidity: {humidity}'
      p = f'Pressure: {pressure}'
      wheather_info = n + '\n' + t + '\n' + h + '\n' + p
   else:
      print(response.text)

   return wheather_info

def send_email(content):
   host = ''
   port = 25
   local_hostname = 'localhost'

   sender = 'petrucornel.cristea@gmail.com'
   receivers = ['petrucornel.cristea@gmail.com','cornelcristea97@gmail.com']
   message = content

   try:
      smtpObj = SMTP(host, port, local_hostname)
      smtpObj.sendmail(sender, receivers, message)
      msg = 'Successfully sent email'
   except:
      msg = 'Error: unable to send email'

   return msg


if __name__ == '__main__':
   lat, lon, name = get_location()
   wheather_info = get_weather(lat, lon, name)
   send_email(wheather_info)
