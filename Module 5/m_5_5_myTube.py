from time import sleep


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        pass

    def log_in(self, username, password):
        if username in self.users:
            pass
        pass

    def register(self, un, pw, age):
        self.log_out()
        if un in self.users:
            print(f'Имя пользователя {un} занято.')
        else:
            self.users.append(User(un, pw, age))
            self.log_in(un, pw)
            pass

        pass

    def log_out(self):
        self.current_user = None
        pass

    def add(self, *kwargs):
        for v in kwargs:
            if isinstance(v, Video):
                self.videos.append(v)
        pass

    def get_videos(self, query):
        reply = []
        for video in self.videos:
            if query.lower() in video.title.lower():
                reply.append(video.title)
                pass
            pass
        print(reply)
        pass

    def watch_video(self, query):
        if self.current_user is None:
            print('Для просмотра видео необходимо войти в аккаунт.')
        elif True:
            pass
        pass
    pass


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time = time_now
        self.adult = adult_mode
        pass
    pass


class User:
    def __init__(self, nickname, password, age):
        self.username = nickname
        self.pw = hash(password)
        self.age = age
        pass
    pass


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
