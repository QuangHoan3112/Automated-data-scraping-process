import json

class LabelTop:
    def __init__(self, data):
        self.uri = data.get('uri')
        self.url_list = data.get('url_list', [])
        self.width = data.get('width')
        self.height = data.get('height')

class ShareInfo:
    def __init__(self, data):
        self.share_url = data.get('share_url')
        self.share_desc = data.get('share_desc')
        self.share_title = data.get('share_title')
        self.share_desc_info = data.get('share_desc_info')

class MusicInfo:
    def __init__(self, data):
        self.id = data.get('id')
        self.id_str = data.get('id_str')
        self.title = data.get('title')
        self.author = data.get('author')
        self.album = data.get('album')
        self.cover_large = LabelTop(data.get('cover_large', {}))
        self.cover_medium = LabelTop(data.get('cover_medium', {}))
        self.cover_thumb = LabelTop(data.get('cover_thumb', {}))
        self.play_url = LabelTop(data.get('play_url', {}))
        self.source_platform = data.get('source_platform')
        self.duration = data.get('duration')
        self.extra = json.loads(data.get('extra', '{}'))
        self.user_count = data.get('user_count')
        self.share_info = ShareInfo(data.get('share_info', {}))
        self.status = data.get('status')
        self.owner_id = data.get('owner_id')
        self.owner_nickname = data.get('owner_nickname')
        self.is_original = data.get('is_original')
        self.mid = data.get('mid')
        self.owner_handle = data.get('owner_handle')
        self.sec_uid = data.get('sec_uid')
        self.avatar_thumb = LabelTop(data.get('avatar_thumb', {}))
        self.avatar_medium = LabelTop(data.get('avatar_medium', {}))
        self.preview_start_time = data.get('preview_start_time')
        self.preview_end_time = data.get('preview_end_time')
        self.is_commerce_music = data.get('is_commerce_music')
        self.is_original_sound = data.get('is_original_sound')
        self.audition_duration = data.get('audition_duration')
        self.shoot_duration = data.get('shoot_duration')
        self.is_allow_shoot = data.get('is_allow_shoot')
        self.is_author_artist = data.get('is_author_artist')
        self.matched_song = data.get('matched_song', {})
        self.video_duration = data.get('video_duration')
        self.aweme_type = data.get('aweme_type')

# Nhập ID của bài nhạc cần tìm
music_id = input("Nhập ID Music cần tìm: ")
output_file = f"tiktok_music_{music_id}.json"

# Đọc dữ liệu từ file JSON và chuyển thành đối tượng MusicInfo
with open(output_file, 'r', encoding='utf-8') as file:
    json_data = file.read()

data = json.loads(json_data)
music_info = MusicInfo(data['data']['music_info'])

# In ra tất cả các thông tin của đối tượng MusicInfo
print(f"Title: {music_info.title}")
print(f"Author: {music_info.author}")
print(f"Album: {music_info.album}")
print(f"Cover Large URI: {music_info.cover_large.uri}")
print(f"Cover Medium URI: {music_info.cover_medium.uri}")
print(f"Cover Thumb URI: {music_info.cover_thumb.uri}")
print(f"Play URL: {music_info.play_url.uri}")
print(f"Source Platform: {music_info.source_platform}")
print(f"Duration: {music_info.duration}")
print(f"User Count: {music_info.user_count}")
print(f"Share URL: {music_info.share_info.share_url}")
print(f"Owner ID: {music_info.owner_id}")
print(f"Owner Nickname: {music_info.owner_nickname}")
print(f"Is Original: {music_info.is_original}")
print(f"Mid: {music_info.mid}")
print(f"Owner Handle: {music_info.owner_handle}")
print(f"Sec UID: {music_info.sec_uid}")
print(f"Avatar Thumb URI: {music_info.avatar_thumb.uri}")
print(f"Avatar Medium URI: {music_info.avatar_medium.uri}")
print(f"Preview Start Time: {music_info.preview_start_time}")
print(f"Preview End Time: {music_info.preview_end_time}")
print(f"Is Commerce Music: {music_info.is_commerce_music}")
print(f"Is Original Sound: {music_info.is_original_sound}")
print(f"Audition Duration: {music_info.audition_duration}")
print(f"Shoot Duration: {music_info.shoot_duration}")
print(f"Is Allow Shoot: {music_info.is_allow_shoot}")
print(f"Is Author Artist: {music_info.is_author_artist}")
print(f"Matched Song: {music_info.matched_song}")
print(f"Video Duration: {music_info.video_duration}")
print(f"Aweme Type: {music_info.aweme_type}")
