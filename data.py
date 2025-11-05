import requests as req
import json
 
def get_songs(query):
 
    result = req.get("https://saavn.sumit.co/api/search/songs",
                params={
                "query": query,
                "page": "0",
                "limit": "5"
                }
            )
 
    all_json = result.json()
    print(all_json)
 
    data = all_json['data']['results']
 
    with open("jsondata" , "w") as f:
        json.dump(data , f , indent=4)
        
        
    f.close()
    print("file saved !")
    
name = input("enter the song name:-")
get_songs(name)