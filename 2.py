import speech_recognition as sr
import pyttsx3
import random

def initialize_tts():
    engine = pyttsx3.init()
    return engine

def initialize_recognizer():
    recognizer = sr.Recognizer()
    return recognizer

def speak(engine, text, language='ru'):
    if language == 'ru':
        engine.setProperty('voice', 'ru')
    elif language == 'en':
        engine.setProperty('voice', 'en')
    engine.say(text)
    engine.runAndWait()

def recognize_speech(recognizer, language='ru-RU'):
    with sr.Microphone() as source:
        print("Скажите что-нибудь:")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language=language)
            print(f"Вы сказали: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
            return None
        except sr.RequestError as e:
            print(f"Ошибка сервиса распознавания речи; {e}")
            return None

def flip_coin(engine):
    result = random.choice(['Орёл', 'Решка'])
    speak(engine, f"Результат подбрасывания монетки: {result}")

def guess_number(engine):
    number_to_guess = random.randint(1, 100)
    speak(engine, "Загадано число от 1 до 100. Попробуйте угадать!")
    while True:
        user_input = recognize_speech(recognizer)
        if user_input is None:
            continue
        if 'стоп' in user_input or 'stop' in user_input:
            speak(engine, "Игра в угадайку остановлена.")
            break
        try:
            user_guess = int(user_input)
            if user_guess < number_to_guess:
                speak(engine, "Загаданное число больше.")
            elif user_guess > number_to_guess:
                speak(engine, "Загаданное число меньше.")
            else:
                speak(engine, "Вы угадали!")
                break
        except ValueError:
            speak(engine, "Пожалуйста, введите целое число.")

def change_language_settings(engine, language='ru'):
    if language == 'ru':
        recognizer_language = 'ru-RU'
    elif language == 'en':
        recognizer_language = 'en-US'
    else:
        speak(engine, "Неподдерживаемый язык. Поддерживаются только 'русский' и 'английский'.")
        return None
    speak(engine, f"Язык изменён на {language}.")
    return recognizer_language

def main():
    engine = initialize_tts()
    global recognizer
    recognizer = initialize_recognizer()
    recognizer_language = 'ru-RU'

    speak(engine, "Выберите действие: подбросить монетку, угадать число, изменить язык или выйти.")

    while True:
        command = recognize_speech(recognizer, recognizer_language)
        if command is None:
            continue
        if recognizer_language == 'ru-RU':
            if 'подбросить монетку' in command:
                flip_coin(engine)
            elif 'угадать число' in command:
                guess_number(engine)
            elif 'изменить язык' in command:
                speak(engine, "На какой язык вы хотите переключиться? Русский или английский?")
                language_command = recognize_speech(recognizer, recognizer_language)
                if language_command is None:
                    continue
                if 'русский' in language_command:
                    recognizer_language = change_language_settings(engine, 'ru')
                elif 'английский' in language_command:
                    recognizer_language = change_language_settings(engine, 'en')
            elif 'выйти' in command:
                speak(engine, "До свидания!")
                break
            elif 'стоп' in command:
                speak(engine, "Программа остановлена.")
                break
            else:
                speak(engine, "Неверный выбор. Попробуйте снова.")
        elif recognizer_language == 'en-US':
            if 'flip a coin' in command or 'подбросить монетку' in command:
                flip_coin(engine)
            elif 'guess number' in command or 'угадать число' in command:
                guess_number(engine)
            elif 'russian' in command or 'изменить язык' in command:
                speak(engine, "Which language would you like to switch to? Russian or English?")
                language_command = recognize_speech(recognizer, recognizer_language)
                if language_command is None:
                    continue
                if 'russian' in language_command or 'русский' in language_command:
                    recognizer_language = change_language_settings(engine, 'ru')
                elif 'english' in language_command or 'английский' in language_command:
                    recognizer_language = change_language_settings(engine, 'en')
            elif 'exit' in command or 'выйти' in command:
                speak(engine, "Goodbye!")
                break
            elif 'stop' in command or 'стоп' in command:
                speak(engine, "Program stopped.")
                break
            else:
                speak(engine, "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
