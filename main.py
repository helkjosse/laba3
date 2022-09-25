alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ'


def caesar_encrypt(text: str, shift: int):
    result = ""

    for char in text:
        index = alphabet.find(char)
        if index == -1:
            return "Ошибка, найден недопустимый символ: " + char
        else:
            new_index = index + shift
            new_index %= len(alphabet)
            result += alphabet[new_index:new_index + 1]

    return result


def caesar_decrypt(text: str, shift: int):
    result = ""

    for char in text:
        index = alphabet.find(char)
        if index == -1:
            return "Ошибка, найден недопустимый символ: " + char + ")"
        else:
            new_index = index - shift
            new_index %= len(alphabet)
            result += alphabet[new_index:new_index + 1]

    return result


if __name__ == '__main__':
    input_text = input("Введите текст (ТОЛЬКО латинские буквы): ")
    caesar_mode = int(input("Выберите режим (введите цифры):\n1 - зашифровать\n2 - расшифровать\n"))
    input_shift = int(input("Введите кол-во сдвигов: "))

    if caesar_mode == 1:
        print("Результат:", caesar_encrypt(input_text, input_shift))
    if caesar_mode == 2:
        print("Результат:", caesar_decrypt(input_text, input_shift))
    if caesar_mode != 1 and caesar_mode != 2:
        print("Режим под номером", caesar_mode, "не найден, перезапустите приложение")
