def check_calculate_gipo(kat1: float, kat2: float) -> bool:
    not_error = True

    try:
        (kat1**kat2**2)**0.5
    except OverflowError:
        not_error = False
    
    return not_error


def main():
    kat1=float(input("kat1= "))
    kat2=float(input("kat2= "))
    print(check_calkulate_gipo(kat1, kat2))


if __name__ == "__main__":
    main()    

