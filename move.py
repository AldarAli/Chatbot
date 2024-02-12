''' 
import shutil
import os

source_folder = '/home/kali-0101/Desktop/Chatbot/www.thinkmind.org/articles/extracted_text_articles'
target_folder = '/home/kali-0101/Desktop/Chatbot/www.thinkmind.org/cover+articles_matchs'

files = os.listdir(source_folder)
for file in files:
    if file.endswith(".html"):
        shutil.move(os.path.join(source_folder, file), target_folder)
        
'''

import shutil
import os

# list of file names to be moved
filenames = ['sec_v12_n12_2019_8.txt', 'cyber_2018_7_30_88020.txt', 'geoprocessing_2020_1_50_30053.txt',
             'geoprocessing_2019_2_30_30063.txt', 'sotics_2015_4_40_60080.txt', 'geoprocessing_2011_2_10_30030.txt',
             'securware_2019_5_10_30072.txt', 'cyber_2023_1_30_80029.txt', 'sysmea_v5_n34_2012_3.txt',
             'prediction_solutions_2023_1_10_30002.txt', 'vehicular_2018_5_20_38002.txt',
             'geoprocessing_2015_1_20_30079.txt', 'icsea_2023_1_30_10022.txt', 'intelli_2023_1_40_60014.txt',
             'dbkda_2017_2_20_50020.txt', 'icqnm_2020_1_10_60025.txt', 'achi_2016_20_20_20279.txt',
             'soft_v15_n34_2022_2.txt', 'geoprocessing_2013_1_10_30134.txt', 'sec_v15_n34_2022_8.txt']

# source and destination folders
source_folder = '/home/kali-0101/Desktop/Chatbot/www.thinkmind.org/articles/extracted_text_articles'
destination_folder = '/home/kali-0101/Desktop/Chatbot/www.thinkmind.org/cover+articles_matchs'

# move files
for filename in filenames:
    shutil.move(os.path.join(source_folder, filename), os.path.join(destination_folder, filename))
