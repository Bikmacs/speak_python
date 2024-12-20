from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "8084208281:AAHDpjbA7Kj9CnSs0IKucCUKWz9tuBkrFR4"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text='Сортировка чисел'))
    keyboard.add(types.KeyboardButton(text='Сортировка по алфавиту'))
    return keyboard

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nчдкд?", reply_markup=get_keyboard())

@dp.message_handler(lambda message: message.text == "Сортировка чисел")
async def handle_sort_numbers(message: types.Message):
    await message.answer("Введите числа через пробел для сортировки:")

@dp.message_handler(lambda message: message.text == "Сортировка по алфавиту")
async def handle_sort_alphabet(message: types.Message):
    await message.answer("Введите слова через пробел для сортировки:")

@dp.message_handler()
async def handle_input(message: types.Message):
    try:
        numbers = list(map(int, message.text.split()))
        sorted_numbers = BubbleSort(numbers)
        await message.answer(f"Отсортированные числа: {sorted_numbers}")
    except ValueError:
        words = message.text.split()
        sorted_words = sorted(words)
        await message.answer(f"Отсортированные слова: {sorted_words}")
    await message.answer("Что вы хотите сделать дальше?", reply_markup=get_keyboard())

def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
