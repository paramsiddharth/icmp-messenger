#!/bin/bash

# Just a script to make things easier :P
# Made with ❤ by Param.

echo 'ICMP Messenger'

param=$(echo "$1" | sed -e 's/\(.*\)/\L\1/')

if [ "$param" == "--help"  ]; then
	echo 'Usage: ./run.sh [sender/receiver]'
	exit
else
	python show_ips.py

	if [ "$param" != "sender"  ] && [ "$param" != "receiver"  ]; then
		echo 'I am a...'
		echo '1. Sender'
		echo '2. Receiver'
		echo
		echo -n '([1]/2): '
		read param
		param=$(echo $param | xargs)
		if [ "$param" = '2' ]; then
			param=receiver
		else
			param=sender
		fi
	fi
fi

if [ "$param" = "sender" ]; then
	python sender.py
else
	python receiver.py
fi
