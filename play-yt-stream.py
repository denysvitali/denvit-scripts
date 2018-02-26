import soco
for zone in soco.discover():
    my_zone = zone
    break
print("Found your zone: %s" % my_zone)
my_zone.play_uri('x-rincon-mp3radio://192.168.1.199:8080')
print("Now playing YT Live")
