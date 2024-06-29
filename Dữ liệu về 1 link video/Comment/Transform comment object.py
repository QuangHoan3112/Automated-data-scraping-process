import json

class User:
    def __init__(self, user_data):
        self.id = user_data.get('id')
        self.region = user_data.get('region')
        self.sec_uid = user_data.get('sec_uid')
        self.unique_id = user_data.get('unique_id')
        self.nickname = user_data.get('nickname')
        self.signature = user_data.get('signature')
        self.avatar = user_data.get('avatar')
        self.verified = user_data.get('verified')
        self.secret = user_data.get('secret')
        self.aweme_count = user_data.get('aweme_count')
        self.follower_count = user_data.get('follower_count')
        self.favoriting_count = user_data.get('favoriting_count')
        self.total_favorited = user_data.get('total_favorited')
        self.ins_id = user_data.get('ins_id')
        self.youtube_channel_title = user_data.get('youtube_channel_title')
        self.youtube_channel_id = user_data.get('youtube_channel_id')
        self.twitter_name = user_data.get('twitter_name')
        self.twitter_id = user_data.get('twitter_id')

class Comment:
    def __init__(self, comment_data):
        self.id = comment_data.get('id')
        self.text = comment_data.get('text')
        self.create_time = comment_data.get('create_time')
        self.digg_count = comment_data.get('digg_count')
        self.reply_total = comment_data.get('reply_total')
        self.user = User(comment_data.get('user'))
        self.status = comment_data.get('status')

#Tạo json data
json_data = '''
{
  "code": 0,
  "msg": "success",
  "processed_time": 0.4721,
  "data": {
    "comments": [
      {
        "id": "7375528713884287774",
        "text": "❤️❤️❤️🌹🌹🌹",
        "create_time": 1717249118,
        "digg_count": 0,
        "reply_total": 0,
        "user": {
          "id": "7092951459327837226",
          "region": "VN",
          "sec_uid": "MS4wLjABAAAAjhF5vHrSdTPcbdfbK5HZL3A2buIo9k0LBGqXmPeKD0fIJ7YztYjiIo8HuscTcAYk",
          "unique_id": "jennydoan80",
          "nickname": "jennydoann",
          "signature": "",
          "avatar": "https://p77-va.tiktokcdn.com/tos-maliva-avt-0068/7216462459794620459~tplv-tiktokx-cropcenter-q:300:300:q75.jpeg?pack_by_platform=true&ps=124&s=COMMENT_LIST&sc=avatar&shcp=ff37627b&shp=30310797&t=1",
          "verified": false,
          "secret": false,
          "aweme_count": 0,
          "follower_count": 0,
          "favoriting_count": 0,
          "total_favorited": 0,
          "ins_id": "",
          "youtube_channel_title": "",
          "youtube_channel_id": "",
          "twitter_name": "",
          "twitter_id": ""
        },
        "status": 1
      },
      {
        "id": "7374699184400040709",
        "text": "Verry beautiful",
        "create_time": 1717055971,
        "digg_count": 1,
        "reply_total": 0,
        "user": {
          "id": "7279546462857364482",
          "region": "TW",
          "sec_uid": "MS4wLjABAAAA1ynB3Ns-SzfkBM2NwmRqgG63CRzxxPK_dlJCdCdEK82l6BEwjwCOyuH59yKbYa3F",
          "unique_id": "coitam86210",
          "nickname": "Quyhoang",
          "signature": "",
          "avatar": "https://p77-va.tiktokcdn.com/tos-maliva-avt-0068/abdad601db777f72f6c4fc0e526fe5fb~tplv-tiktokx-cropcenter-q:300:300:q75.jpeg?pack_by_platform=true&ps=124&s=COMMENT_LIST&sc=avatar&shcp=ff37627b&shp=30310797&t=1",
          "verified": false,
          "secret": false,
          "aweme_count": 0,
          "follower_count": 0,
          "favoriting_count": 0,
          "total_favorited": 0,
          "ins_id": "",
          "youtube_channel_title": "",
          "youtube_channel_id": "",
          "twitter_name": "",
          "twitter_id": ""
        },
        "status": 1
      }
    ],
    "total": 2549,
    "cursor": 10,
    "hasMore": true
  }
}
'''

# Chuyển đổi Json
data = json.loads(json_data)

# Tạo comment data
comments_data = data['data']['comments']
comments = [Comment(comment_data) for comment_data in comments_data]

# Truy cập dữ liệu
for comment in comments:
    print(f"Comment ID: {comment.id}")
    print(f"Text: {comment.text}")
    print(f"Create Time: {comment.create_time}")
    print(f"Digg Count: {comment.digg_count}")
    print(f"Reply Total: {comment.reply_total}")
    
    # Accessing user information
    print(f"User ID: {comment.user.id}")
    print(f"User Nickname: {comment.user.nickname}")
    print(f"User Region: {comment.user.region}")
    print(f"User Unique ID: {comment.user.unique_id}")
    print(f"User Signature: {comment.user.signature}")
    print(f"User Avatar URL: {comment.user.avatar}")
    print(f"User Verified: {comment.user.verified}")
    print(f"User Secret: {comment.user.secret}")
    print(f"User Aweme Count: {comment.user.aweme_count}")
    print(f"User Follower Count: {comment.user.follower_count}")
    print(f"User Favoriting Count: {comment.user.favoriting_count}")
    print(f"User Total Favorited: {comment.user.total_favorited}")
    print(f"User Instagram ID: {comment.user.ins_id}")
    print(f"User YouTube Channel Title: {comment.user.youtube_channel_title}")
    print(f"User YouTube Channel ID: {comment.user.youtube_channel_id}")
    print(f"User Twitter Name: {comment.user.twitter_name}")
    print(f"User Twitter ID: {comment.user.twitter_id}")
    
    print()

