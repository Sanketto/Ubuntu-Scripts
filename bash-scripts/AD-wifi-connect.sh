#!/bin/bash
is_laptop=$(nmcli device wifi)
is_local_login=$(cut -d: -f1 /etc/passwd | grep -w "$USERNAME")
#don't execute this if loging as local user ot if its desktop
if [ -z "$is_laptop" ] || [ -n "$is_local_login" ]; then
exit 0
fi
function connect_wifi(){
    local display=":$(ls /tmp/.X11-unix/* | sed 's#/tmp/.X11-unix/X##' | head -n 1)"
    local user=$(who | grep '('$display')' | awk '{print $1}' | head -n 1)
    local uid=$(id -u $user)
    sudo -u $user DISPLAY=$display DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$uid/bus nmcli connection add type wifi con-name "KPIT-AD-USER" ssid "KPIT-AD-USER"
    sudo -u $user DISPLAY=$display DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$uid/bus nmcli con modify KPIT-AD-USER 802-1x.eap peap 802-1x.identity $user 802-1x.phase2-auth mschapv2
    sudo -u $user DISPLAY=$display DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$uid/bus nmcli con modify KPIT-AD-USER wifi-sec.key-mgmt wpa-eap
    sudo -u $user DISPLAY=$display DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$uid/bus nmcli con up KPIT-AD-USER
}

kpit_wifi_status=$(nmcli device | grep 'connected\s\+\KPIT-AD-USER')
other_wifi_status=$(nmcli device | grep 'wlp0s20f3\s\+\wifi\s\+\connected')
available_wifi_status=$(nmcli device wifi | grep KPIT-AD-USER)
echo $kpit_wifi_status
echo $other_wifi_status
echo $available_wifi_status

if [ -n "$kpit_wifi_status" ] || [ -n "$other_wifi_status" ] || ! [ -n "$available_wifi_status" ]; then
  echo "Wifi is already connected"
else
    nmcli connection delete KPIT-AD-USER
    echo "run script"
    connect_wifi
fi