#!/bin/bash

varservice='attractionmaps.service'
patchto='/etc/systemd/system'
#patchto='.'


ADMIN_ID=''
BOT_TOKEN=''
ip='127.0.0.1'

. ./.env

echo 'Change ADMIN_ID? (y/n) Current ID is' $ADMIN_ID

read change
if [[ "$change" == y* ]]
then
  read ADMIN_ID
  echo 'ADMIN_ID changed succesfully'
fi

echo 'Change BOT_TOKEN? (y/n) Current Token is' $BOT_TOKEN

read change
if [[ "$change" == y* ]]
then
  read BOT_TOKEN
  echo 'BOT_TOKEN changed succesfully'
fi

echo 'Change ip? (y/n) Current ip is' "$ip"

read change
if [[ "$change" == y* ]]
then
  read ip
  echo 'ip changed succesfully'
fi

rm -rf ./.env
touch ./.env
{
  echo 'ADMIN_ID='$ADMIN_ID'
BOT_TOKEN='$BOT_TOKEN'
ip='$ip
} > ./.env

echo '(Re)create service?'

read change
if [[ "$change" == y* ]]
then
  if [ -e $patchto/$varservice ] 
  then
    sudo rm -rf $patchto/$varservice
  fi
  touch ./$varservice
{
  echo '[Unit]
Description=AttractionMaps_testing

[Service]
WorkingDirectory='$PWD'
ExecStart=python3 '$PWD'/app.py
Restart=always
User='$USER'

[Install]
WantedBy=multi-user.target'
} > ./$varservice
  sudo mv -f ./$varservice $patchto/$varservice
  echo 'Service created'
  sudo systemctl daemon-reload 
  sudo systemctl enable $varservice
  sudo systemctl start $varservice
  echo 'Service started'
fi

