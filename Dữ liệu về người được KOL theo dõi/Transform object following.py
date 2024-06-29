class Following:
    def __init__(self, id, region, sec_uid, unique_id, nickname, signature, avatar, verified, secret,
                 aweme_count, follower_count, favoriting_count, total_favorited, ins_id,
                 youtube_channel_title, youtube_channel_id, twitter_name, twitter_id):
        self.id = id
        self.region = region
        self.sec_uid = sec_uid
        self.unique_id = unique_id
        self.nickname = nickname
        self.signature = signature
        self.avatar = avatar
        self.verified = verified
        self.secret = secret
        self.aweme_count = aweme_count
        self.follower_count = follower_count  # Giữ nguyên tên biến này vì dữ liệu JSON gửi về có tên là follower_count
        self.favoriting_count = favoriting_count
        self.total_favorited = total_favorited
        self.ins_id = ins_id
        self.youtube_channel_title = youtube_channel_title
        self.youtube_channel_id = youtube_channel_id
        self.twitter_name = twitter_name
        self.twitter_id = twitter_id
import json
from pickle import TRUE
# Dữ liệu JSON đã cung cấp
data = {
    "code": 0,
    "msg": "success",
    "processed_time": 0.4107,
    "data": {
      "followings": [
        {
          "id": "6902446316572967938",
          "region": "VN",
          "sec_uid": "MS4wLjABAAAAaHd34j9n4Y3Er2uY8ewreISIupFDc4Hfoz9aTw3OfpmpMjjcXF2b3IbYOb0UgvQa",
          "unique_id": "8saigon",
          "nickname": "Tâm Sài Gòn",
          "signature": "8saigonvn@gmail.com",
          "avatar": "https://p3-sg.tiktokcdn.com/tos-alisg-avt-0068/f9c4f07ae73bfd2361b3146fc38f2072~tplv-tiktokx-cropcenter-q:300:300:q75.jpeg?pack_by_platform=true&ps=124&s=COMMON_RELATION_LIST&sc=avatar&shcp=65db1d19&shp=30310797&t=1",
          "verified": False,
          "secret": False,
          "aweme_count": 1864,
          "follower_count": 94745,
          "favoriting_count": 1121,
          "total_favorited": 6391611,
          "ins_id": "",
          "youtube_channel_title": "8 Sài Gòn",
          "youtube_channel_id": "UC5qwfANyUq5799QnpkizrSw",
          "twitter_name": "",
          "twitter_id": ""
        },
        {
          "id": "6838245885366273025",
          "region": "VN",
          "sec_uid": "MS4wLjABAAAAh-wAJOn4s0otpHZTT7a1QvNk9KxNDN2qccQRBVdz6rTloIkoEi-efM26MlrtpM9t",
          "unique_id": "di2chinhchu",
          "nickname": "Nguyễn tuấn phong (điều)",
          "signature": "https://www.facebook.com/tuanphongmc.nguyen/",
          "avatar": "https://p3-sg.tiktokcdn.com/tos-alisg-avt-0068/7324303812338909185~tplv-tiktokx-cropcenter-q:300:300:q75.jpeg?pack_by_platform=true&ps=124&s=COMMON_RELATION_LIST&sc=avatar&shcp=65db1d19&shp=30310797&t=1",
          "verified": False,
          "secret": False,
          "aweme_count": 101,
          "follower_count": 65862,
          "favoriting_count": 202,
          "total_favorited": 795313,
          "ins_id": "",
          "youtube_channel_title": "",
          "youtube_channel_id": "",
          "twitter_name": "",
          "twitter_id": ""
        },
        {
          "id": "6517878028821921794",
          "region": "VN",
          "sec_uid": "MS4wLjABAAAAPLK7QkLQKgwdgi5Ml2StEGDv2ihLwjh-binFGRNLIjoVaLdCNv5hnnLqcZAIac4K",
          "unique_id": "max_nhamphuongnam",
          "nickname": "MAX - Nhamphuongnam 🍏",
          "signature": "Email: nhamnamofficial@gmail.com",
          "avatar": "https://p3-sg.tiktokcdn.com/tos-alisg-avt-0068/939b6e015913c62cfe652d37f69eba3b~tplv-tiktokx-cropcenter-q:300:300:q75.jpeg?pack_by_platform=true&ps=124&s=COMMON_RELATION_LIST&sc=avatar&shcp=65db1d19&shp=30310797&t=1",
          "verified": False,
          "secret": False,
          "aweme_count": 445,
          "follower_count": 197658,
          "favoriting_count": 1390,
          "total_favorited": 2031894,
          "ins_id": "nhamphuongnamm",
          "youtube_channel_title": "Nhâm Phương Nam Official",
          "youtube_channel_id": "UCOoQ4_lEG2TX_v8W7NaZZvw",
          "twitter_name": "",
          "twitter_id": ""
        },
        {
          "id": "6794078116661036034",
          "region": "VN",
          "sec_uid": "MS4wLjABAAAAdxjOPobISycc-CKf2wDnZKto05bbkaoqQpkG9pJ0cQ5VP7u6bih3h9pDQFEzhZyc",
          "unique_id": "linhchuoi.2000",
          "nickname": "Linh Chuối 🍌",
          "signature": "Contact for Work IG: nguyenhoangkhanhlinh.2000\nTất cả sản phẩm mình dùng bên dưới👇",
          "avatar": "https://p16-useast2a.tiktokcdn.com/tos-useast2a-avt-0068-giso/13a314ea2b4662e452493fd42a6cb06b~tplv-tiktokx-cropcenter-q:300:300:q75.jpeg?pack_by_platform=true&ps=124&s=COMMON_RELATION_LIST&sc=avatar&shcp=65db1d19&shp=30310797&t=1",
          "verified": False,
          "secret": False,
          "aweme_count": 585,
          "follower_count": 74567,
          "favoriting_count": 2055,
          "total_favorited": 2027812,
          "ins_id": "",
          "youtube_channel_title": "",
          "youtube_channel_id": "",
          "twitter_name": "",
          "twitter_id": ""
        },
        {
          "id": "6774503666692113410",
          "region": "VN",
          "sec_uid": "MS4wLjABAAAAmJhSGUX86xX0YQ8NXfKwR_ZWoZJy353WWfwY8JOKH4XCpelOvVODqTKhGJ8imOpq",
          "unique_id": "huynhduykhuongofficial",
          "nickname": "Huỳnh Duy Khương",
          "signature": "🔑 Kỹ năng giao tiếp\n🏯 Kỹ năng quản lý đội nhóm\n💇 Học cùng anh tại đây:",
          "avatar": "https://p3-sg.tiktokcdn.com/tos-alisg-avt-0068/1b75e9039ed7f55da3454996b566da74~tplv-tiktokx-cropcenter-q:300:300:q75.jpeg?pack_by_platform=true&ps=124&s=COMMON_RELATION_LIST&sc=avatar&shcp=65db1d19&shp=30310797&t=1",
          "verified": False, # type: ignore
          "secret": False, # type: ignore
          "aweme_count": 1312,
          "follower_count": 1559232,
          "favoriting_count": 2022,
          "total_favorited": 38767154,
          "ins_id": "",
          "youtube_channel_title": "Huỳnh Duy Khương",
          "youtube_channel_id": "UCtBZReQN5lbQgjGNOIGOS2Q",
          "twitter_name": "",
          "twitter_id": ""
        }
      ],
      "total": 42,
      "time": 1708376689,
      "hasMore": TRUE
    }
  }

# Chuyển đổi dữ liệu JSON thành các đối tượng Python
followings = [Following(**following_data) for following_data in data["data"]["followings"]]

# Duyệt qua danh sách followings và in ra các thuộc tính của từng đối tượng
for following in followings:
    print(f"ID: {following.id}")
    print(f"Nickname: {following.nickname}")
    print(f"Follower count: {following.follower_count}")
    print(f"Favoriting count: {following.favoriting_count}")
    print(f"Signature: {following.signature}")
    print(f"Avatar URL: {following.avatar}")
    print(f"Verified: {following.verified}")
    print(f"Secret: {following.secret}")
    print(f"Aweme count: {following.aweme_count}")
    print(f"Total favorited: {following.total_favorited}")
    print(f"Instagram ID: {following.ins_id}")
    print(f"YouTube channel title: {following.youtube_channel_title}")
    print(f"YouTube channel ID: {following.youtube_channel_id}")
    print(f"Twitter name: {following.twitter_name}")
    print(f"Twitter ID: {following.twitter_id}")
    print()

