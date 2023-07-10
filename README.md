# PIPS (Speaking Clock)
A pips and speaking clock emulator for Python using espeak and pysine on Linux

Tip: Use an NTP server to sync your computer with the correct time

### How to sync a watch or clock:
To sync an analogue time device, hold the device from ticking when the second hand reaches 12 or 0. Set the mintue hand accordingly as spoken on the :30 second time signal of the speaking clock. Wait for the :45 signal and on the long stroke set the time device to start ticking again.

Launch:
```
python3 -m pips --type=clock
```

- :00 On the first second a long stroke signals to start of the minute
- :15 The current minute will be announced
- :30 The next minute will be announced
- :45 The time signal will begin

### Available pip signatures for pips.play():
- uk, gts (The original pip signature)
- New Zealand (nz)
- Ireland (ire)
- United States (usa)
- Japan (jap)
- Australia (aus)
- Italy (ita)
- Germany (ger)
- India (ind)
- China (chi)
- Hong Kong (hk)
- Isreal (isr)
- Romania (rom)
- Slovakia (slo)


## Install
```
$ mkdir -p ~/git && cd ~/git
$ git clone https://github.com/duracell80/pips.git
$ cd pips && chmod +x *.sh

$ ./install-deb.sh
$ python3 -m pip install .
```

## ALSA Buffer Underrun
Sometimes the audio can be choppy and messages from ALSA complain of buffer issues, likely from how short the pips are.
```
$ sudo nano /etc/pulse/daemon.conf

uncomment and change these lines to:
default-fragments = 5
default-fragment-size-msec = 8
```

## Usage - On command line
```
python3 -m pips --type=pips --lang=jap
python3 -m pips --type=clock

python3 -m pips --type=clock --loops=10 --lang=en-sc --message="On the last stroke the time will be"
```

## Usage - In scripts
```
import time, pips

pips.play("gts") # Greenwhich Time Signal
pips.play("jap") # Japan

# Speaking Clock ...
Params: 
- language (espeak --help), 
- message prepend,  
- number of loops (0 infinite), 
- False = use python module, True = use command line call

pips.speak_clock("en", "On the long stroke the time will be", 100, False)
```

## ToDo:
- Allow script to run seconds ahead of actual time to account for when broadcasting digitally
- Look at ways of cleaning up choppy audio (buffer underun)

https://en.wikipedia.org/wiki/Greenwich_Time_Signal
