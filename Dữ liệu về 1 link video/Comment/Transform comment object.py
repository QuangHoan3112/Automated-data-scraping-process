import json

# Định nghĩa lớp Comment
class Comment:
    def __init__(self, data):
        self.id = data['id']
        self.text = data['text']
        self.create_time = data['create_time']
        self.digg_count = data['digg_count']
        self.reply_total = data['reply_total']
        self.user = User(data['user'])
        self.status = data['status']

# Định nghĩa lớp User
class User:
    def __init__(self, data):
        self.id = data['id']
        self.region = data['region']
        self.sec_uid = data['sec_uid']
        self.unique_id = data['unique_id']
        self.nickname = data['nickname']
        self.signature = data['signature']
        self.avatar = data['avatar']
        self.verified = data['verified']
        self.secret = data['secret']
        self.aweme_count = data['aweme_count']
        self.follower_count = data['follower_count']
        self.favoriting_count = data['favoriting_count']
        self.total_favorited = data['total_favorited']
        self.ins_id = data['ins_id']
        self.youtube_channel_title = data['youtube_channel_title']
        self.youtube_channel_id = data['youtube_channel_id']
        self.twitter_name = data['twitter_name']
        self.twitter_id = data['twitter_id']

# Tên file output
video_id = input("Nhập ID Video: ")
output_file = f"tiktok_comments_{video_id}_results.json"

# Đọc dữ liệu từ file JSON và xử lý
with open(output_file, 'r', encoding='utf-8') as file:
    json_data = file.read()

# Chuyển đổi JSON thành dữ liệu Python
data = json.loads(json_data)

# Lấy danh sách các comment từ dữ liệu
comments_data = data['data']['comments']

# Tạo danh sách các đối tượng Comment từ dữ liệu
comments = [Comment(comment_data) for comment_data in comments_data]

# In ra thông tin từng comment và user tương ứng
for comment in comments:
    print(f"Comment ID: {comment.id}")
    print(f"Text: {comment.text}")
    print(f"Create Time: {comment.create_time}")
    print(f"Digg Count: {comment.digg_count}")
    print(f"Reply Total: {comment.reply_total}")
    
    # In thông tin của người dùng (user)
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
    
    print()

