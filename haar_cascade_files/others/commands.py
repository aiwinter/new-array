#OpenCV create samples commands
#
opencv_createsamples -img pos/98.jpg -bg bg.txt -info info.lst -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950 -pngoutput info

opencv_createsamples \
-bg neg/bg.txt \
-info pos/info.dat \
-num 128 -maxxangle 0.0 -maxyangle 0.0 \
-maxzangle 0.3 -bgcolor 255 -bgthresh 8 \
-w 48 -h 48

#
opencv_createsamples -info positives.txt -num 1950 -w 20 -h 20 -vec positives.vec

opencv_traincascade -data outputDirectory \
-vec cropped.vec \
-bg negativeImageDirectory/negatives.txt \
-numPos 1000 -numNeg 600 -numStages 20 \
-precalcValBufSize 1024 -precalcIdxBufSize 1024 \
-featureType HAAR \
-minHitRate 0.995 -maxFalseAlarmRate 0.5 \
-w 48 -h 48

opencv_createsamples -info positives.txt -bg ../neg/bg.txt -vec cropped_small.vec -num 2000

opencv_traincascade -data smaller  -vec vec/array.vec  -bg bg.txt  -numPos 18500 -numNeg 1200 -numStages 20  -precalcValBufSize 1024 -precalcIdxBufSize 1024  -featureType HAAR -mode ALL  -minHitRate 0.999 -maxFalseAlarmRate 0.5

#Training command
#opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20

../neg/bg.txt



