#!/bin/bash
VIDEO=$(date +"napi_video_%Y-%m-%d")
KEPEK=$(date +"napi_kepek_%Y-%m-%d")


cd /home/pi/nfs-malna/GrassProject/InTimePictures
ls *.jpg > kepek.txt
mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:aspect=4/3:vbitrate=8000000 -vf scale=800:600 -o $VIDEO.avi -mf type=jpeg:fps=8 mf://@kepek.txt

tar -cf $KEPEK.tar *.jpg


avconv -i $VIDEO.avi -c:v libx264 -crf 19 -c:a libfdk_aac -b:a 192k -ac 2 $VIDEO.mp4
cp -f $VIDEO.mp4 /home/pi/nfs-malna/www/lol.mp4
rm -f /home/pi/nfs-malna/GrassProject/InTimePictures/*.jpg
rm -f /home/pi/nfs-malna/GrassProject/InTimePictures/*.txt
rm -f /home/pi/nfs-malna/GrassProject/InTimePictures/*.avi
mv /home/pi/nfs-malna/GrassProject/InTimePictures/$KEPEK.tar /home/pi/nfs-malna/GrassProject/FinishedVideos
mv /home/pi/nfs-malna/GrassProject/InTimePictures/$VIDEO.mp4 /home/pi/nfs-malna/GrassProject/FinishedVideos
