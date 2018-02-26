#!/bin/bash
# Tor's TransPort
_trans_port="9040"

# your internal interface
_inc_if="tor0"

#sudo iptables -F
#sudo iptables -t nat -F

sudo iptables -t nat -A PREROUTING -i $_inc_if -p udp --dport 53 -j REDIRECT --to-ports 5353
sudo iptables -t nat -A PREROUTING -i $_inc_if -p udp --dport 5353 -j REDIRECT --to-ports 5353
sudo iptables -t nat -A PREROUTING -i $_inc_if -p tcp --syn -j REDIRECT --to-ports $_trans_port
