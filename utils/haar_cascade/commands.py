#OpenCV create samples commands
#opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950
#opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec

#Training command
#opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 20 -h 20

