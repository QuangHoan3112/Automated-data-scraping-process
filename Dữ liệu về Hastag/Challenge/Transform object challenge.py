import json

# Define classes for JSON data
class ChallengeInfo:
    def __init__(self, view_count=None, hashtag_profile=None, type=None, user_count=None, cid=None, cha_name=None):
        self.view_count = view_count
        self.hashtag_profile = hashtag_profile
        self.type = type
        self.user_count = user_count
        self.cid = cid
        self.cha_name = cha_name

class ChallengeData:
    def __init__(self, status=None, data=None):
        self.status = status
        self.data = data

# Function to load challenge data from JSON file
def load_challenge_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data_dict = json.load(file)
    
    status = data_dict.get("status")
    challenge_info = data_dict.get("data", {}).get("ch_info", {})

    challenge_data = ChallengeData(status, ChallengeInfo(**challenge_info))
    return challenge_data

# Path to the JSON file
challenge_name = input("Nhập tên challenge: ")
output_file = f"tiktok_challenge_{challenge_name}.json"

# Load data from JSON file into objects
challenge_data = load_challenge_data(output_file)

# Accessing and printing all data
print(f"Challenge Name: {challenge_data.data.cha_name}")
print(f"Challenge Type: {challenge_data.data.type}")
print(f"User Count: {challenge_data.data.user_count}")
print(f"View Count: {challenge_data.data.view_count}")
print(f"Hashtag Profile URL: {challenge_data.data.hashtag_profile}")
print(f"Challenge ID: {challenge_data.data.cid}")
print(f"Status: {challenge_data.status}")

