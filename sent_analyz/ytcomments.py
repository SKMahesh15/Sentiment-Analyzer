import googleapiclient.discovery
import googleapiclient.errors
import json 

class GetComments:
    def __init__(self, vid_id: str):
        self.vid_id = vid_id


    def comments(self):
        api_service_name = "youtube"
        api_version = "v3"
        DEVELOPER_KEY = "AIzaSyDwF7BGDSSRlh56HU05vBrh2MY1okV53yg"

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY)

        request = youtube.commentThreads().list(
            part="snippet",
            videoId=self.vid_id,
            maxResults=20
        )
        response = request.execute()
        response = response['items']
        comments_list = []

        for x in response:
            comments = x["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments_list.append(comments)
        
        return comments_list