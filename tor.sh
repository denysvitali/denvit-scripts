#!/bin/bash
socks_server=127.0.0.1:9050

id="$RANDOM"
tun="$(printf 'tun%04x' "$id")"
ip tuntap add dev $tun mode tun
ip link set $tun up
ip addr add 169.254.1.1/30 dev $tun
sysctl -w net.ipv4.conf.$tun.forwarding=1
ip rule add fwmark $id lookup $id
ip route add default via 169.254.1.2 table $id
iptables -t mangle -I PREROUTING -i wlp7s0 -p tcp -j MARK --set-mark $id
badvpn-tun2socks --tundev $tun --netif-ipaddr 169.254.1.2 --netif-netmask 255.255.255.252 --socks-server-addr $socks_server

iptables -t mangle -D PREROUTING -i wlp7s0 -p tcp -j MARK --set-mark $id
ip route del default via 169.254.1.2 table $id
ip rule del from fwmark $id lookup $id
ip tuntap del dev $tun mode tun

echo "TUN: $tun"
