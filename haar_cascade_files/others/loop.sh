#!/bin/bash
i=1;
for filename in /pos/*.jpg; do
  opencv_createsamples -img ../pos/ "$filename" -bg ../bg.txt -info info "$i" .txt -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950 -pngoutput
  i++;
done