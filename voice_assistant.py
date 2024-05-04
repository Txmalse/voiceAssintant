import os
import speech_recognition
import webbrowser
import pygame

while True:

    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5

    commands_dict = {
        'commands': dict(greeting=(['привіт',
                                    'вітаю',
                                    'здоров',
                                    'доров']),
                         create_task=(['чек',
                                       'створи завдання']),
                         search=(['знайди',
                                  'знайди в інтернеті',
                                  'знайди в гуглі',
                                  'знайди в google',
                                  'шукай',
                                  'шукай в інтернеті',
                                  'шукай в гуглі',
                                  'шукай в в google']),
                         play_music=(['включи музику',
                                      'музику включай',
                                      'давай музику',
                                      'музику врубай',
                                      'музику включай',
                                      'запускай музику',
                                      'врубай музон',
                                      'врубай музику',
                                      'включай музон',
                                      'включай музику',
                                      'запусти музику',
                                      'послухаєм',
                                      'запусти трек',
                                      'давай послухаєм музику',
                                      'послухаєм музику']),
                         web_watch=(['відкрий youtube',
                                     'запусти youtube',
                                     'зайди на youtube',
                                     'зайди youtube',
                                     'youtube',
                                     'включи youtube']),
                         sys_task=(['диспетчер завдань',
                                    'відкрий диспетчер',
                                    'відкрий диспетчер завдань',
                                    'відкрий диспетчер задач',
                                    'запусти диспетчер',
                                    'запусти диспетчер задач',
                                    'запусти диспетчер завдань',
                                    'диспетчер',
                                    'відкрий диспечер',
                                    'відкрий диспечер завдань',
                                    'відкрий диспечер задач',
                                    'запусти диспечер',
                                    'запусти диспечер задач',
                                    'запусти диспечер завдань',
                                    'відкрий діспетчер',
                                    'відкрий діспетчер завдань',
                                    'відкрий діспетчер задач',
                                    'запусти діспетчер',
                                    'запусти діспетчер задач',
                                    'запусти діспетчер завдань',
                                    'відкрий діспетчер',
                                    'відкрий діспетчер завдань',
                                    'відкрий діспетчер задач',
                                    'запусти діспетчер',
                                    'запусти діспетчер задач',
                                    'запусти діспетчер завдань',
                                    'діспетчер',
                                    ]),
                         explorer=(['провідник',
                                    'відкрий папку',
                                    'папку',
                                    'відкрий проводник',
                                    'відкрий провідник',
                                    'відкрий ще один провідник',
                                    'відкрий ще один проводник',
                                    'відкрий ще один проводнік',
                                    'відкрий ще одну папку',
                                    'запусти провідник',
                                    'запусти ще один провідник',
                                    'запусти ще один проводник',
                                    'запусти ще один проводнік',
                                    'запусти проводник',
                                    'запусти проводнік',
                                    'проводник']),
                         records=(['запис']),
                         settings=(['відкрий настройки',
                                    'відкрий параметри']),
                         grats=(['дякую',
                                 'молодець']),
                         volume_music=(['гучність 10%',
                                        'гучність 20%',
                                        'гучність 30%',
                                        'гучність 40%',
                                        "гучність 50%",
                                        'гучність 60%',
                                        'гучність 70%',
                                        'гучність 80%',
                                        "гучність 90%",
                                        'гучність 100%'])
                         )
    }


    def listen_command():
        """The function will return the recognized command"""

        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.2)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio, language="uk-UA").lower()

            return query
        except speech_recognition.UnknownValueError:
            return 'Не зрозумів !'


    def greeting():
        """Greeting function"""
        return 'Привіт!'



    def records():
        print('Очікую...')
        m = listen_command()
        return m


    def grats():
        """Senc u function"""
        return 'Будь ласка! (^_^)'



    def create_task():
        """Create a todo task"""
        print('Що добавити в todo-list?')
        query = listen_command()
        with open('todo-list.txt', 'a') as file:
            file.write(f"! {query}\n")
            file.close()
        return f'Задача {query} добавлена в todo-list!'

    def search():
        print("Слухаю?")
        query = listen_command()
        url = ('https://www.google.com.tr/search?q={}') .format(query)
        webbrowser.open_new_tab(url)
        return 'Шукаю ', query, '.'

    def web_watch():
        """Watch a web page"""
        webbrowser.open('https://www.youtube.com', new=2)
        return 'Відкриваю Ютуб!'


    def settings():
        os.system(f'start C:/Windows/ImmersiveControlPanel/SystemSettings.exe')
        return 'Відкриваю Параметри!'


    def explorer():
        os.system(f'start C:/Windows/explorer.exe')
        return 'Відкриваю Провідник!'


    def sys_task():
        os.system(f'start C:/Windows/System32/Taskmgr.exe')
        return 'Відкриваю Диспетчер завдань!'

    def play_music():
        """Play youtube playlist"""

        url = ('https://www.youtube.com/watch?v=BN1WwnEDWAM&list=RDBN1WwnEDWAM&start_radio=1') # ваша ссилка на плейлист
        webbrowser.open_new_tab(url)

        return 'Включаю музику!'


    def volume_music():
        """Volume of the music"""
        query = listen_command()
        if query == 'гучність 10%':

            print('Гучність: 10 %')
            return pygame.mixer.music.set_volume(0.1)
        elif query == 'гучність 20%':

            print('Гучність: 20 %')
            return pygame.mixer.music.set_volume(0.2)
        elif query == 'гучність 30%':

            print('Гучність: 30 %')
            return pygame.mixer.music.set_volume(0.3)
        elif query == 'гучність 40%':
            pygame.mixer.music.set_volume(0.4)
            return 'Гучність: 40 %'
        elif query == "гучність 50%":
            pygame.mixer.music.set_volume(0.5)
            return 'Гучність: 50 %'
        elif query == 'гучність 60%':
            pygame.mixer.music.set_volume(0.6)
            return 'Гучність: 60 %'
        elif query == 'гучність 70%':
            pygame.mixer.music.set_volume(0.7)
            return 'Гучність: 70 %'
        elif query == 'гучність 80%':
            pygame.mixer.music.set_volume(0.8)
            return 'Гучність: 80 %'
        elif query == "гучність 90%":
            pygame.mixer.music.set_volume(0.9)
            return 'Гучність: 90 %'
        elif query == 'гучність 100%':
            pygame.mixer.music.set_volume(1.0)
            return 'Гучність: 100 %'


    def main():
        query = listen_command()

        for k, v in commands_dict['commands'].items():
            if query in v:
                print(globals()[k]())


    if __name__ == '__main__':
        main()
