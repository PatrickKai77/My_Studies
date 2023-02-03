
banned_users = ['andrew', 'carolina', 'david']
user='marie'
if user not in banned_users:
    print(user.title() + ", você pode responder ao comentário.")
else:
    print(user.title() + ", você foi temporariamente banida(o).")