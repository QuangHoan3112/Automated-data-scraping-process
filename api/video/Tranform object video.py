import json

# Định nghĩa các lớp Python
class MusicInfo:
    def __init__(self, id=None, title=None, play=None, cover=None, author=None, original=None, duration=None, album=None):
        self.id = id
        self.title = title
        self.play = play
        self.cover = cover
        self.author = author
        self.original = original
        self.duration = duration
        self.album = album

class Author:
    def __init__(self, id=None, unique_id=None, nickname=None, avatar=None):
        self.id = id
        self.unique_id = unique_id
        self.nickname = nickname
        self.avatar = avatar

class Data:
    def __init__(self, aweme_id=None, id=None, region=None, title=None, cover=None, ai_dynamic_cover=None, origin_cover=None, duration=None, play=None, wmplay=None, hdplay=None, size=None, wm_size=None, hd_size=None, music=None, music_info=None, play_count=None, digg_count=None, comment_count=None, share_count=None, download_count=None, collect_count=None, create_time=None, anchors=None, anchors_extras=None, is_ad=None, commerce_info=None, commercial_video_info=None, item_comment_settings=None, author=None):
        self.aweme_id = aweme_id
        self.id = id
        self.region = region
        self.title = title
        self.cover = cover
        self.ai_dynamic_cover = ai_dynamic_cover
        self.origin_cover = origin_cover
        self.duration = duration
        self.play = play
        self.wmplay = wmplay
        self.hdplay = hdplay
        self.size = size
        self.wm_size = wm_size
        self.hd_size = hd_size
        self.music = music
        self.music_info = MusicInfo(**music_info) if music_info else None
        self.play_count = play_count
        self.digg_count = digg_count
        self.comment_count = comment_count
        self.share_count = share_count
        self.download_count = download_count
        self.collect_count = collect_count
        self.create_time = create_time
        self.anchors = anchors
        self.anchors_extras = anchors_extras
        self.is_ad = is_ad
        self.commerce_info = commerce_info
        self.commercial_video_info = commercial_video_info
        self.item_comment_settings = item_comment_settings
        self.author = Author(**author) if author else None

class Response:
    def __init__(self, code=None, msg=None, processed_time=None, data=None):
        self.code = code
        self.msg = msg
        self.processed_time = processed_time
        self.data = Data(**data) if data else None

# Tên file output
video_id = input("Nhập ID Video: ")
output_file = f"tiktok_video_{video_id}_details.json"

# Đọc dữ liệu từ file JSON và xử lý
with open(output_file, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Tạo đối tượng Response từ dữ liệu JSON
response = Response(**json_data)

# Truy cập các thuộc tính của đối tượng Following
print("Following Information:")
print("Aweme ID:", response.data.aweme_id if response.data else None)
print("ID:", response.data.id if response.data else None)
print("Region:", response.data.region if response.data else None)
print("Title:", response.data.title if response.data else None)
print("Cover:", response.data.cover if response.data else None)
print("AI Dynamic Cover:", response.data.ai_dynamic_cover if response.data else None)
print("Origin Cover:", response.data.origin_cover if response.data else None)
print("Duration:", response.data.duration if response.data else None)
print("Play:", response.data.play if response.data else None)
print("WM Play:", response.data.wmplay if response.data else None)
print("HD Play:", response.data.hdplay if response.data else None)
print("Size:", response.data.size if response.data else None)
print("WM Size:", response.data.wm_size if response.data else None)
print("HD Size:", response.data.hd_size if response.data else None)
print("Music:", response.data.music if response.data else None)
print("Play Count:", response.data.play_count if response.data else None)
print("Digg Count:", response.data.digg_count if response.data else None)
print("Comment Count:", response.data.comment_count if response.data else None)
print("Share Count:", response.data.share_count if response.data else None)
print("Download Count:", response.data.download_count if response.data else None)
print("Collect Count:", response.data.collect_count if response.data else None)
print("Create Time:", response.data.create_time if response.data else None)
print("Anchors:", response.data.anchors if response.data else None)
print("Anchors Extras:", response.data.anchors_extras if response.data else None)
print("Is Ad:", response.data.is_ad if response.data else None)

# Truy cập các thuộc tính của đối tượng MusicInfo
if response.data and response.data.music_info:
    print("\nMusic Info:")
    print("ID:", response.data.music_info.id)
    print("Title:", response.data.music_info.title)
    print("Play:", response.data.music_info.play)
    print("Cover:", response.data.music_info.cover)
    print("Author:", response.data.music_info.author)
    print("Original:", response.data.music_info.original)
    print("Duration:", response.data.music_info.duration)
    print("Album:", response.data.music_info.album)

# Truy cập các thuộc tính của đối tượng Author
if response.data and response.data.author:
    print("\nAuthor Info:")
    print("ID:", response.data.author.id)
    print("Unique ID:", response.data.author.unique_id)
    print("Nickname:", response.data.author.nickname)
    print("Avatar:", response.data.author.avatar)
