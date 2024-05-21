"""
 in this python code snippet, we sort files in a directory into different subdirectories
 based on the conference names in the file name.
 we specify the source directory where the files are located and the destination 
 directories where the files should be moved based on the prefix of the file name which 
 contain conference name it belog to.
 we then list all the files in the source directory and move the files 
 to the destination directories based on the prefix of the file name.
"""
import os
import shutil

# specify the source directory where the files are located.
source_directory = '***'

# specify the destination directories
destination_directories = {
    'articleid=access': 'data/ACCESS', 
    'articleid=accse': 'data/ACCSE',
    'articleid=achi': 'data/ACHI',
    'articleid=adaptive': 'data/ADAPTIVE',
    'articleid=advcomp': 'data/ADVCOMP',
    'articleid=afin': 'data/AFIN',
    'articleid=aict': 'data/AICT',
    'articleid=alldata': 'data/ALLDATA',
    'articleid=allsensors': 'data/ALLSENSORS',
    'articleid=ambient': 'data/AMBIENT',
    'articleid=ap2ps': 'data/AP2PC',
    'articleid=bionature': 'data/BIONATURE',
    'articleid=biotechno': 'data/BIOTECHNO',
    'articleid=braininfo': 'data/BRAININFO',
    'articleid=bustech': 'data/BUSTECH',
    'articleid=cenics': 'data/CENICS',
    'articleid=centric': 'data/CENTRIC',
    'articleid=cloud_computing': 'data/CLOUD_COMPUTING',
    'articleid=cocora': 'data/COCORA',
    'articleid=cognitive': 'data/COGNITIVE',
    'articleid=colla': 'data/COLLA',
    'articleid=computation_tools': 'data/COMPUTATION_TOOLS',
    'articleid=content': 'data/CONTENT',
    'articleid=coreta': 'data/CORETA',
    'articleid=ctrq': 'data/CTRQ',
    'articleid=cyber': 'data/CYBER',
    'articleid=cyberlaws': 'data/CYBERLAWS',
    'articleid=data_analytics': 'data/DATA_ANALYTICS',
    'articleid=dbkda': 'data/DBKDA',
    'articleid=depend': 'data/DEPEND',
    'articleid=digital': 'data/DIGITAL',
    'articleid=eknow': 'data/EKNOW',
    'articleid=elml': 'data/ELML',
    'articleid=emerging': 'data/EMERGING',
    'articleid=energy': 'data/ENERGY',
    'articleid=etelemed': 'data/ETELEMED',
    'articleid=fassi': 'data/FASSI',
    'articleid=future_computing': 'data/FUTURE_COMPUTING',
    'articleid=geoprocessing': 'data/GEOPROCESSING',
    'articleid=global_health': 'data/GLOBAL_HEALTH',
    'articleid=green': 'data/GREEN',
    'articleid=healthinfo': 'data/HEALTHINFO',
    'articleid=huso': 'data/HUSO',
    'articleid=iaria_congress': 'data/IARIA_CONGRESS',
    'articleid=icas': 'data/ICAS',
    'articleid=iccgi': 'data/ICCGI',
    'articleid=icds': 'data/ICDS',
    'articleid=icdt': 'data/ICDT',
    'articleid=icimp': 'data/ICIMP',
    'articleid=iciw': 'data/ICIW',
    'articleid=icn': 'data/ICN',
    'articleid=icns': 'data/ICNS',
    'articleid=icons': 'data/ICONS',
    'articleid=icqnm': 'data/ICQNM',
    'articleid=icsea': 'data/ICSEA',
    'articleid=icsnc': 'data/ICSNC',
    'articleid=icwmc': 'data/ICWMC',
    'articleid=immm': 'data/IMMM',
    'articleid=infocomp': 'data/INFOCOMP',
    'articleid=innov': 'data/INNOV',
    'articleid=intelli': 'data/INTELLI',
    'articleid=intensive': 'data/INTENSIVE',
    'articleid=internet': 'data/INTERNET',
    'articleid=mesh': 'data/MESH',
    'articleid=mmedia': 'data/MMEDIA',
    'articleid=mobility': 'data/MOBILITY',
    'articleid=modern_systems': 'data/MODERN_SYSTEMS',
    'articleid=mopas': 'data/MOPAS',
    'articleid=pandemics_analytics': 'data/PANDEMICS_ANALYTICS',
    'articleid=patterns': 'data/PATTERNS',
    'articleid=pesaro': 'data/PESARO',
    'articleid=prediction_solutions': 'data/PREDICTION_SOLUTIONS',
    'articleid=securware': 'data/SECURWARE',
    'articleid=semapro': 'data/SEMAPRO',
    'articleid=sensorcomm': 'data/SENSORCOMM',
    'articleid=sensordevices': 'data/SENSORDEVICES',
    'articleid=service_computation': 'data/SERVICE_COMPUTATION',
    'articleid=signal': 'data/SIGNAL',
    'articleid=simul': 'data/SIMUL',
    'articleid=smart': 'data/SMART',
    'articleid=smart_accessibility': 'data/SMART_ACCESSIBILITY',
    'articleid=society_trends': 'data/SOCIETY_TRENDS',
    'articleid=softeng': 'data/SOFTENG',
    'articleid=sotics': 'data/SOTICS',
    'articleid=spacomm': 'data/SPACOMM',
    'articleid=spwid': 'data/SPWID',
    'articleid=ubicomm': 'data/UBICOMM',
    'articleid=valid': 'data/VALID',
    'articleid=vehicular': 'data/VEHICULAR',
    'articleid=visual': 'data/VISUAL',
    'articleid=web': 'data/WEB',
    'articleid=intsys': 'data/JOURNALS/IntSys',
    'articleid=inttech': 'data/JOURNALS/IntTech',
    'articleid=lifsci': 'data/JOURNALS/LifSci',
    'articleid=netser': 'data/JOURNALS/NetSer',
    'articleid=sec': 'data/JOURNALS/Sec',
    'articleid=soft': 'data/JOURNALS/Soft',
    'articleid=sysmea': 'data/JOURNALS/SysMea',
    'articleid=tele': 'data/JOURNALS/Tele',
}

# list all the files in the source directory.
files = os.listdir(source_directory)

# move the files to the destination directories based on the prefix of the file name.
for file in files:
    for prefix, destination_directory in destination_directories.items():
        if file.startswith(prefix):
            source_file = os.path.join(source_directory, file)
            destination_file = os.path.join(destination_directory, file)

            # move the file
            shutil.move(source_file, destination_file)
            break  # break the loop if the file is moved to a destination directory.

print("Files moved successfully.")
