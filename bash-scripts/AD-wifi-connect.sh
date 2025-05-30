#!/bin/bash
function run_command(){
    local display=":$(ls /tmp/.X11-unix/* | sed 's#/tmp/.X11-unix/X##' | head -n 1)"
    local user=$(who | grep '('$display')' | awk '{print $1}' | head -n 1)
    local uid=$(id -u $user)
    sudo -u $user DISPLAY=$display DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$uid/bus $1
}

nmcli connection delete KPIT-AD-USER
if [ "$USERNAME" = "kpit" ]; then
exit 0
fi
run_command "nmcli connection add type wifi con-name "KPIT-AD-USER" ssid "KPIT-AD-USER""
run_command "nmcli c modify KPIT-AD-USER 802-1x.eap peap 802-1x.identity $user  802-1x.phase2-auth mschapv2"
run_command "nmcli con modify KPIT-AD-USER wifi-sec.key-mgmt wpa-eap"
run_command "nmcli con up KPIT-AD-USER"