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

# Đoạn JSON mẫu
json_data = '''
{
    "status": "ok",
    "data": {
      "status_code": 0,
      "user": {
        "avatar_168x168": {
          "uri": "tos-alisg-avt-0068/7311323706284834818",
          "url_list": [
            "https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/7311323706284834818~c5_168x168.webp?lk3s=a5d48078\u0026nonce=61710\u0026refresh_token=b88507cd16e43054c760d3da3ab30e88\u0026x-expires=1719561600\u0026x-signature=f3NTzbWyrxB6fFjQwyLEaa9nrGw%3D\u0026shp=a5d48078\u0026shcp=2472a6c6",
            "https://p9-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/7311323706284834818~c5_168x168.webp?lk3s=a5d48078\u0026nonce=22430\u0026refresh_token=6f2c165a82b5113ba813b9b42be278b1\u0026x-expires=1719561600\u0026x-signature=%2BCiqnqUHc28Im0bImq5YvyMbBaQ%3D\u0026shp=a5d48078\u0026shcp=2472a6c6",
            "https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/7311323706284834818~c5_168x168.jpeg?lk3s=a5d48078\u0026nonce=30751\u0026refresh_token=5253671c9cfb79082532275abfd4a890\u0026x-expires=1719561600\u0026x-signature=TgoX145IlvUTanRxIBqFqmVbnvM%3D\u0026shp=a5d48078\u0026shcp=2472a6c6"
          ]
        },
        "avatar_300x300": {
          "uri": "tos-alisg-avt-0068/7311323706284834818",
          "url_list": [
            "https://p9-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/7311323706284834818~c5_300x300.webp?lk3s=a5d48078\u0026nonce=90052\u0026refresh_token=af7694d1211aec647cd5334f641f641c\u0026x-expires=1719561600\u0026x-signature=QM7%2BFhyykc8avcf3PN51UpGAkjA%3D\u0026shp=a5d48078\u0026shcp=2472a6c6",
            "https://p16-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/7311323706284834818~c5_300x300.webp?lk3s=a5d48078\u0026nonce=30429\u0026refresh_token=fdc23ab4ce16721d04ea727a0f47da7b\u0026x-expires=1719561600\u0026x-signature=yLc1Ceq2sXQkXd5EbzmMd%2BwrBYs%3D\u0026shp=a5d48078\u0026shcp=2472a6c6",
            "https://p9-sign-sg.tiktokcdn.com/tos-alisg-avt-0068/7311323706284834818~c5_300x300.jpeg?lk3s=a5d48078\u0026nonce=79219\u0026refresh_token=a9f685916adf6b6026365c61dff101ad\u0026x-expires=1719561600\u0026x-signature=8VbjvTY6Edjma3D%2BLwxS3JbN8iY%3D\u0026shp=a5d48078\u0026shcp=2472a6c6"
          ]
        },
        "avatar_larger": {
          "uri": "tos-alisg-avt-0068/7311323706284834818",
          "url_list": [
            "https://p9-sign-sg.tiktokcdn.com/aweme/1080x1080/tos-alisg-avt-0068/7311323706284834818.webp?lk3s=a5d48078\u0026nonce=28814\u0026refresh_token=0a5e1e152a974bc658d1c9346b21d19d\u0026x-expires=1719561600\u0026x-signature=ZYL3IQJq15H4Cgeni3oJUmK3gPs%3D\u0026shp=a5d48078\u0026shcp=2472a6c6",
            "https://p16-sign-sg.tiktokcdn.com/aweme/1080x1080/tos-alisg-avt-0068/7311323706284834818.webp?lk3s=a5d48078\u0026nonce=68841\u0026refresh_token=7cc5308bc307ab181e3112de77bd9d53\u0026x-expires=1719561600\u0026x-signature=5MKAKHeF95KjZnaSCpPQGXGh6BY%3D\u0026shp=a5d48078\u0026shcp=2472a6c6",
            "https://p9-sign-sg.tiktokcdn.com/aweme/1080x1080/tos-alisg-avt-0068/7311323706284834818.jpeg?lk3s=a5d48078\u0026nonce=41572\u0026refresh_token=a566f0dafe0fa96980d0077d03020d72\u0026x-expires=1719561600\u0026x-signature=w3suT1HrvaERFJZ0zcXpoTphbow%3D\u0026shp=a5d48078\u0026shcp=2472a6c6"
          ]
        },
        "avatar_medium": {
          "uri": "tos-alisg-avt-0068/7311323706284834818",
          "url_list": [
            "https://p16-sign-sg.tiktokcdn.com/aweme/720x720/tos-alisg-avt-0068/7311323706284834818.webp?lk3s=a5d48078\u0026nonce=80089\u0026refresh_token=799c7cfdd5214ee49aff7f71148adad4\u0026x-expires=1719561600\u0026x-signature=y%2FkZ8Y70xL%2Fx%2B%2F8xDrUnnmsebPQ%3D\u0026shp=a5d48078\u0026shcp=2472a6c6",
            "https://p9-sign-sg.tiktokcdn.com/aweme/720x720/tos-alisg-avt-0068/7311323706284834818.webp?lk3s=a5d48078\u0026nonce=96633\u0026refresh_token=b3bd96ac2fd127071e65c60711a8dd04\u0026x-expires=1719561600\u0026x-signature=jCOjx54gTfNKvQxyQR8ZeshJu5s%3D\u0026shp=a5d48078\u0026shcp=2472a6c6",
            "https://p16-sign-sg.tiktokcdn.com/aweme/720x720/tos-alisg-avt-0068/7311323706284834818.jpeg?lk3s=a5d48078\u0026nonce=85332\u0026refresh_token=7841f2e5cbaa5989e8c8e586d3bc46be\u0026x-expires=1719561600\u0026x-signature=yMy3eE5rk1brdl6%2FEQIl5D4zlq4%3D\u0026shp=a5d48078\u0026shcp=2472a6c6"
          ]
        },
        "avatar_thumb": {
          "uri": "tos-alisg-avt-0068/7311323706284834818",
          "url_list": [
            "https://p16-sign-sg.tiktokcdn.com/aweme/100x100/tos-alisg-avt-0068/7311323706284834818.webp?lk3s=a5d48078\u0026nonce=5620\u0026refresh_token=3b85d1b84af006bb257a33bb81735e8e\u0026x-expires=1719561600\u0026x-signature=7r8lP4i8nQ28m5CkqaFpAO%2B95Hg%3D\u0026shp=a5d48078\u0026shcp=2472a6c6",
            "https://p9-sign-sg.tiktokcdn.com/aweme/100x100/tos-alisg-avt-0068/7311323706284834818.webp?lk3s=a5d48078\u0026nonce=11742\u0026refresh_token=105b577f1945e553cb105c4a4ffc2c0f\u0026x-expires=1719561600\u0026x-signature=lilanUbBtgfwdrkefH47HTt5ZUg%3D\u0026shp=a5d48078\u0026shcp=2472a6c6",
            "https://p16-sign-sg.tiktokcdn.com/aweme/100x100/tos-alisg-avt-0068/7311323706284834818.jpeg?lk3s=a5d48078\u0026nonce=5237\u0026refresh_token=0c80b6e62b39139fd36b12234cb5a5fe\u0026x-expires=1719561600\u0026x-signature=Tl3H%2B6NFfe7lNxyv4gP0zwIsETU%3D\u0026shp=a5d48078\u0026shcp=2472a6c6"
          ]
        },
        "aweme_count": 219,
        "commerce_user_info": {
          "ad_experience_entry": false,
          "ad_experience_text": "",
          "ad_revenue_rits": null
        },
        "custom_verify": "Trấn Thành",
        "follower_count": 6683799,
        "following_count": 41,
        "nickname": "Trấn Thành",
        "original_musician": {
          "digg_count": 0,
          "music_count": 67,
          "music_used_count": 0
        },
        "privacy_setting": {
          "following_visibility": 1
        },
        "profile_tab_type": 3,
        "sec_uid": "MS4wLjABAAAAB5j1_V17p6a1EnXRVjtlpg8CSNtYSNcWR_-LT9AInI4eHRpDjonGRzdOvdx7dLMV",
        "share_info": {
          "share_url": "https://www.tiktok.com/@tranthanh123?_r=1\u0026_d=e5j772h0d16h4l\u0026sec_uid=MS4wLjABAAAAB5j1_V17p6a1EnXRVjtlpg8CSNtYSNcWR_-LT9AInI4eHRpDjonGRzdOvdx7dLMV\u0026share_author_id=6541596320166576129\u0026sharer_language=en\u0026source=h5_m",
          "share_desc": "Check out Trấn Thành! #TikTok",
          "share_title": "Join TikTok and see what I’ve been up to!"
        },
        "short_id": "0",
        "show_artist_playlist": 1,
        "signature_language": "un",
        "tab_settings": {
          "private_tab": {
            "private_tab_style": 1,
            "show_private_tab": false
          }
        },
        "total_favorited": 50092524,
        "uid": "6541596320166576129",
        "unique_id": "tranthanh123",
        "verification_type": 1,
        "video_icon": {
          "uri": "",
          "url_list": []
        }
      }
    }
  }
'''

# Phân tích JSON thành dictionary
data = json.loads(json_data)

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

