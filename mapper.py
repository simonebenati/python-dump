import sys,webbrowser

sys.argv
addr = " ".join(sys.argv[1:])
if len(sys.argv) > 1:
    webbrowser.open('https://www.google.it/maps/place/'+str(addr))
else:
    webbrowser.open('https://www.google.it/maps/place/')
