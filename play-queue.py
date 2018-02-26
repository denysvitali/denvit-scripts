import soco
for zone in soco.discover():
    my_zone = zone
    break
print("Found your zone: %s" % my_zone)
my_zone.play_from_queue(0)
