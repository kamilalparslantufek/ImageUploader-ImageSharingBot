import glob
def get_path_list(dir):
    try:
        path_list = glob.glob(dir+'/*.*')           #gets all files inside folder
        return path_list
    except:
        return 0