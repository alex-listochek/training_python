def check_float(text: str) -> bool:
    not_error = True

    try:
        float(text)
    except ValueError:
        not_error = False

    return not_error


def main():
    a=input("a= ")
    print(check_float(a), float(a))


if __name__ == "__main__":
    main()