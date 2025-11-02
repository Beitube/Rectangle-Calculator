from math import sqrt, sin, cos, tan, pi, e, pow

lang_ch = input(print("Your language is RUS or ENG (write it as in the question)"))

if lang_ch == "RUS" or lang_ch == "rus" or lang_ch == "РУС" or lang_ch == "рус":

    shape_ch = input(
        print("Выберите фигуру:(Круг, Прямоугольник, Квадрат, Треугольник)")
    )

    if shape_ch == "Прямоугольник" or shape_ch == "прямоугольник":

        rectangleSide1 = float(input(print("Введите 1 сторону прямоугольника")))
        rectangleSide2 = float(input(print("Введите 2 сторону прямоугольника")))

        rectangleSquare = rectangleSide1 * rectangleSide2
        rectanglePerimeter = 2 * (rectangleSide1 + rectangleSide2)
        rectangleDiagonal = sqrt(pow(rectangleSide1, 2) + pow(rectangleSide2, 2))

        print(
            "Площадь прямоугольника:",
            rectangleSquare,
            "\nПериметр прямоугольника:",
            rectanglePerimeter,
            "\nДлина диагонали",
            rectangleDiagonal,
        )

    elif shape_ch == "Круг" or shape_ch == "круг":
        circleRadius = float(input(print("Введите радиус круга")))
        circlegleDiameter = float(input(print("Введите диаметр круга")))

        circleSquare = pi * pow(circleRadius, 2)
        circleLength = pi * circlegleDiameter

        print("Площадь круга:", circleSquare, "\nДлина окуржности:", circleLength)

    elif shape_ch == "Квадрат" or shape_ch == "квадрат":
        squareSide1 = float(input(print("Введите 1 сторону квадрата")))
        squareSide2 = float(input(print("Введите 2 сторону квадрата")))

        x2Square = squareSide1 * squareSide2
        squarePerimeter = 2 * (squareSide1 + squareSide2)
        squareDiagonal = sqrt(pow(squareSide1, 2) + pow(squareSide2, 2))

        print(
            "Площадь прямоугольника:",
            x2Square,
            "\nПериметр прямоугольника:",
            squarePerimeter,
            "\nДлина диагонали",
            squareDiagonal,
        )
    elif shape_ch == "Треугольник" or shape_ch == "треугольник":
        triangleA = input(
            print(
                'Введите сторону A треугольника(если вам она неизвестна введите "-", без кавычек)'
            )
        )
        triangleB = input(
            print(
                'Введите сторону B треугольника(если вам она неизвестна введите "-", без кавычек)'
            )
        )
        triangleC = input(
            print(
                'Введите сторону C треугольника(если вам она неизвестна введите "-", без кавычек)'
            )
        )

        triangleUnknown_count = 0
        if triangleA == "-":
            triangleUnknown_count += 1
        if triangleB == "-":
            triangleUnknown_count += 1
        if triangleC == "-":
            triangleUnknown_count += 1

        if triangleUnknown_count == 0:

            triangleA = int(triangleA)
            triangleB = int(triangleB)
            triangleC = int(triangleC)

            trianglePerimeter = triangleA + triangleB + triangleC

            if (
                triangleA == triangleB and triangleB == triangleC
            ):  # Равносторонний треуголник
                triangleSquare = (sqrt(3) * pow(triangleA, 2)) / 4

                print(
                    "Площадь равностороннего треугольника:",
                    triangleSquare,
                    "\nПериметр равносторннего треугольника:",
                    trianglePerimeter,
                )
            elif (
                triangleA == triangleB
                or triangleB == triangleC
                or triangleA == triangleC
            ):  # Равнобедренный треугольник

                if triangleA == triangleB:
                    traingleBase = triangleC
                    sideA = triangleA
                    sideB = triangleB
                elif triangleA == triangleC:
                    traingleBase = triangleB
                    sideA = triangleA
                    sideB = triangleC
                else:
                    traingleBase = triangleA
                    sideA = triangleC
                    sideB = triangleB

                triangleHigh = sqrt((pow(sideA, 2) - pow((sideB / 2), 2)))
                triangleSquare = 0.5 * traingleBase * triangleHigh

                print(
                    "Площадь равнобедренного треугольника:",
                    triangleSquare,
                    "\nПериметр равнобедренного треугольника:",
                    trianglePerimeter,
                    "\nВысота равнобедренного треугольника",
                    triangleHigh,
                )
            else:
                trangleHalfPerimeter = trianglePerimeter / 2
                triangleSquare = sqrt(
                    (
                        trangleHalfPerimeter
                        * (trangleHalfPerimeter - triangleA)
                        * (trangleHalfPerimeter - triangleB)
                        * (trangleHalfPerimeter - triangleC)
                    )
                )

                print(
                    "Площадь треугольника:",
                    triangleSquare,
                    "\nПериметр треугольника:",
                    trianglePerimeter,
                    "\nПолупериметр треугольника",
                    trangleHalfPerimeter,
                )

        elif triangleUnknown_count == 1:
            if triangleA == "-":
                triangleB = float(triangleB)
                triangleC = float(triangleC)
           
                triangleAngleA = input(print('Введите угол между 2 известными вам сторонами(если угол вам неизвестен введите "-" без кавычек) ')) 
                triangleAngleB = input(print('Введите угол напротив одной известной вам стороны(если угол вам неизвестен введите "-" без кавычек) '))  

                if triangleAngleA != "-":
                    triangleAngleA = float(triangleAngleA)
                    triangleSquare = 0.5 * triangleB * triangleC * sin(triangleAngleA)
                    
                    print(
                    "Площадь треугольника:",
                    triangleSquare,
                    )
                elif triangleAngleB != "-":
                    SINtriangleAngleA = (triangleB  * sin(triangleAngleB)) / triangleC

                    if SINtriangleAngleA > 1:
                        print("Треугольника не существует!")   
                    elif SINtriangleAngleA == 1:
                        triangleAngleA = float(triangleAngleA) 
                        triangleAngleA = 90 # прямоугольный треугольник

                        triangleSquare = 0.5 * triangleB * triangleC * sin(triangleAngleA)
                    
                        print(
                            "Площадь треугольника:",
                            triangleSquare,
                        )
                    elif  SINtriangleAngleA < 1:
                        print("Временно не поддерживается")

            elif triangleB == "-":
                float(sideA) = triangleA
                float(sideB) = triangleC

                triangleAngleA = input(print('Введите угол между 2 известными вам сторонами(если угол вам неизвестен введите "-" без кавычек) ')) 
                triangleAngleB = input(print('Введите угол напротив одной известной вам стороны(если угол вам неизвестен введите "-" без кавычек) '))  

                if triangleAngleA != "-":
                    triangleAngleA = float(triangleAngleA)
                    triangleSquare = 0.5 * triangleB * triangleC * sin(triangleAngleA)
                    
                    print(
                    "Площадь треугольника:",
                    triangleSquare,
                    )
                elif triangleAngleB != "-":
                    SINtriangleAngleA = (triangleB  * sin(triangleAngleB)) / triangleC

                    if SINtriangleAngleA > 1:
                        print("Треугольника не существует!")   
                    elif SINtriangleAngleA == 1:
                        triangleAngleA = float(triangleAngleA) 
                        triangleAngleA = 90 # прямоугольный треугольник

                        triangleSquare = 0.5 * triangleB * triangleC * sin(triangleAngleA)
                    
                        print(
                            "Площадь треугольника:",
                            triangleSquare,
                        )
                    elif  SINtriangleAngleA < 1:
                        print("Временно не поддерживается")
            elif triangleC == "-":
                float(sideA) = triangleA
                float(sideB) = triangleB   

                triangleAngleA = input(print('Введите угол между 2 известными вам сторонами(если угол вам неизвестен введите "-" без кавычек) ')) 
                triangleAngleB = input(print('Введите угол напротив одной известной вам стороны(если угол вам неизвестен введите "-" без кавычек) '))  

                if triangleAngleA != "-":
                    triangleAngleA = float(triangleAngleA)
                    triangleSquare = 0.5 * triangleB * triangleC * sin(triangleAngleA)
                    
                    print(
                    "Площадь треугольника:",
                    triangleSquare,
                    )
                elif triangleAngleB != "-":
                    SINtriangleAngleA = (triangleB  * sin(triangleAngleB)) / triangleC

                    if SINtriangleAngleA > 1:
                        print("Треугольника не существует!")   
                    elif SINtriangleAngleA == 1:
                        triangleAngleA = float(triangleAngleA) 
                        triangleAngleA = 90 # прямоугольный треугольник

                        triangleSquare = 0.5 * triangleB * triangleC * sin(triangleAngleA)
                    
                        print(
                            "Площадь треугольника:",
                            triangleSquare,
                        )
                    elif  SINtriangleAngleA < 1:
                        print("Временно не поддерживается") 
        else:
            print("Простите, но для подсчета недостаточно данных")
    else:
        print("Простите, эта фигура временно не поддерживается!")


elif lang_ch == "ENG" or lang_ch == "eng":

    shape_ch = input(print("Choose the shape:(Circle, Rectangle, Square)"))

    if shape_ch == "Rectangle" or shape_ch == "rectangle":

        rectangleSide1 = float(input(print("Enter 1 side of the rectangle")))
        rectangleSide2 = float(input(print("Enter 2 side of the rectangle")))
        rectangleHigh = float(input(print("Enter the height of the rectangle")))

        rectangleSquare = rectangleSide1 * rectangleSide2
        rectanglePerimeter = 2 * (rectangleSide1 + rectangleSide2)
        rectangleDiagonal = sqrt(pow(rectangleSide1, 2) + pow(rectangleSide2, 2))

        print(
            "Rectangle area:",
            rectangleSquare,
            "\nRectangle perimeter:",
            rectanglePerimeter,
            "\nRectangle diagonale",
            rectangleDiagonal,
        )
    elif shape_ch == "Circle" or shape_ch == "circle":
        circleRadius = int(input(print("Enter circle radius")))
        circlegleDiameter = int(input(print("Enter diameter circle")))

        circleSquare = pi * pow(circleRadius, 2)
        circleLength = pi * circlegleDiameter

        print(
            "Square circle:",
            circleSquare,
            "\nCircumference length:",
            circleLength,
        )
    elif shape_ch == "Square" or shape_ch == "square":
        squareSide1 = float(input(print("Enter 1 side of the square")))
        squareSide2 = float(input(print("Enter 2 side of the square")))

        x2Square = squareSide1 * squareSide2
        squarePerimeter = 2 * (squareSide1 + squareSide2)
        squareDiagonal = sqrt(pow(squareSide1, 2) + pow(squareSide2, 2))

        print(
            "Square area:",
            x2Square,
            "\nПSquare perimeter:",
            squarePerimeter,
            "\nSquare diagonale",
            squareDiagonal,
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
