"""
helper micropython function to auto connecting wifi when esp8266 starts
"""

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect("WiFi-9488", "85228498")
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())