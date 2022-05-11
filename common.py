import os
import cv2

emo = ['Anger','Contempt','Disgust','Fear','Happy','Sadness','Surprise']
datatset_folders = [ "/Users/poojaps/Desktop/project/CK+48/anger","/Users/poojaps/Desktop/project/CK+48/contempt",
           "/Users/poojaps/Desktop/project/CK+48/disgust","/Users/poojaps/Desktop/project/CK+48/fear",
           "/Users/poojaps/Desktop/project/CK+48/happy","/Users/poojaps/Desktop/project/CK+48/sadness",
           "/Users/poojaps/Desktop/project/CK+48/surprise" ]
viola_folder = ["/Users/poojaps/Desktop/project/afterviola/anger","/Users/poojaps/Desktop/project/afterviola/contempt",
            "/Users/poojaps/Desktop/project/afterviola/disgust","/Users/poojaps/Desktop/project/afterviola/fear",
            "/Users/poojaps/Desktop/project/afterviola/happy","/Users/poojaps/Desktop/project/afterviola/sadness",
            "/Users/poojaps/Desktop/project/afterviola/surprise" ]

fd_lbp = ["/Users/poojaps/Desktop/project/fd/afterlbp/anger","/Users/poojaps/Desktop/project/fd/afterlbp/contempt",
           "/Users/poojaps/Desktop/project/fd/afterlbp/disgust","/Users/poojaps/Desktop/project/fd/afterlbp/fear",
           "/Users/poojaps/Desktop/project/fd/afterlbp/happy","/Users/poojaps/Desktop/project/fd/afterlbp/sadness",
          "/Users/poojaps/Desktop/project/fd/afterlbp/surprise" ]

tp_folders = ["/Users/poojaps/Desktop/project/fd/afterlbp-tp/anger","/Users/poojaps/Desktop/project/fd/afterlbp-tp/contempt",
           "/Users/poojaps/Desktop/project/fd/afterlbp-tp/disgust","/Users/poojaps/Desktop/project/fd/afterlbp-tp/fear",
           "/Users/poojaps/Desktop/project/fd/afterlbp-tp/happy","/Users/poojaps/Desktop/project/fd/afterlbp-tp/sadness",
          "/Users/poojaps/Desktop/project/fd/afterlbp-tp/surprise" ]
fp_folders = ["/Users/poojaps/Desktop/project/fd/afterlbp-fp/anger","/Users/poojaps/Desktop/project/fd/afterlbp-fp/contempt",
           "/Users/poojaps/Desktop/project/fd/afterlbp-fp/disgust","/Users/poojaps/Desktop/project/fd/afterlbp-fp/fear",
           "/Users/poojaps/Desktop/project/fd/afterlbp-fp/happy","/Users/poojaps/Desktop/project/fd/afterlbp-fp/sadness",
          "/Users/poojaps/Desktop/project/fd/afterlbp-fp/surprise" ]

sd_lbp = ['/Users/poojaps/Desktop/project/sd/histogram/1.txt',
          '/Users/poojaps/Desktop/project/sd/histogram/2.txt',
          '/Users/poojaps/Desktop/project/sd/histogram/3.txt',
          '/Users/poojaps/Desktop/project/sd/histogram/4.txt',
          '/Users/poojaps/Desktop/project/sd/histogram/5.txt',
          '/Users/poojaps/Desktop/project/sd/histogram/6.txt',
          '/Users/poojaps/Desktop/project/sd/histogram/7.txt'
          ]
def load_images_from_folder(folder):
  images = []
  for filename in os.listdir(folder):
     if any([filename.endswith(x) for x in ['.jpeg', '.jpg','.png']]):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
  return images