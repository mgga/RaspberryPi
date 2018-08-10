# WS281 Control with the Pi

These are some beginner code snippets in python to teach you how to interact with a WS2812 strip of LEDs using python and a RaspberryPi

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Update your repos

```
sudo apt-get update
```
Install python and pip

```
sudo apt-get install python
sudo apt-get install python-pip
```

Install other dependencies

```
sudo apt-get install gcc make build-essential python-dev git scons swig
```

Disable the audio output (we need it to control the LEDs)
```
sudo nano /etc/modprobe.d/snd-blacklist.conf
```
and add the following line
```
blacklist snd_bcm2835
```

Furthermore we need to edit the configuration file
```
sudo nano /boot/config.txt
```
look for the line containing (use ctrl + W to search)
```
# Enable audio (loads snd_bcm2835)
dtparam=audio=on
```
change it to
```
# Enable audio (loads snd_bcm2835)
#dtparam=audio=on
```
now reboot
```
sudo reboot
```

### Installing

Download the rpi_ws281x submodule
```
git submodule update --init --recursive
```

We now need to compile it
```
cd rpi_ws281x/
sudo scons
```

Now go into the python folder
```
cd python
```

And now build and install the modules
```
sudo python setup.py build
sudo python setup.py install
```

## Authors
* **Jeremy Garff** - *WS2112 Library* - [jgarff](https://github.com/jgarff)
* **Miguel Almeida** - *Readme File* - [mgga](https://github.com/mgga)

See also the list of [contributors](https://github.com/mgga/RaspberryPi/contributors) who participated in this project.

## License

This project is licensed under a permissive License - see the [LICENSE.md](rpi_ws281x/LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* NEC for the time provided to accomplish this
* RaspberryPi foundation for making such a cool device