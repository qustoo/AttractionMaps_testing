#!/bin/bash

varservice='attractionmaps.service'
patchto='/etc/systemd/system'
#patchto='.'


ADMIN_ID=''
BOT_TOKEN=''
ip='127.0.0.1'
qiwi=''
qiwi_public_key=''
wallet=''
PGUSER=''
PGPASSWORD=''

. ./.env

echo 'Change ADMIN_ID? (y/n) Current ID is' $ADMIN_ID
read change
if [[ "$change" == y* ]]
then
  echo 'Enter new ADMIN_ID:'
  read ADMIN_ID
  echo 'ADMIN_ID changed successfully'
fi

echo 'Change BOT_TOKEN? (y/n) Current Token is' $BOT_TOKEN
read change
if [[ "$change" == y* ]]
then
  echo 'Enter new BOT_TOKEN:'
  read BOT_TOKEN
  echo 'BOT_TOKEN changed successfully'
fi

echo 'Change ip? (y/n) Current ip is' "$ip"
read change
if [[ "$change" == y* ]]
then
  echo 'Enter new IP:'
  read ip
  echo 'ip changed successfully'
fi

echo 'Change qiwi key? (y/n) Current qiwi key is' "$qiwi"
read change
if [[ "$change" == y* ]]
then
  echo 'Enter new QIWI key:'
  read qiwi
  echo 'qiwi key changed successfully'
fi

echo 'Change PUBLIC qiwi key? (y/n) Current PUBLIC qiwi key is' "$qiwi_public_key"
read change
if [[ "$change" == y* ]]
then
  echo 'Enter new QIWI PUBLIC key:'
  read qiwi_public_key
  echo 'qiwi PUBLIC key changed successfully'
fi

echo 'Change qiwi wallet? (y/n) Current qiwi wallet is' "$wallet"
read change
if [[ "$change" == y* ]]
then
  echo 'Enter new QIWI wallet:'
  read wallet
  echo 'qiwi wallet changed successfully'
fi

echo  'Change PostgreSQL user? (y/n) Current user is' "$PGUSER"
read change
if [[ "$change" == y* ]]
then
  echo "Enter new PostgreSQL's user:"
  read PGUSER
  echo "PostgreSQL's user changed successfully"
fi

echo  'Change PostgreSQL password? (y/n) Current user is' "$PGPASSWORD"
read change
if [[ "$change" == y* ]]
then
  echo "Enter new PostgreSQL's password:"
  read PGPASSWORD
  echo "PostgreSQL's password changed successfully"
fi



rm -rf ./.env
touch ./.env
{
  echo 'ADMIN_ID='$ADMIN_ID'
BOT_TOKEN='$BOT_TOKEN'
ip='$ip'
qiwi='$qiwi'
qiwi_public_key='$qiwi_public_key'
wallet='$wallet'
PGUSER='$PGUSER'
PGPASSWORD='$PGPASSWORD
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

