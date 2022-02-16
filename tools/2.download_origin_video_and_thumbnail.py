import os
import re
import json
import requests

def download_file(url, local_filename):
    # local_filename = url.split('/')[1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename



with open("origin.json", mode="r", encoding="utf-8" ) as json_file:
    json_data = json.load(json_file)
    for data in json_data:
        filename = re.sub('[\r\n\t\\\/:*?"<>|]', '', data["created_at"] +"_"+ data["title"] + "_view" + str(data["view_count"]) + "_" + data["creator_name"])
        print(filename)
        # filename os path add "../cilps/"
        filename = os.path.join("../clips/", filename)
        if os.path.isfile(filename+".mp4") == False:
            download_file( data["download_url"], filename + ".mp4")
            download_file( data["thumbnail_url"], filename + ".jpg")
