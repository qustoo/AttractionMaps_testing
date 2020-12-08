#!/bin/bash

varservice='attractionmaps.service'
patchto='/etc/systemd/system'
sudo systemctl disable $varservice
sudo systemctl stop $varservice
sudo rm -rf $patchto/$varservice
sudo systemctl daemon-reload 
