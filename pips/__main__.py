#Script to launch pips from the command line.
#Type python -m pips

import argparse

try:
    from pips import *
except:
    from . import *


def main():
	a_lang = "en"

	parser = argparse.ArgumentParser(description='Optional app description')

	parser.add_argument('--type', type=str, default='pips', help='Type of operation, pips or clock')
	parser.add_argument('--lang', type=str, default='en', help='Language of clock, see espeak --help or type of pip eg bra for Brazil')
	parser.add_argument('--message', type=str, default='On the long stroke the time will be', help='Customize the begining of the speaking clock time signal')
	parser.add_argument('--loops', type=int, default=0, help='Number of times to loop the time signal or pips (0 = infinitely)')

	args = parser.parse_args()

	try:
		a_type = str(args.type)
	except:
		a_type = "pips"

	try:
		a_lang = str(args.lang)
	except:
		a_lang = "en"

	a_message = str(args.message)

	try:
		a_loops = int(args.a_loops)
	except:
		a_loops = 0


	if str(args.type.lower()) == "pips":
		pips.play(str(a_lang))
		return

	if str(args.type.lower()) == "alarm":
		pips.alarm()
		return


	if str(args.type.lower()) == "clock":
		pips.speak_clock(str(a_lang), str(a_message), int(a_loops), False)


if __name__ == "__main__":
	main()
