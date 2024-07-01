class Avatar:
    def __init__(self, uri, url_list):
        self.uri = uri
        self.url_list = url_list

class User:
    def __init__(self, status, status_code, avatar_168x168, avatar_300x300, avatar_larger, avatar_medium, avatar_thumb,
                 follower_count, following_count, nickname, original_musician, privacy_setting, sec_uid, share_info,
                 short_id, signature_language, tab_settings, total_favorited, uid, unique_id, verification_type,
                 video_icon):
        self.status = status
        self.status_code = status_code
        self.avatar_168x168 = Avatar(**avatar_168x168)
        self.avatar_300x300 = Avatar(**avatar_300x300)
        self.avatar_larger = Avatar(**avatar_larger)
        self.avatar_medium = Avatar(**avatar_medium)
        self.avatar_thumb = Avatar(**avatar_thumb)
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
        self.video_icon = Avatar(**video_icon)

import json

# Tên file output
nickname = input("Nhập nickname người dùng: ")
output_file = f"user_{nickname}_tiktok_data.json"

# Đọc dữ liệu từ file JSON và phân tích thành dictionary
with open(output_file, 'r', encoding='utf-8') as file:
    json_data = json.load(file)


# Tạo đối tượng User từ dữ liệu JSON
user_data = data["data"]["user"]
user_object = User(
    data["status"],
    data["data"]["status_code"],
    user_data["avatar_168x168"],
    user_data["avatar_300x300"],
    user_data["avatar_larger"],
    user_data["avatar_medium"],
    user_data["avatar_thumb"],
    user_data["follower_count"],
    user_data["following_count"],
    user_data["nickname"],
    user_data["original_musician"],
    user_data["privacy_setting"],
    user_data["sec_uid"],
    user_data["share_info"],
    user_data["short_id"],
    user_data["signature_language"],
    user_data["tab_settings"],
    user_data["total_favorited"],
    user_data["uid"],
    user_data["unique_id"],
    user_data["verification_type"],
    user_data["video_icon"]
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

