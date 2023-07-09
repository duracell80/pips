# pips
A pips and speaking clock emulator for python using espeak on Linux

## Install
```
$ mkdir -p ~/git && cd ~/git
$ git clone https://github.com/duracell80/pips.git
$ cd pips && chmod +x *.sh

$ ./install-deb.sh
$ python3 -m pip install .
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
