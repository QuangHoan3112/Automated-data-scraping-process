import json

# Định nghĩa các lớp cho dữ liệu từ JSON
class Avatar:
    def __init__(self, uri, url_list, width, height):
        self.uri = uri
        self.url_list = url_list
        self.width = width
        self.height = height

class OriginalMusician:
    def __init__(self, digg_count, music_count, music_used_count):
        self.digg_count = digg_count
        self.music_count = music_count
        self.music_used_count = music_used_count

class UserInfo:
    def __init__(self, avatar_168x168, avatar_300x300, avatar_larger, avatar_medium, avatar_thumb,
                 avatar_uri, aweme_count, follower_count, following_count, ins_id, nickname,
                 search_user_name, original_musician, sec_uid, short_id, total_favorited, uid,
                 unique_id, user_mode, user_rate, video_icon):
        self.avatar_168x168 = Avatar(**avatar_168x168)
        self.avatar_300x300 = Avatar(**avatar_300x300)
        self.avatar_larger = Avatar(**avatar_larger)
        self.avatar_medium = Avatar(**avatar_medium)
        self.avatar_thumb = Avatar(**avatar_thumb)
        self.avatar_uri = avatar_uri
        self.aweme_count = aweme_count
        self.follower_count = follower_count
        self.following_count = following_count
        self.ins_id = ins_id
        self.nickname = nickname
        self.search_user_name = search_user_name
        self.original_musician = OriginalMusician(**original_musician)
        self.sec_uid = sec_uid
        self.short_id = short_id
        self.total_favorited = total_favorited
        self.uid = uid
        self.unique_id = unique_id
        self.user_mode = user_mode
        self.user_rate = user_rate
        self.video_icon = Avatar(**video_icon)

# Hàm để load dữ liệu từ file JSON và tạo các đối tượng tương ứng
def load_user_info(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data_dict = json.load(file)
    
    user_list = data_dict["data"]["user_list"]
    user_objects = []
    
    for user_data in user_list:
        try:
            user_info = UserInfo(**user_data["user_info"])
            user_objects.append(user_info)
        except KeyError as e:
            print(f"Lỗi Key: Thiếu trường {e} trong user_info")
            continue
        except TypeError as e:
            print(f"Lỗi Type: {e}")
            continue
    
    return user_objects

# Đường dẫn tới tệp JSON
keyword = input("Nhập từ khóa: ")
output_file = f"tiktok_user_{keyword}_results.json"

# Load dữ liệu từ file JSON và tạo các đối tượng
users = load_user_info(output_file)

# In ra tất cả các thông tin của từng user object
for user in users:
    print(f"User {user.unique_id}:")
print(f"Nickname: {user.nickname}")
print(f"Follower count: {user.follower_count}")
print(f"Following count: {user.following_count}")
print(f"Instagram ID: {user.ins_id}")
print(f"Search username: {user.search_user_name}")
print(f"Total videos created: {user.aweme_count}")
print(f"Total favorited count: {user.total_favorited}")
print(f"User ID: {user.uid}")
print(f"Unique ID: {user.unique_id}")
print(f"User mode: {user.user_mode}")
print(f"User rate: {user.user_rate}")
print(f"Sec UID: {user.sec_uid}")
print(f"Short ID: {user.short_id}")
print(f"Avatar URI: {user.avatar_uri}")
print(f"Avatar 168x168: {user.avatar_168x168.uri}")
print(f"Avatar 300x300: {user.avatar_300x300.uri}")
print(f"Avatar larger: {user.avatar_larger.uri}")
print(f"Avatar medium: {user.avatar_medium.uri}")
print(f"Avatar thumb: {user.avatar_thumb.uri}")
print(f"Original musician info: Digg count - {user.original_musician.digg_count}, Music count - {user.original_musician.music_count}")
print("-" * 50)

