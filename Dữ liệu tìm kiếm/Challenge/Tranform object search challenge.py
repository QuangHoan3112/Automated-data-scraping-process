import json

# Định nghĩa các lớp cho dữ liệu từ JSON
class ChallengeInfo:
    def __init__(self, view_count, type, user_count, cid, cha_name):
        self.view_count = view_count
        self.type = type
        self.user_count = user_count
        self.cid = cid
        self.cha_name = cha_name

class Challenge:
    def __init__(self, challenge_info, items, position):
        self.challenge_info = challenge_info
        self.items = items
        self.position = position

class Data:
    def __init__(self, challenge_list):
        self.challenge_list = challenge_list

class Response:
    def __init__(self, status, data):
        self.status = status
        self.data = data

# Hàm để load dữ liệu từ file JSON và tạo các đối tượng tương ứng
def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data_dict = json.load(file)
    
    # Sử dụng list comprehension và map để tạo danh sách các đối tượng Challenge
    challenge_list = list(map(lambda item: Challenge(
        challenge_info=ChallengeInfo(
            view_count=item["challenge_info"]["view_count"],
            type=item["challenge_info"]["type"],
            user_count=item["challenge_info"]["user_count"],
            cid=item["challenge_info"]["cid"],
            cha_name=item["challenge_info"]["cha_name"]
        ),
        items=item["items"],
        position=item["position"]
    ), data_dict["data"]["challenge_list"]))
    
    data = Data(challenge_list=challenge_list)
    response = Response(status=data_dict["status"], data=data)
    
    return response

# Thay đổi tên file JSON tương ứng
keyword = input("Nhập keyword: ")  # Thay thế bằng từ khóa thực tế của bạn
file_path = f"tiktok_challenge_{keyword}_results.json"

# Thực hiện load dữ liệu từ file JSON và tạo các đối tượng
response = load_json_data(file_path)

# In ra tất cả thông tin
print("Response Status:", response.status)
for idx, challenge in enumerate(response.data.challenge_list):
    print(f"Challenge {idx + 1}:")
    print("  - Challenge Info:")
    print("    - View Count:", challenge.challenge_info.view_count)
    print("    - Type:", challenge.challenge_info.type)
    print("    - User Count:", challenge.challenge_info.user_count)
    print("    - CID:", challenge.challenge_info.cid)
    print("    - Challenge Name:", challenge.challenge_info.cha_name)
    print("  - Items:", challenge.items)
    print("  - Position:", challenge.position)
    print()  # Dòng trống để phân tách giữa các challenge
