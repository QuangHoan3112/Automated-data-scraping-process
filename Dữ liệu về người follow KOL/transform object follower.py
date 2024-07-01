import json

class Follower:
    def __init__(self, id, region, sec_uid, unique_id, nickname, signature, avatar, verified, secret, aweme_count, follower_count, favoriting_count, total_favorited, ins_id, youtube_channel_title, youtube_channel_id, twitter_name, twitter_id):
        self.id = id
        self.region = region
        self.sec_uid = sec_uid
        self.unique_id = unique_id
        self.nickname = nickname
        self.signature = signature
        self.avatar = avatar  # Ensure the 'avatar' field is correctly handled in JSON data
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

# Nhập ID người dùng từ người dùng
user_id = input("Nhập ID người dùng: ")

# Xây dựng tên file dựa trên user_id
output_file = f"tiktok_user_{user_id}_followers.json"

# Đọc dữ liệu từ file JSON và xử lý
with open(output_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

followers_data = data["data"]["followers"]

# In ra thông tin của từng người theo dõi
for follower_data in followers_data:
    follower = Follower(
        id=follower_data.get('id'),
        region=follower_data.get('region'),
        sec_uid=follower_data.get('secUid'),
        unique_id=follower_data.get('uniqueId'),
        nickname=follower_data.get('nickname'),
        signature=follower_data.get('signature'),
        avatar=follower_data.get('avatar'),
        verified=follower_data.get('verified'),
        secret=follower_data.get('secret'),
        aweme_count=follower_data.get('awemeCount'),
        follower_count=follower_data.get('followerCount'),
        favoriting_count=follower_data.get('favoritingCount'),
        total_favorited=follower_data.get('totalFavorited'),
        ins_id=follower_data.get('insId'),
        youtube_channel_title=follower_data.get('youtubeChannelTitle'),
        youtube_channel_id=follower_data.get('youtubeChannelId'),
        twitter_name=follower_data.get('twitterName'),
        twitter_id=follower_data.get('twitterId')
    )
    print(f"Follower {follower.unique_id}:")
    print(f" - Region: {follower.region}")
    print(f" - Sec UID: {follower.sec_uid}")
    print(f" - Unique ID: {follower.unique_id}")
    print(f" - Nickname: {follower.nickname}")
    print(f" - Signature: {follower.signature}")
    print(f" - Avatar: {follower.avatar}")
    print(f" - Verified: {follower.verified}")
    print(f" - Secret: {follower.secret}")
    print(f" - Aweme count: {follower.aweme_count}")
    print(f" - Follower count: {follower.follower_count}")
    print(f" - Favoriting count: {follower.favoriting_count}")
    print(f" - Total favorited: {follower.total_favorited}")
    print(f" - Instagram ID: {follower.ins_id}")
    print(f" - YouTube channel title: {follower.youtube_channel_title}")
    print(f" - YouTube channel ID: {follower.youtube_channel_id}")
    print(f" - Twitter name: {follower.twitter_name}")
    print(f" - Twitter ID: {follower.twitter_id}")
    print()

# In tổng số người theo dõi
print(f"Total followers: {data['data']['total']}")
