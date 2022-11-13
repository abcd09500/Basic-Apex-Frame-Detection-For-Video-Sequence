import cv2
import os
import numpy as np
import re
import pandas as pd


read_path = 'E:/Ddisk0801/SMIC/SMIC_all_raw/SMIC_all_raw'

SMIC_NIR_excel_data = pd.read_excel("E:/Ddisk0801/SMIC/SMIC_all_raw/SMIC_all_raw/NIR/SMIC-NIR-E_annotation.xlsx"
                                    ,usecols=["Subject", "Filename", "OnsetF NIR", "ApexF NIR", "Emotion"])
SMIC_NIR_excel_data_array = np.array(SMIC_NIR_excel_data)


tmp =[]

for i in range(len(SMIC_NIR_excel_data_array)):
    Subject=str(SMIC_NIR_excel_data_array[i,0])
    Filename=SMIC_NIR_excel_data_array[i,1]
    OnsetFrame=str(SMIC_NIR_excel_data_array[i,2])
    Emotion = SMIC_NIR_excel_data_array[i,4]

    if(len(OnsetFrame)==4):
        OnsetFrame = "0" + OnsetFrame

    # 数据集的根目录
    onset_path = 'E:/Ddisk0801/SMIC/SMIC_all_raw/SMIC_all_raw/NIR/' + 's' + Subject + '/micro/' + Emotion +'/' + Filename
    #print(onset_path)
    # 对所有文件排序
    lists = sorted(os.listdir(onset_path))
    #print(lists)
    # 第一帧
    firstFrame = []
    # 第二帧
    secondFrame = []

    ith_frame_index = 1
    ith_frame_store = 0
    maximum_diff = []
    current_diff = []
    foreground1 = []
    max_frame =[]
    max_frame1 =[]
    s = (0,0,0)
    max =np.zeros(s)
    count = 1
    foreground_list = []
    for list in lists:
        
        y =  np.array(len(lists),dtype=int) #建立一個內容為0 長度為100的整數陣列
        fullfilename = []
        path = os.path.join(onset_path, list)
        get_path = path.split('/')[-1]
        get_path = re.sub('.bmp','',get_path)
        fullfilename = re.sub('image','',get_path)
       
        
        # 当前帧
        firstFrame = cv2.imread('E:/Ddisk0801/SMIC/SMIC_all_raw/SMIC_all_raw/NIR/' + 's' + Subject + '/micro/' + Emotion +'/' + Filename + '/' + OnsetFrame + '.bmp')
        print('E:/Ddisk0801/SMIC/SMIC_all_raw/SMIC_all_raw/NIR/' + 's' + Subject + '/micro/' + Emotion +'/' + Filename + '/' + OnsetFrame + '.bmp')
        a = str(int(OnsetFrame) + count)
        if(len(a)==4):
            a = "0" + a
        secondFrame = cv2.imread('E:/Ddisk0801/SMIC/SMIC_all_raw/SMIC_all_raw/NIR/' + 's' + Subject + '/micro/' + Emotion +'/' + Filename + '/' + a + '.bmp')
        print('E:/Ddisk0801/SMIC/SMIC_all_raw/SMIC_all_raw/NIR/' + 's' + Subject + '/micro/' + Emotion +'/' + Filename + '/'  + a + '.bmp')
        count = count +1
        if (count>=len(lists)):
            break
        
        
        foreground = cv2.absdiff(firstFrame,secondFrame)

        if foreground.sum() > max.sum():
           max = foreground.sum() 
           ith_frame_store = ith_frame_index

        ith_frame_index = ith_frame_index + 1
        cv2.waitKey(30)
       
    onset = int(OnsetFrame) + ith_frame_store

    print('\n--------------------')
    print('Onset: '+ OnsetFrame)
    tmp.append(str(onset))
    print("第" + str(i+1) + "筆apex:" + str(onset))
    print('--------------------')
   
df = pd.DataFrame(tmp,columns=['ApexF'])
df.to_excel('C:/Users/BiBi/Desktop/SMIC_detect_apex/SMIC-NIR-E_apex.xlsx', sheet_name='NIR',index =False)
print('SMIC-NIR儲存完畢!')