lang_ch = input(print("Your language is RUS or ENG (write it as in the question)"))

if lang_ch == "RUS":

    RUside1 = int(input(print("Введите 1 сторону прямоугольника")))
    RUside2 = int(input(print("Введите 2 сторону прямоугольника")))
    RUhigh = int(input(print("Введите высоту прямоугольника")))

    RUsquare = RUside1 * RUside2
    RUperimeter = 2 * (RUside1 + RUside2)
    RUvolume = RUside1 * RUside2 * RUhigh

    print(
        "Площадь прямоугольника:",
        RUsquare,
        "\nПериметр прямоугольника:",
        RUperimeter,
        "\nОбъем прямоугольника",
        RUvolume,
    )


elif lang_ch == "ENG":

    ENGside1 = int(input(print("Enter 1 side of the rectangle")))
    ENGside2 = int(input(print("Enter 2 side of the rectangle")))
    ENGhigh = int(input(print("Enter the height of the rectangle")))

    ENGsquare = ENGside1 * ENGside2
    ENGperimeter = 2 * (ENGside1 + ENGside2)
    ENGvolume = ENGside1 * ENGside2 * ENGhigh

    print(
        "Rectangle area:",
        ENGsquare,
        "\nRectangle perimeter:",
        ENGperimeter,
        "\nRectangle volume",
        ENGvolume,
    )
