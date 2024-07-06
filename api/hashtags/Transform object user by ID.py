import json

class Avatar:
    def __init__(self, uri=None, url_list=None):
        self.uri = uri
        self.url_list = url_list if url_list is not None else []

class User:
    def __init__(self, status=None, status_code=None, avatar_168x168=None, avatar_300x300=None, avatar_larger=None,
                 avatar_medium=None, avatar_thumb=None, follower_count=None, following_count=None, nickname=None,
                 original_musician=None, privacy_setting=None, sec_uid=None, share_info=None, short_id=None,
                 signature_language=None, tab_settings=None, total_favorited=None, uid=None, unique_id=None,
                 verification_type=None, video_icon=None):
        self.status = status
        self.status_code = status_code
        self.avatar_168x168 = Avatar(**(avatar_168x168 if avatar_168x168 else {}))
        self.avatar_300x300 = Avatar(**(avatar_300x300 if avatar_300x300 else {}))
        self.avatar_larger = Avatar(**(avatar_larger if avatar_larger else {}))
        self.avatar_medium = Avatar(**(avatar_medium if avatar_medium else {}))
        self.avatar_thumb = Avatar(**(avatar_thumb if avatar_thumb else {}))
        self.follower_count = follower_count
        self.following_count = following_count
        self.nickname = nickname
        self.original_musician = original_musician
        self.privacy_setting = privacy_setting
        self.sec_uid = sec_uid
        self.share_info = share_info
        self.short_id = short_id
        self.signature_language = signature_language
        self.tab_settings = tab_settings
        self.total_favorited = total_favorited
        self.uid = uid
        self.unique_id = unique_id
        self.verification_type = verification_type
        self.video_icon = Avatar(**(video_icon if video_icon else {}))

# Tên file output
user_id = input("Nhập ID người dùng: ")
data_file = f"user_{user_id}_tiktok_data.json"

# Đọc dữ liệu từ file JSON và phân tích thành dictionary
with open(data_file, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Tạo đối tượng User từ dữ liệu JSON
user_data = json_data["data"]["user"]
user_object = User(
    json_data.get("status"),
    json_data["data"].get("status_code"),
    user_data.get("avatar_168x168"),
    user_data.get("avatar_300x300"),
    user_data.get("avatar_larger"),
    user_data.get("avatar_medium"),
    user_data.get("avatar_thumb"),
    user_data.get("follower_count"),
    user_data.get("following_count"),
    user_data.get("nickname"),
    user_data.get("original_musician"),
    user_data.get("privacy_setting"),
    user_data.get("sec_uid"),
    user_data.get("share_info"),
    user_data.get("short_id"),
    user_data.get("signature_language"),
    user_data.get("tab_settings"),
    user_data.get("total_favorited"),
    user_data.get("uid"),
    user_data.get("unique_id"),
    user_data.get("verification_type"),
    user_data.get("video_icon")
)

# In ra một số thông tin của đối tượng User
print("Status:", user_object.status)
print("Status code:", user_object.status_code)
print("Follower count:", user_object.follower_count)
print("Following count:", user_object.following_count)
print("Nickname:", user_object.nickname)
print("Original musician:", user_object.original_musician)
print("Privacy setting:", user_object.privacy_setting)
print("Sec UID:", user_object.sec_uid)
print("Share info:", user_object.share_info)
print("Short ID:", user_object.short_id)
print("Signature language:", user_object.signature_language)
print("Tab settings:", user_object.tab_settings)
print("Total favorited:", user_object.total_favorited)
print("UID:", user_object.uid)
print("Unique ID:", user_object.unique_id)
print("Verification type:", user_object.verification_type)

print("\nAvatar 168x168:")
print("URI:", user_object.avatar_168x168.uri)
print("URL list:")
for url in user_object.avatar_168x168.url_list:
    print(url)

print("\nAvatar 300x300:")
print("URI:", user_object.avatar_300x300.uri)
print("URL list:")
for url in user_object.avatar_300x300.url_list:
    print(url)

print("\nAvatar larger:")
print("URI:", user_object.avatar_larger.uri)
print("URL list:")
for url in user_object.avatar_larger.url_list:
    print(url)

print("\nAvatar medium:")
print("URI:", user_object.avatar_medium.uri)
print("URL list:")
for url in user_object.avatar_medium.url_list:
    print(url)

print("\nAvatar thumb:")
print("URI:", user_object.avatar_thumb.uri)
print("URL list:")
for url in user_object.avatar_thumb.url_list:
    print(url)

print("\nVideo icon:")
print("URI:", user_object.video_icon.uri)
print("URL list:")
for url in user_object.video_icon.url_list:
    print(url)
