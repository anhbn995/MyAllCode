import os
import subprocess
from tqdm import tqdm
# subprocess.call(["ls", "-l"])
def create_list_id(path):
    list_id = []
    for file in os.listdir(path):
        if file.endswith(".tif"):
            # list_id.append(os.path.join(path,file))
            list_id.append(file[:-4])
    return list_id

if __name__ == "__main__":
    # old_time = r"/home/skymap/public/data_change_detection/202112_1"
    # new_time = r"/home/skymap/public/data_change_detection/trainslate_20220803_out"
    # stacked_dir = r"/home/skymap/big_data/stacked"
    # list_id = create_list_id(old_time)
    # if not os.path.exists(stacked_dir):
    #     os.makedirs(stacked_dir) 
    # for image_id in tqdm(list_id,total=len(list_id)):
        # inpath1 = os.path.join(old_time,image_id+".tif")
        # inpath2 = os.path.join(new_time,image_id+".tif")
        # outpath = os.path.join(stacked_dir,image_id+".tif")
        # subprocess.call(['gdal_merge.py',"-separate",'-of','gtiff',"-ot","Byte","-co", "COMPRESS=LZW","-o",outpath,inpath1,inpath2])
        
    inpath1 = r"/home/skm/SKM16/Data/ThaiLandChangeDetection/image-uint8/20210601.tif"
    inpath2 = r"/home/skm/SKM16/Data/ThaiLandChangeDetection/image-uint8/20220207.tif"
    outpath = r"/home/skm/SKM16/Data/ThaiLandChangeDetection/image-uint8/stack.tif"
    subprocess.call(['gdal_merge.py',"-separate",'-of','gtiff',"-ot","Byte","-co", "COMPRESS=LZW","-o",outpath,inpath1,inpath2])