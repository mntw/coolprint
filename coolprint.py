#!/usr/bin/python
import sys, time, random, string, os, argparse, signal

def signal_handler(signal, frame):
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler) # catch SIGIN with signal_handler

def realtime(txt, t=0.02, nl=1):
    for i in range(len(txt)):
        sys.stdout.write('\r%s' % txt[0:i+1])
        sys.stdout.flush()
        time.sleep(t)
    if nl:  print ''

def cyphering(txt, n=50, t=0.02, nl=1):
    outstr = txt[:]
    swaping = [random.choice(range(10, n)) for i in txt] 
    while swaping != (len(txt) * [0]):
        for i in range(len(outstr)):
            if swaping[i] > 0:
                outstr = list(outstr)
                outstr[i] = random.choice(string.printable[:-6])
                outstr = ''.join(outstr)
                swaping[i] -= 1
            elif swaping[i] == 0:
                outstr = list(outstr)
                outstr[i] = txt[i] 
                outstr = ''.join(outstr)
        sys.stdout.write('\r%s' % outstr)
        sys.stdout.flush()
        time.sleep(t)
    sys.stdout.write('\r%s' % txt)
    sys.stdout.flush()
    if nl:  print ''


if __name__ == "__main__":
    parser = argparse.ArgumentParser() # creating key-parser object
    parser.add_argument("-c", "--cypher", help="cypher mode printing", action="store_true")
    parser.add_argument("-r", "--realtime", help="real time mode printing", action="store_true")
    parser.add_argument("-t", "--time", type=float, help="specify time of printing", default=0.03)
    args = parser.parse_args() 

    Time = args.time
    func = realtime
    if args.cypher: func = cyphering
    elif args.realtime: func = realtime

    for i in sys.stdin:
        func(i[:-1], t=Time)
