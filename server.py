import requests
from flask import Flask, jsonify

BOT_TOKEN = "7916365451:AAFXYYMdoCEtUQnNQBbIE4we3TVHYXh1wa0"
CHANNEL_ID = "-1002269184924"

app = Flask(__name__)

def get_videos():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    response = requests.get(url).json()
    
    videos = []
    for update in response["result"]:
        if "channel_post" in update and "video" in update["channel_post"]:
            file_id = update["channel_post"]["video"]["file_id"]
            file_info_url = f"https://api.telegram.org/bot{BOT_TOKEN}/getFile?file_id={file_id}"
            file_info = requests.get(file_info_url).json()
            
            video_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info['result']['file_path']}"
            videos.append(video_url)
    
    return videos

@app.route("/get_videos", methods=["GET"])
def fetch_videos():
    return jsonify(get_videos())

if __name__ == "__main__":
    app.run(debug=True)
