import check_input
import calculate


def input_num(text_input:str) -> float:
    rezult = input(text_input)

    if check_input.check_float(rezult):
        rezult = float(rezult)
    else:
        print("Вы ввели не число, введите ещё раз \n")
        rezult = input_num(text_input)

    return rezult
    
    
def search_gipo():
    print()
    print("Назначение")
    
    katet = [-1, -1]

    for kat in range(2):
        text_input = "Введите катет" + str(kat+1) + ": "

        flag = True
        while flag:
            katet[kat] = input_num(text_input)
            if katet[kat]>0 and katet[kat] != float("inf"):
                flag = False
            elif katet[kat]<=0:
                print("Введите число больше 0")
            else:
                print("Вы ввели очень большое число, повторите ввод")

    rezult = calculate.calculate_gipo(katet[0], katet[1])
    if rezult == float("inf"):
        rezult = "Вычесление невозможно, вы ввели очень большие значения"

    print()
    if type(rezult) == str:
        print(rezult)
    else:
        print(f"Длина гипотенузы равна {rezult:.2f}")
    print()


def main():

    flag = True
    while flag:
        print("Хотите ли произвести вычисление?")
        end = input("Введите да/нет:")

        if end == "да":
            search_gipo()
        elif end == "нет":
            flag = False
        else:
            print("Команда не распознана, повторите ввод \n")
        print("программа заввершена")


if __name__ == "__main__":
    main()


