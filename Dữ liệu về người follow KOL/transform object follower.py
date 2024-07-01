import json

# Đường dẫn đến file output
user_id = input("Nhập ID người dùng: ")
output_file = f"tiktok_user_{user_id}_followers.json"

# Đọc dữ liệu từ file JSON
with open(output_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Chuyển đổi dữ liệu JSON thành các đối tượng Python (sử dụng class Follower đã định nghĩa)
followers = [Follower(**follower_data) for follower_data in data["data"]["followers"]]

# In ra thông tin của một số người theo dõi đầu tiên
for follower in followers:
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

