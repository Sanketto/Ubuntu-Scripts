#!/bin/bash
nmcli connection add type wifi con-name "KPIT-AD-USER" ssid "KPIT-AD-USER"
nmcli c modify KPIT-AD-USER 802-1x.eap peap 802-1x.identity $user  802-1x.phase2-auth mschapv2
nmcli con modify KPIT-AD-USER wifi-sec.key-mgmt wpa-eap
nmcli con up KPIT-AD-USER