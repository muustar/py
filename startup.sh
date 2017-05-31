#!/bin/sh
#startup.sh
#ujraindítás után elinduló alkalmazások
python /mnt/nfs/py/relay_ki.py
python /mnt/nfs/py/mozgaserzekelo.py &>/dev/null
