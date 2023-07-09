# pips
Speaking Clock

## Install
mkdir -p ~/git
$ git clone https://github.com/duracell80/pips.git
$ cd pips && chmod +x *.sh

$ ./install-deb.sh
$ python3 -m pip install .

## Usage

import time, pips

pips.pips_play("gts") # Greenwhich Time Signal
time.sleep(10)
pips.pips_play("jap") # Japan

# Speaking Clock
# Params: language (espeak --help), message prepend,  number of loops (0 infinite), False = use python module, True = use command line call
pips.speak_clock("en", "On the long stroke the time will be")

