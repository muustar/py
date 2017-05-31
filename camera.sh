#!/bin/bash
# pin kiosztás ezen a linken
# https://projects.drogon.net/raspberry-pi/wiringpi/pins/
#
# Feco
#
allapot=$(gpio read 1)
if [ "$allapot" = 1 ]; then
	echo "ki volt kapcsolva, ezert bekapcsoltam"
	python /home/pi/nfs-malna/py/relay_be.py
else
	echo "be volt kapcsolva"
fi

DATE=$(date +"%Y-%m-%d_%H%M%S")

#fswebcam -r 800x600 --no-banner /home/pi/grass/$DATE.jpg
sudo -u pi fswebcam -r 800x600 --title "Macskafű" --top-banner --timestamp "%Y.%m.%d. %H:%M:%S" /home/pi/nfs-malna/GrassProject/InTimePictures/$DATE.jpg
cp -f /home/pi/nfs-malna/GrassProject/InTimePictures/$DATE.jpg /home/pi/nfs-malna/www/ki.jpg
if [ "$allapot" = 1 ]; then
	echo "ki volt kapcsolva eredetileg, ezert kikapcsoltam"
	python /home/pi/nfs-malna/py/relay_ki.py
else
	echo "be volt kapcsolva, ezert nem kapcsoltam ki"
fi
