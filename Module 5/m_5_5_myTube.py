from time import sleep


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        pass

    def __repr__(self):
        return (f'Текущий пользователь: {self.current_user}; '
                f'Зарегистрированных пользователей: {len(self.users)}; '
                f'Загруженных видео: {len(self.videos)}')

    def log_in(self, username, password):
        unknown_user = True
        for user in self.users:
            if user.un == username:
                unknown_user = False
                if user.pw == hash(password):
                    self.current_user = user
                    print(f'Выполнен вход в аккаунт {username}.')
                    break
                else:
                    print("Неверный пароль.")
                    pass
                pass
        if unknown_user:
            print("Пользователь с таким именем не зарегистрирован.")
            pass
        pass

    def register(self, un, pw, age):
        user = User(un, pw, age)
        for us in self.users:
            if user.un == us.un:
                print(f'Имя пользователя {un} уже занято.')
                break
            pass
        else:
            self.users.append(user)
            print(f'Пользователь {un} был успешно зарегестрирован.')
            if self.current_user is not None:
                self.log_out()
            self.log_in(un, pw)
            pass
        pass

    def log_out(self):
        self.current_user = None
        print(f'Выполнен выход из аккаунта.')
        pass

    def add(self, *kwargs):
        for v in kwargs:
            if isinstance(v, Video):
                self.videos.append(v)
                print(f'Было добавлено новое видео - {v.title} длительностью {v.duration}.')
                pass
            pass
        pass

    def get_videos(self, query):
        reply = []
        for video in self.videos:
            if query.lower() in video.title.lower():
                reply.append(video.title)
                pass
            pass
        if reply:
            return f'Подходящие по запросу видео: {reply}.'
        else:
            return 'Подходящих по запросу видео не обнаружено.'

    def watch_video(self, query):
        if self.current_user is not None:
            found = False
            for video in self.videos:
                if query == video.title:
                    found = True
                    if video.adult and (self.current_user.age < 18):
                        print("Данное видео недуступно для просмотра несовершеннолетним пользователям.")
                        break
                    else:
                        print(f'Видео "{video.title}" успешно запущено.')
                        t = 0
                        while t < video.duration:
                            print(t, end=' ')
                            t += 1
                            sleep(1)
                            pass
                        print("Конец видео.")
                        pass
                    break
            if not found:
                print("Видео с таким названием не найдено.")
                pass
        else:
            print('Для просмотра видео необходимо войти в аккаунт.')
        pass
    pass


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time = time_now
        self.adult = adult_mode
        pass

    def __str__(self):
        return f'"{self.title}"; {self.duration} секунд'
    pass


class User:
    def __init__(self, nickname, password, age):
        self.un = nickname
        self.pw = hash(password)
        self.age = age
        pass

    def __str__(self):
        return self.un
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
