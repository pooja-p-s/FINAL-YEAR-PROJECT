from common import *

def each_emo(filename):
    with open(filename, 'r') as file:
        all_file = file.read().strip()  #remove extra newlines (if any)
        all_file_list = all_file.split('\n')  #make list of lines
        final_data = [[float(each_num) for each_num in line.split()] for line in all_file_list]  # make list of list 
    return final_data


def create_data():
    temp = list()
    for i in range(0,7):
        temp = temp + each_emo(sd_lbp[i])
    print(len(temp))
create_data()
labels=[]
order=0
for folder in datatset_folders:
        images = load_images_from_folder(folder)
        for img in images:
            labels.append(emo[order])
        order = order+1
print(labels)