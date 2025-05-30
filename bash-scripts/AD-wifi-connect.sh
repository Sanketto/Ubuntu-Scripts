#!/bin/bash
display=":$(ls /tmp/.X11-unix/* | sed 's#/tmp/.X11-unix/X##' | head -n 1)"
user=$(who | grep '('$display')' | awk '{print $1}' | head -n 1)
uid=$(id -u $user)

nmcli connection delete KPIT-AD-USER
if [ "$USERNAME" = "kpit" ]; then
exit 0
fi
nmcli connection add type wifi con-name "KPIT-AD-USER" ssid "KPIT-AD-USER"
nmcli c modify KPIT-AD-USER 802-1x.eap peap 802-1x.identity $user  802-1x.phase2-auth mschapv2
nmcli con modify KPIT-AD-USER wifi-sec.key-mgmt wpa-eap
nmcli con up KPIT-AD-USER