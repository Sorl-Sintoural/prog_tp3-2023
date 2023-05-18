
from time import sleep
import board
from adafruit_bme280 import basic as adafruit_bme280
import adafruit_tsl2591
print(" - - - Library Import Complete")

# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
tsl2591 = adafruit_tsl2591.TSL2591(i2c)
print(" - - - I2C Initialization Complete")


bme280.sea_level_pressure = 1013.25
print(" - - - Sea Level Pressure Set")

def read_capt() :
	try :
		Temperature = bme280.temperature
		RelHumidity = bme280.relative_humidity
		Pressure = bme280.pressure
		Altitude = bme280.altitude

		Lux = tsl2591.lux
		Infrared = tsl2591.infrared
		Visible = tsl2591.visible
		Spectrum = tsl2591.full_spectrum
	except :
		print(" - - - TOO MUCH LUX - - - ")

	capt_BME = (f"\nTemperature: {Temperature} 'C\n"
			f"Relative Humidity: {RelHumidity} %\n"
			f"Pressure: {Pressure} hPa\n"
			f"Altitude: {Altitude} meters\n")
	capt_TSL = (f"Total light: {Lux} lux\n"
			f"Infrared light: {Infrared}\n"
			f"Visible light: {Visible}\n"
			f"Full spectrum (IR + visible) light: {Spectrum}\n")

	print(f"{capt_BME}\n - - - - - - - \n{capt_TSL}")

	sleep(1)

	return Temperature , RelHumidity, Pressure, Spectrum