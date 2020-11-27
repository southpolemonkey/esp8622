# esp8266

## Grill temperature monitor

Phase 1

- Connect and start up esp8266 board, set up a simple web server
- Send data to an endpoint from esp8266 
- Connect esp8266 with arduino
- Pass data from arduino to esp8266
- Read temperature data from analog input
- Convert analog input to digital signal
- Display temperature on a LCD display
- Power arduino solution

Phase 2

- Set up a proxy server to convert http requests to https and send to parse.com
- Set up trigger

Phase 3

- Create a client for reading data from parse.com


## Reference

### esp8266 set up

- install ch340g driver https://www.arduined.eu/ch340g-converter-windows-7-driver-download/
- add http://arduino.esp8266.com/stable/package_esp8266com_index.json in arduino ide preference
- install esp8622 package in boarder manager
- select serial port


https://tttapa.github.io/ESP8266/Chap07%20-%20Wi-Fi%20Connections.html

https://maakbaas.com/esp8266-iot-framework/logs/https-requests/

https://randomnerdtutorials.com/esp32-client-server-wi-fi/

https://medium.com/@kazmiekr/smoking-meat-with-the-internet-of-things-b047ecda94a0


### Node

http://docs.parseplatform.org/parse-server/guide/#connect-your-app-to-parse-server