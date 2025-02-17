import instaloader

# Login ke akun Instagram
USERNAME = "faroyzisptra"
PASSWORD = "2fpds7j.9Nn.Q.9"

bot = instaloader.Instaloader()
bot.login(USERNAME, PASSWORD)

# Ambil daftar following & followers
profile = instaloader.Profile.from_username(bot.context, USERNAME)
followers = {f.username for f in profile.get_followers()}
following = {f.username for f in profile.get_followees()}

# Cari orang yang tidak follow balik
not_following_back = following - followers

# Unfollow mereka
for user in not_following_back:
    print(f"Unfollowing: {user}")
    bot.context.username_unfollow(user)

print("✅ Selesai Unfollow yang Tidak Follow Balik!")
