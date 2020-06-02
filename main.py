import os
import imgurpython
import pandas as pd
from src.authimgur import auth_imgur
from src.getimages import get_path_list
from src.imageuploader import uploadimages


def run():
    #create csv list or read it
    try:
        url_list = pd.read_csv("url_list.csv", index_col=0)
    except:
        url_list = pd.DataFrame(columns=['title', 'url'])
    #path list
    dir = "C:\Docs\pics"            #directory where all my pics are in
    path_list = get_path_list(dir)  #gets us path list
    if path_list == 0:
        print('Error 0 : File Reading Error')
        return 0
    ##auth
    client_id = '2ecc2285f234620'
    client_secret = '3bea3bee9abe41592cd40233ec974b523715ebf8'
    client = auth_imgur(client_id,client_secret)
    #upload
    new_url_list = uploadimages(path_list,client,url_list)
    #save uploaded list
    url_list_2 = pd.DataFrame(new_url_list,columns=['title', 'url'])
    print(url_list_2)
    url_list = pd.concat([url_list,url_list_2], ignore_index=True)

    url_list.to_csv("url_list.csv")
    
if __name__ == "__main__":
    run()