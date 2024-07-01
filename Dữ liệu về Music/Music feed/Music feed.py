import requests
import json

# Nhập ID của âm nhạc từ người dùng
music_id = input("Nhập Music ID: ")

# Nhập số lượng truy vấn từ người dùng
max_cursor = input("Nhập số lượng truy vấn: ")

# URL API
url = f"https://tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com/music/{music_id}/feed"

# Thông tin querystring
querystring = {"max_cursor": max_cursor}

# Headers
headers = {
    "x-rapidapi-key": "6b6ca08709mshc0be3cb9d1c6b4bp11a949jsnc754d60f18a3",
    "x-rapidapi-host": "tiktok-scrapper-videos-music-challenges-downloader.p.rapidapi.com"
}

# Gửi request và nhận response
response = requests.get(url, headers=headers, params=querystring)

# Kiểm tra mã trạng thái của response
if response.status_code == 200:
    # Chuyển đổi response thành JSON
    data = response.json()
    
    # Lưu dữ liệu JSON vào file
    output_file = f"tiktok_music_{music_id}_feed.json"
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Dữ liệu đã được lưu vào file {output_file}")
else:
    print("Yêu cầu API không thành công. Mã trạng thái:", response.status_code)
    print("Nội dung response:", response.text)
