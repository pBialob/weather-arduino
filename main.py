from m5stack import *
from m5ui import *
from uiflow import *
import urequests
import network
import wifiCfg
from libs.json_py import *
import time


setScreenColor(lcd.WHITE)


Random = None
humidity = None
temp = None
press = None
weather = None



city = M5TextBox(10, 150, "city", lcd.FONT_UNICODE, lcd.BLACK, rotate=0)
circle0 = M5Circle(56, 69, 18, lcd.BLACK, lcd.BLACK)
circle1 = M5Circle(131, 74, 13, lcd.BLACK, lcd.BLACK)
circle6 = M5Circle(100, 84, 55, lcd.WHITE, lcd.BLACK)
circle3 = M5Circle(80, 70, 17, lcd.BLACK, lcd.BLACK)
circle4 = M5Circle(85, 52, 22, lcd.BLACK, lcd.BLACK)
rectangle0 = M5Rect(63, 98, 2, 4, lcd.BLACK, lcd.BLACK)
rectangle1 = M5Rect(99, 93, 2, 13, lcd.BLACK, lcd.BLACK)
rectangle2 = M5Rect(78, 93, 2, 13, lcd.BLACK, lcd.BLACK)
rectangle5 = M5Rect(118, 91, 2, 17, lcd.BLACK, lcd.BLACK)
rectangle10 = M5Rect(44, 96, 2, 8, lcd.BLACK, lcd.BLACK)
huminidity = M5TextBox(79, 175, "H:", lcd.FONT_DejaVu18, lcd.BLACK, rotate=0)
label2 = M5TextBox(10, 175, "T:", lcd.FONT_DejaVu18, lcd.BLACK, rotate=0)
pressure = M5TextBox(129, 175, "P:", lcd.FONT_DejaVu18, lcd.BLACK, rotate=0)
t_val = M5TextBox(31, 179, "t", lcd.FONT_Default, lcd.BLACK, rotate=0)
h_val = M5TextBox(104, 179, "h", lcd.FONT_Default, lcd.BLACK, rotate=0)
p_val = M5TextBox(152, 180, "p", lcd.FONT_Default, lcd.BLACK, rotate=0)
label1 = M5TextBox(4, 4, "T[C] | H [%] | P [hPa]", lcd.FONT_DefaultSmall, lcd.BLACK, rotate=0)
circle2 = M5Circle(109, 70, 17, lcd.BLACK, lcd.BLACK)
circle5 = M5Circle(100, 84, 49, lcd.BLACK, lcd.BLACK)

import random


# Describe this function...
def show_sunny():
  global Random, humidity, temp, press, weather
  circle6.show()
  circle5.show()

# Describe this function...
def hide_sunny():
  global Random, humidity, temp, press, weather
  circle6.hide()
  circle5.hide()

# Describe this function...
def show_rainy():
  global Random, humidity, temp, press, weather
  circle0.show()
  circle1.show()
  circle2.show()
  circle3.show()
  circle4.show()
  rectangle0.show()
  rectangle1.show()
  rectangle2.show()
  rectangle5.show()
  rectangle10.show()

# Describe this function...
def hide_rainy():
  global Random, humidity, temp, press, weather
  circle0.hide()
  circle1.hide()
  circle2.hide()
  circle3.hide()
  circle4.hide()
  rectangle0.hide()
  rectangle1.hide()
  rectangle2.hide()
  rectangle5.hide()
  rectangle10.hide()

# Describe this function...
def animate_sunny():
  global Random, humidity, temp, press, weather
  Random = random.randint(49, 55)
  circle6.setSize(Random)
  circle5.show()

# Describe this function...
def animate_rainy():
  global Random, humidity, temp, press, weather
  Random = random.randint(2, 50)
  rectangle0.setSize(height=Random)
  Random = random.randint(2, 50)
  rectangle1.setSize(height=Random)
  Random = random.randint(2, 50)
  rectangle2.setSize(height=Random)
  Random = random.randint(2, 50)
  rectangle5.setSize(height=Random)
  Random = random.randint(2, 50)
  rectangle10.setSize(height=Random)

# Describe this function...
def init():
  global Random, humidity, temp, press, weather
  try:
    req = urequests.request(method='GET', url='https://api.openweathermap.org/data/2.5/weather?q=Warsaw&units=metric&appid=adb9f15b6acf914eeb1fef8e1db04d9f', headers={})
    humidity = get_json_key((get_json_key((req.text), 'main')), 'humidity')
    temp = get_json_key((get_json_key((req.text), 'main')), 'temp')
    press = get_json_key((get_json_key((req.text), 'main')), 'pressure')
    weather = get_json_key((get_json_key((req.text), 'weather'))[0], 'main')
    gc.collect()
    req.close()
  except:
    pass
  reset_animations()
  if weather == 'Cloudy':
    show_cloudy()
  if weather == 'Rain':
    show_rainy()
  if weather == 'Clear':
    show_sunny()
  city.setText('Warszawa')
  t_val.setText(str(temp))
  p_val.setText(str(press))
  h_val.setText(str(humidity))
  coreInkShow()

# Describe this function...
def setup_london():
  global Random, humidity, temp, press, weather
  try:
    req = urequests.request(method='GET', url='https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=adb9f15b6acf914eeb1fef8e1db04d9f', headers={})
    humidity = get_json_key((get_json_key((req.text), 'main')), 'humidity')
    temp = get_json_key((get_json_key((req.text), 'main')), 'temp')
    press = get_json_key((get_json_key((req.text), 'main')), 'pressure')
    weather = get_json_key((get_json_key((req.text), 'weather'))[0], 'main')
    gc.collect()
    req.close()
  except:
    pass
  reset_animations()
  if weather == 'Rain':
    show_rainy()
  if weather == 'Clear':
    show_sunny()
  if weather == 'Cloudy':
    show_cloudy()
  city.setText('London')
  t_val.setText(str(temp))
  p_val.setText(str(press))
  h_val.setText(str(humidity))
  coreInkShow()

# Describe this function...
def setup_warsaw():
  global Random, humidity, temp, press, weather
  try:
    req = urequests.request(method='GET', url='https://api.openweathermap.org/data/2.5/weather?q=Warsaw&units=metric&appid=adb9f15b6acf914eeb1fef8e1db04d9f', headers={})
    humidity = get_json_key((get_json_key((req.text), 'main')), 'humidity')
    temp = get_json_key((get_json_key((req.text), 'main')), 'temp')
    press = get_json_key((get_json_key((req.text), 'main')), 'pressure')
    weather = get_json_key((get_json_key((req.text), 'weather'))[0], 'main')
    gc.collect()
    req.close()
  except:
    pass
  reset_animations()
  if weather == 'Cloudy':
    show_cloudy()
  if weather == 'Rain':
    show_rainy()
  if weather == 'Clear':
    show_sunny()
  city.setText('Warszawa')
  t_val.setText(str(temp))
  p_val.setText(str(press))
  h_val.setText(str(humidity))
  coreInkShow()

# Describe this function...
def setup_stavanger():
  global Random, humidity, temp, press, weather
  try:
    req = urequests.request(method='GET', url='https://api.openweathermap.org/data/2.5/weather?q=Stavanger&units=metric&appid=adb9f15b6acf914eeb1fef8e1db04d9f', headers={})
    humidity = get_json_key((get_json_key((req.text), 'main')), 'humidity')
    temp = get_json_key((get_json_key((req.text), 'main')), 'temp')
    press = get_json_key((get_json_key((req.text), 'main')), 'pressure')
    weather = get_json_key((get_json_key((req.text), 'weather'))[0], 'main')
    gc.collect()
    req.close()
  except:
    pass
  reset_animations()
  if weather == 'Cloudy':
    show_cloudy()
  if weather == 'Rain':
    show_rainy()
  if weather == 'Clear':
    show_sunny()
  city.setText('Stavanger')
  t_val.setText(str(temp))
  p_val.setText(str(press))
  h_val.setText(str(humidity))
  coreInkShow()

# Describe this function...
def reset_animations():
  global Random, humidity, temp, press, weather
  hide_sunny()
  hide_rainy()
  hide_cloudy()

# Describe this function...
def hide_cloudy():
  global Random, humidity, temp, press, weather
  circle0.hide()
  circle1.hide()
  circle2.hide()
  circle3.hide()
  circle4.hide()

# Describe this function...
def show_cloudy():
  global Random, humidity, temp, press, weather
  circle0.show()
  circle1.show()
  circle2.show()
  circle3.show()
  circle4.show()


def buttonUP_wasPressed():
  global Random, humidity, temp, press, weather
  setup_stavanger()
  pass
btnUP.wasPressed(buttonUP_wasPressed)

def buttonMID_wasPressed():
  global Random, humidity, temp, press, weather
  setup_warsaw()
  pass
btnMID.wasPressed(buttonMID_wasPressed)

def buttonDOWN_wasPressed():
  global Random, humidity, temp, press, weather
  setup_london()
  pass
btnDOWN.wasPressed(buttonDOWN_wasPressed)


if 1000:
  wifiCfg.doConnect('iPhone (Piotr)', 'loleks123')
  while not (wifiCfg.wlan_sta.isconnected()):
    wait(1)
coreInkShow()
init()
while True:
  if weather == 'Rain':
    animate_rainy()
  else:
    animate_sunny()
  coreInkPartialShow(0, 0, 200, 200)
  wait_ms(2)
