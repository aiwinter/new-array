#OpenCV create samples commands
#3437 1145

opencv_createsamples -img pos/98.jpg -bg bg.txt -info info.lst -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950 -pngoutput info

opencv_createsamples \
-bg neg/bg.txt \
-info pos/info.dat \
-num 128 -maxxangle 0.0 -maxyangle 0.0 \
-maxzangle 0.3 -bgcolor 255 -bgthresh 8 \
-w 48 -h 48

perl createsamples.pl positives.txt negatives.txt samples 1500 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 20 -h 20"

#
opencv_createsamples -info positives.txt -num 1950 -w 20 -h 20 -vec positives.vec

opencv_traincascade -data cascade/ -vec vec/pos.vec -bg bg.txt -nstages 20 -nsplits 2 -minhitrate 0.999 -maxfalsealarm 0.5 -npos 3437 -nneg 1145 -w 10 -h 10 -mode ALL

opencv_traincascade -data classifier -vec samples.vec -bg negatives.txt\
-numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000\
-numNeg 600 -w 80 -h 40 -mode ALL -precalcValBufSize 1024\
-precalcIdxBufSize 1024

opencv_traincascade -data outputDirectory \
-vec cropped.vec \
-bg negativeImageDirectory/negatives.txt \
-numPos 1000 -numNeg 600 -numStages 20 \
-precalcValBufSize 1024 -precalcIdxBufSize 1024 \
-featureType HAAR \
-minHitRate 0.995 -maxFalseAlarmRate 0.5 \
-w 48 -h 48

opencv_createsamples -info info/pos.txt -bg bg.txt -vec vec/pos.vec -w 10 -h 10

opencv_traincascade -data cascade -vec vec/pos.vec -bg bg.txt -numPos 3437 -numNeg 1145 -numStages 10 -featureType HAAR -mode ALL -minHitRate 0.999 -maxFalseAlarmRate 0.955

#Training command
opencv_traincascade -data cascade -vec vec/pos.vec -bg bg.txt -numPos 3437 -numNeg 1145 -numStages 10 -w 10 -h 10 precalcValBufSize 1024 -precalcIdxBufSize 1024  -featureType HAAR -mode ALL  -minHitRate 0.999 -maxFalseAlarmRate 0.955

../neg/bg.txt


opencv_createsamples -img blank_200.jpg -bg ../bg.txt -info pos.txt -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950

 opencv_createsamples -img ../pos/full_200.jpg -bg ../bg.txt -info pos2.txt -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950

 opencv_traincascade -data cascade6 -vec vec/positives.vec -bg bg.txt -numPos 10000  -numNeg 1000 -numStages 10  -w 20 -h 20 precalcValBufSize 1024 -precalcIdxBufSize 1024  -featureType HAA
R -mode ALL  -minHitRate 0.999 -maxFalseAlarmRate 0.6 -weightTrimRate 0.95 -maxDepth 1

 opencv_traincascade -data cascade7 -vec vec/positives.vec -bg bg.txt -numPos 10  -numNeg 1000 -numStages 20  -w 20 -h 20 precalcValBufSize 1024 -precalcIdxBufSize 1024  -featureType HAA
R -mode ALL  -minHitRate 0.999 -maxFalseAlarmRate 0.6 -weightTrimRate 0.95 -maxDepth 1

 https://github.com/mrnugget/opencv-haar-classifier-training
 https://stackoverflow.com/questions/16058080/how-to-train-cascade-properly/29882896#29882896
 http://note.sonots.com/SciSoftware/haartraining.html
 https://stackoverflow.com/questions/10961763/haartraining-with-opencv-error/12271213#12271213
 https://stackoverflow.com/questions/10863560/haar-training-opencv-assertion-failed
 https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
 https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html
 http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html
 https://memememememememe.me/post/training-haar-cascades/
 https://code.google.com/archive/p/imageclipper/







