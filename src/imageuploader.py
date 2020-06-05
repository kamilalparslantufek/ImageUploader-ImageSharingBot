import os
import imgurpython
import imgurpython.helpers.error
import pandas as pd

def uploadimages(path_list,client,csv_list):
    """Uploads images to imgur.

    Arguments:
        path_list {list} -- [List of files at directory.]
        client {ImgurClient} -- [ImgurClient we get from authentication.]
        csv_list {list} -- [List of uploaded pictures.]
    """
    #we create a dataframe to keep our imgur links
    url_list = []
  # for every image in path list
    iterator = 1
    try:
        for image in path_list:
            title = str(os.path.basename(image))[:-4]
            if csv_list[csv_list["title"]== title].empty == True:
                config = {
                    'title': title
                }
                img = client.upload_from_path(image, config = config)   
                #upload as title and upload returns us link of url
                #print("title: " + title + " link: " + img['link'] + "\t\t\t" + str(iterator) + "/50")
                print("title:{title}, link:{link} \t\t\t {iterator}/50".format(title=title, link=img['link'], iterator=str(iterator)))
                #we return list to main so we can save it    
                url_list.append([title, img['link']])
                iterator = iterator + 1
            else:
                continue
    except imgurpython.helpers.error.ImgurClientRateLimitError:
        print("err1")
        return url_list
    except Exception as e:
        print(e)
        return url_list
        

    return url_list
   