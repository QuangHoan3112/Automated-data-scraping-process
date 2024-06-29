# Định nghĩa các lớp Python
class MusicInfo:
    def __init__(self, id, title, play, cover, author, original, duration, album):
        self.id = id
        self.title = title
        self.play = play
        self.cover = cover
        self.author = author
        self.original = original
        self.duration = duration
        self.album = album

class Author:
    def __init__(self, id, unique_id, nickname, avatar):
        self.id = id
        self.unique_id = unique_id
        self.nickname = nickname
        self.avatar = avatar

class Data:
    def __init__(self, aweme_id, id, region, title, cover, ai_dynamic_cover, origin_cover, duration, play, wmplay, hdplay, size, wm_size, hd_size, music, music_info, play_count, digg_count, comment_count, share_count, download_count, collect_count, create_time, anchors, anchors_extras, is_ad, commerce_info, commercial_video_info, item_comment_settings, author):
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
        self.music_info = MusicInfo(**music_info)
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
        self.author = Author(**author)

class Response:
    def __init__(self, code, msg, processed_time, data):
        self.code = code
        self.msg = msg
        self.processed_time = processed_time
        self.data = Data(**data)

# Dữ liệu JSON
import json

# Đường dẫn đến file JSON chứa dữ liệu
file_path = "path/to/your/file.json"  #Note: đường truyền này có sau khi code kia chạy xong

# Đọc dữ liệu từ file JSON
with open(file_path, "r", encoding="utf-8") as file:
    json_data = json.load(file)
response = Response(**json_data)

# Truy cập các thuộc tính của đối tượng Following
print("Following Information:")
print("Aweme ID:", response.data.aweme_id)
print("ID:", response.data.id)
print("Region:", response.data.region)
print("Title:", response.data.title)
print("Cover:", response.data.cover)
print("AI Dynamic Cover:", response.data.ai_dynamic_cover)
print("Origin Cover:", response.data.origin_cover)
print("Duration:", response.data.duration)
print("Play:", response.data.play)
print("WM Play:", response.data.wmplay)
print("HD Play:", response.data.hdplay)
print("Size:", response.data.size)
print("WM Size:", response.data.wm_size)
print("HD Size:", response.data.hd_size)
print("Music:", response.data.music)
print("Play Count:", response.data.play_count)
print("Digg Count:", response.data.digg_count)
print("Comment Count:", response.data.comment_count)
print("Share Count:", response.data.share_count)
print("Download Count:", response.data.download_count)
print("Collect Count:", response.data.collect_count)
print("Create Time:", response.data.create_time)
print("Anchors:", response.data.anchors)
print("Anchors Extras:", response.data.anchors_extras)
print("Is Ad:", response.data.is_ad)

# Truy cập các thuộc tính của đối tượng MusicInfo
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
print("\nAuthor Info:")
print("ID:", response.data.author.id)
print("Unique ID:", response.data.author.unique_id)
print("Nickname:", response.data.author.nickname)
print("Avatar:", response.data.author.avatar)

