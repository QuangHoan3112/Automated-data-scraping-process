import json

# Định nghĩa lớp User
class User:
    def __init__(self, data):
        self.id = data.get('id', None)
        self.region = data.get('region', None)
        self.sec_uid = data.get('sec_uid', None)
        self.unique_id = data.get('unique_id', None)
        self.nickname = data.get('nickname', None)
        self.signature = data.get('signature', None)
        self.avatar = data.get('avatar', None)
        self.verified = data.get('verified', None)
        self.secret = data.get('secret', None)
        self.aweme_count = data.get('aweme_count', None)
        self.follower_count = data.get('follower_count', None)
        self.favoriting_count = data.get('favoriting_count', None)
        self.total_favorited = data.get('total_favorited', None)
        self.ins_id = data.get('ins_id', None)
        self.youtube_channel_title = data.get('youtube_channel_title', None)
        self.youtube_channel_id = data.get('youtube_channel_id', None)
        self.twitter_name = data.get('twitter_name', None)
        self.twitter_id = data.get('twitter_id', None)

# Định nghĩa lớp Comment
class Comment:
    def __init__(self, data):
        self.id = data.get('id', None)
        self.text = data.get('text', None)
        self.create_time = data.get('create_time', None)
        self.digg_count = data.get('digg_count', None)
        self.reply_total = data.get('reply_total', None)
        self.user = User(data.get('user', {}))
        self.status = data.get('status', None)

# Tên file output
video_id = input("Nhập ID Video: ")
output_file = f"tiktok_comments_{video_id}_results.json"

# Đọc dữ liệu từ file JSON và xử lý
with open(output_file, 'r', encoding='utf-8') as file:
    json_data = file.read()

# Chuyển đổi JSON thành dữ liệu Python
data = json.loads(json_data)

# Lấy danh sách các comment từ dữ liệu
comments_data = data['data'].get('comments', [])

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
    print(f"User Aweme
