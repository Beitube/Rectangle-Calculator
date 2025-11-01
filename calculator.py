from math import sqrt, sin, cos, tan, pi, e, pow

lang_ch = input(print("Your language is RUS or ENG (write it as in the question)"))

if lang_ch == "RUS" or lang_ch == "rus" or lang_ch == "РУС" or lang_ch == "рус":

    RUshape_ch = input(print("Выберите фигуру:(Круг, Прямоугольник)"))

    if RUshape_ch == "Прямоугольник" or RUshape_ch == "прямоугольник":

        RU_rectangleSide1 = int(input(print("Введите 1 сторону прямоугольника")))
        RU_rectangleSide2 = int(input(print("Введите 2 сторону прямоугольника")))
        RU_rectangleHigh = int(input(print("Введите высоту прямоугольника")))

        RU_rectangleSquare = RU_rectangleSide1 * RU_rectangleSide2
        RU_rectanglePerimeter = 2 * (RU_rectangleSide1 + RU_rectangleSide2)
        RU_rectangleVolume = RU_rectangleSide1 * RU_rectangleSide2 * RU_rectangleHigh

        print(
            "Площадь прямоугольника:",
            RU_rectangleSquare,
            "\nПериметр прямоугольника:",
            RU_rectanglePerimeter,
            "\nОбъем прямоугольника",
            RU_rectangleVolume,
        )

    elif RUshape_ch == "Круг" or RUshape_ch == "круг":
        RU_circleRadius = int(input(print("Введите радиус круга")))
        RU_circlegleDiameter = int(input(print("Введите диаметр круга")))

        RU_circleSquare = pi * pow(RU_circleRadius, 2)
        RU_circleLength = pi * RU_circlegleDiameter

        print("Площадь круга:", RU_circleSquare, "\nДлина окуржности:", RU_circleLength)
    else:
        print("Простите, эта фигура временно не поддерживается!")


elif lang_ch == "ENG" or lang_ch == "eng":

    ENGshape_ch = input(print("Choose the shape:(Circle, Rectangle)"))

    if ENGshape_ch == "Rectangle" or ENGshape_ch == "rectangle":

        ENG_rectangleSide1 = int(input(print("Enter 1 side of the rectangle")))
        ENG_rectangleSide2 = int(input(print("Enter 2 side of the rectangle")))
        ENG_rectangleHigh = int(input(print("Enter the height of the rectangle")))

        ENG_rectangleSquare = ENG_rectangleSide1 * ENG_rectangleSide2
        ENG_rectanglePerimeter = 2 * (ENG_rectangleSide1 + ENG_rectangleSide2)
        ENG_rectangleVolume = (
            ENG_rectangleSide1 * ENG_rectangleSide2 * ENG_rectangleHigh
        )

        print(
            "Rectangle area:",
            ENG_rectangleSquare,
            "\nRectangle perimeter:",
            ENG_rectanglePerimeter,
            "\nRectangle volume",
            ENG_rectangleVolume,
        )
    elif ENGshape_ch == "Circle" or ENGshape_ch == "circle":
        ENG_circleRadius = int(input(print("Enter circle radius")))
        ENG_circlegleDiameter = int(input(print("Enter diameter circle")))

        ENG_circleSquare = pi * pow(ENG_circleRadius, 2)
        ENG_circleLength = pi * ENG_circlegleDiameter

        print(
            "Square circle:", ENG_circleSquare, "\ncircumference length:", ENG_circleLength
        )
    else:
        print("Sorry, this figure is temporarily unsupported!")

else:
    print(
        "Sorry, this language is not supported!",
        "\n",
        "Простите, этот язык не поддерживается",
        sep="",
    )
