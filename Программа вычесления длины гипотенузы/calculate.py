import check_calculate

def calculate_gipo(kat1: float, kat2:float) -> float :

    rezult = float("inf")

    if check_calculate.check_calculate_gipo(kat1, kat2):
        rezult = (kat1**kat2**2)**0.5
    
    return rezult


def main():
    kat1 = float(input("kat1= "))
    kat2 = float(input("kat2= "))
    print(calculate_gipo(kat1, kat2))
    

if __name__ == "__main__":
    main()

