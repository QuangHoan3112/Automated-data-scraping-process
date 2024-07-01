import json

# Đường dẫn tới file JSON đã lưu
user_id = input("Nhập id người dùng: ")
input_file = f"tiktok_user_{user_id}_followings.json"

with open(input_file, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Lớp Following
class Following:
    def __init__(self, id, region, sec_uid, unique_id, nickname, signature, avatar, verified, secret,
                 aweme_count, follower_count, favoriting_count, total_favorited, ins_id,
                 youtube_channel_title, youtube_channel_id, twitter_name, twitter_id):
        self.id = id
        self.region = region
        self.sec_uid = sec_uid
        self.unique_id = unique_id
        self.nickname = nickname
        self.signature = signature
        self.avatar = avatar
        self.verified = verified
        self.secret = secret
        self.aweme_count = aweme_count
        self.follower_count = follower_count
        self.favoriting_count = favoriting_count
        self.total_favorited = total_favorited
        self.ins_id = ins_id
        self.youtube_channel_title = youtube_channel_title
        self.youtube_channel_id = youtube_channel_id
        self.twitter_name = twitter_name
        self.twitter_id = twitter_id

# Chuyển đổi dữ liệu JSON thành các đối tượng Python của lớp Following
followings = []
for following_data in data["data"]["followings"]:
    # Tạo một dictionary mới chỉ với các trường cần thiết
    filtered_data = {
        'id': following_data.get('id'),
        'region': following_data.get('region'),
        'sec_uid': following_data.get('sec_uid'),
        'unique_id': following_data.get('unique_id'),
        'nickname': following_data.get('nickname'),
        'signature': following_data.get('signature'),
        'avatar': following_data.get('avatar'),
        'verified': following_data.get('verified'),
        'secret': following_data.get('secret'),
        'aweme_count': following_data.get('aweme_count'),
        'follower_count': following_data.get('follower_count'),
        'favoriting_count': following_data.get('favoriting_count'),
        'total_favorited': following_data.get('total_favorited'),
        'ins_id': following_data.get('ins_id'),
        'youtube_channel_title': following_data.get('youtube_channel_title'),
        'youtube_channel_id': following_data.get('youtube_channel_id'),
        'twitter_name': following_data.get('twitter_name'),
        'twitter_id': following_data.get('twitter_id'),
    }
    
    # Khởi tạo đối tượng Following từ filtered_data
    following_obj = Following(**filtered_data)
    followings.append(following_obj)

# Duyệt qua danh sách followings và in ra các thuộc tính của từng đối tượng
for following in followings:
    print(f"ID: {following.id}")
    print(f"Nickname: {following.nickname}")
    print(f"Follower count: {following.follower_count}")
    print(f"Favoriting count: {following.favoriting_count}")
    print(f"Signature: {following.signature}")
    print(f"Avatar URL: {following.avatar}")
    print(f"Verified: {following.verified}")
    print(f"Secret: {following.secret}")
    print(f"Aweme count: {following.aweme_count}")
    print(f"Total favorited: {following.total_favorited}")
    print(f"Instagram ID: {following.ins_id}")
    print(f"YouTube channel title: {following.youtube_channel_title}")
    print(f"YouTube channel ID: {following.youtube_channel_id}")
    print(f"Twitter name: {following.twitter_name}")
    print(f"Twitter ID: {following.twitter_id}")
    print()

