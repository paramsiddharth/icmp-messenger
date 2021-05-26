# ICMP Messenger
An application to send and receive messages in the form of ICMP echo request payloads.

## Docker Quickstart
1.	Pull the image and create a network.
	``` bash
	docker pull paramsiddharth/icmp-messenger
	docker network create mynet
	```
2.	Create a receiver.
	``` bash
	docker run --rm -it --network mynet --name my-receiver paramsiddharth/icmp-messenger receiver
	```
	Note the IP address of the receiver.
3.	Start up a sender.
	``` bash
	docker run --rm -it --network mynet --name my-sender paramsiddharth/icmp-messenger sender
	```
	Enter the address of the receiver and send messages. The messages will appear in the receiver's console.

## Execution
Install the Python 3 dependencies (preferably in a virtual environment):
``` bash
pip install -r requirements.txt
```

Execute `sender.py` or `receiver.py` depending on what is desired.
``` bash
# Sender
python sender.py

# Receiver
python receiver.py
```

Inside Bash/MSYS2/Cygwin, `run.sh` may be executed for a more interactive startup. `run.sh` is the Docker container's intended entrypoint.

For the sender, enter the name or IP address of another machine on the network to start chatting.

For the receiver, a list of network addresses (on all interfaces) will be displayed.

## Execution (Docker)
Pull the image from Docker Hub.
``` bash
docker pull paramsiddharth/icmp-messenger
```

Create a network for the container(s).
``` bash
docker network create mynetwork
```

Start an attached container in that network.
``` bash
docker run --rm -it --network mynet --name my-app paramsiddharth/icmp-messenger # You may optionally pass command-line arguments "sender" or "receiver"
```

It will be able to communicate with the other containers in the same network.

## Development
Build the image using Docker.
``` bash
docker build -t paramsiddharth/icmp-messenger .
```

# Made with ❤ by [Param](https://www.paramsid.com).