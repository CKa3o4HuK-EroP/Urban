from time import sleep


class UrTube:
    pass


class Video:
    videos = []

    def __new__(cls, *args, **kwargs):
        if args[0] not in cls.videos:
            cls.videos.append(args[0])
            return object.__new__(cls)
        else:
            print("Видео с таким названием уже существует.")
            return None

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        pass
    pass


class User:
    users = []

    def __new__(cls, *args, **kwargs):
        if args[0] not in cls.users:
            cls.users.append(args[0])
            return object.__new__(cls)
        else:
            print(f'Имя пользователя {args[0]} уже занято.')
            return None

    def __init__(self, nickname, *, password, age):
        self.username = nickname
        self.pw = hash(password)
        self.age = age
    pass
