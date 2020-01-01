def store_raw_images(img):
    try:
        print(i)
        img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
        height, width = img.shape[:2]
        max_height = 100
        max_width = 100
        scaling_factor = max_width / float(width)
        resized_image = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        height, width = img.shape[:2]
        cv2.imwrite("neg/"+str(pic_num)+".jpg",resized_image)
        pic_num += 1
            
    except Exception as e:
        print(str(e)) 

def create_pos_n_neg():
    for file_type in ['neg']:
        
        for img in os.listdir(file_type):

            if file_type == 'pos':
                line = file_type+'/'+img+' 1 0 0 50 50\n'
                with open('info.dat','a') as f:
                    f.write(line)
            elif file_type == 'neg':
                line = file_type+'/'+img+'\n'
                with open('bg.txt','a') as f:
                    f.write(line)