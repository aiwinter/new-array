#! /bin/bash

i=1;
for filename in pos/*; do
	#echo "$i"
	#mkdir info"$i"
	opencv_createsamples -img "$filename" -num 10 -bg bg.txt -info info/pos"$i".txt -pngoutput /info -maxxangle 0.6 -maxyangle 0 -maxzangle 0.3 -maxidev 100 -bgcolor 256 -bgthresh 10 -w 20 -h 20
	#opencv_createsamples -img "$filename" -bg bg.txt -info pos "$i" .txt -pngoutput newpos -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950
	#opencv_createsamples -img "$filename" -num 10 -bg negatives.dat -vec samples.vec -maxxangle 0.6 -maxyangle 0 -maxzangle 0.3 -maxidev 100 -bgcolor 0 -bgthresh 0 -w 20 -h 20
 ##opencv_createsamples -img "$filename" -num 10 -bg negatives.dat -info test.dat -maxxangle 0.6 -maxyangle 0 -maxzangle 0.3 -maxidev 100 -bgcolor 0 -bgthresh 0
 let i++
done
