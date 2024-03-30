def menu(options: dict):
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")

    choice = int(input("Choose an option: ")) - 1
    options[tuple(options.keys())[choice]]()
