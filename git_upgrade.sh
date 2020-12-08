#!/bin/bash

varservice='attractionmaps.service'
sudo systemctl disable $varservice
sudo systemctl stop $varservice
git pull
sudo systemctl enable $varservice
sudo systemctl start $varservice