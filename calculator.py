class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def result(self):
        print('The result of is:')
class Calculation_Operator:
    def __init__(self):
        self.operator()

    def operator(self):
        num1 = float(input("Enter the first number: "))
        operation_dict = {
            '+' : Sum,
            '-' : Subtract,
            '*' : Multiply,
            '/' : Divide,
            '%' : Modulus,
            '**': Exponentiation
        }

        for symble in operation_dict:
           print(symble)
        ob_symble = input('Pick an operation: ')

        continue_ = 0
        while continue_ != "x":
            num2 = float(input('Enter the next number: '))
            Calculator(num1, num1)
            if ob_symble == '+':
                ob = Sum
                b = ob.add(self, num1, num2)
            elif ob_symble == '-':
                ob = Subtract
                b = ob.sub(self, num1, num2)
            elif ob_symble == '*':
                ob = Multiply
                b = ob.mul(self, num1, num2)
            elif ob_symble == '/':
                ob = Divide
                b = ob.divide(self, num1, num2)
            elif ob_symble == '%':
                ob = Modulus
                b = ob.mod(self, num1, num2)
            elif ob_symble == '**':
                ob = Exponentiation
                b = ob.exp(self, num1, num2)
            else:
                print("Error: Please enter '+', '-', '*', '/', '%', '**' the operator did not found.")
                break
            calculator_function = operation_dict[ob_symble]
            output = b
            print(f'{num1} {ob_symble} {num2} = {b}')
            continue_ = input(
                f"\n\tEnter 'y' to continue with {output} or 'n' to start a new calculation or enter 'x' to exit: ").lower()

            if continue_ == 'y':
                num1 = output
                for symble in operation_dict:
                        print(symble)
                ob_symble = input('Pick an operation: ')
            elif continue_ == 'n':
                Calculation_Operator()
                break
            else:
                continue_ =='x'
                #print("Good bye")
                print('\n\t\tCalculator (Made by Kanishka Noori)')
                print('---------------------------------------------------')
                print("Enter '1' for '+', '-', '*', '/', '%' ,'**' operation.")
                print("Enter '2' for trigonometric function.")
                print("Enter '3' for display the 'e' and 'pi' values.")
                print("Enter '4' for calculate the area of 'Circle', 'Square', 'Rectangle' and 'Triangle' .")

                number = input('\n \tEnter the number of operation that you want: ')
                if number == "1":
                    Calculation_Operator() == True
                elif number == "2":
                    Trigonometric_fucntions() == True
                elif number == "3":
                    ConstantValues() == True
                elif number == "4":
                    Area() == True
                else:
                    print('Error: Please enter a number between 1-4!')


class Sum(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def add(self, num1, num2):
        return num1 + num2

class Subtract(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def sub(self, num1, num2):
            return num1 - num2

class Multiply(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def mul(self, num1, num2):
            return num1 * num2

class Divide(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def divide(self, num1, num2):
            return num1 / num2

class Modulus(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def mod(self, num1, num2):
            return num1 % num2

class Exponentiation(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def exp(self, num1, num2):
            return num1 ** num2

class Trigonometric_fucntions(Calculator):
    def __init__(self):
        self.Operator1()


    def Operator1(self):

        operation_dict1 = {
            'sin': Sin,
            'cos': Cos,
            'tan': Tan
        }
        for symble1 in operation_dict1:
           print(symble1)
        ob_symble1 = input('Pick an operation: ')
        continue_ = 0
        while continue_ != "x":
            if ob_symble1 == 'sin':
                num1 = int(input("Enter the amount of a popular degree: "))
                ob1 = Sin(num1)
                b = ob1.result(num1)
            elif ob_symble1 == 'cos':
                num1 = int(input("Enter the amount of a popular degree: "))
                ob1 = Cos(num1)
                b = ob1.result(num1)
            elif ob_symble1 == 'tan':
                num1 = int(input("Enter the amount of a popular degree: "))
                ob1 = Tan(num1)
                b = ob1.result(num1)
            else:
                print("Error: Not a trigonomic fucntion!")
                break

            Trigonometric_fucntions = operation_dict1[ob_symble1]
            output = b
            #print(f'{ob_symble1}{num1} = {b}')
            continue_ = input(
                f"\n\tEnter 'n' to start a new calculation or enter 'x' to exit: ").lower()

            if continue_ == 'n':
                Trigonometric_fucntions(num1)
                for symble1 in operation_dict1:
                    print(symble1)
                ob_symble1 = input('Pick an operation: ')
            else:
                print('Good Bye!')
                print('\n\t\tCalculator (Made by Kanishka Noori)')
                print('---------------------------------------------------')
                print("Enter '1' for '+', '-', '*', '/', '%' ,'**' operation.")
                print("Enter '2' for trigonometric function.")
                print("Enter '3' for display the 'e' and 'pi' values.")
                print("Enter '4' for calculate the area of 'Circle', 'Square', 'Rectangle' and 'Triangle' .")

                number = input('\n \tEnter the number of operation that you want: ')
                if number == "1":
                    Calculation_Operator() == True
                elif number == "2":
                    Trigonometric_fucntions() == True
                elif number == "3":
                    ConstantValues() == True
                elif number == "4":
                    Area() == True
                else:
                    print('Error: Please enter a number between 1-4!')


class Sin(Trigonometric_fucntions):
    def __init__(self, num1):
        #super().__init__(self,num1)
        self.num1 = num1


    def result(self, num1):
        if self.num1 == 0:
            print("sin0 = 0")
            return self.num1
        elif self.num1 == 30:
            print('sin30 = 0.5')
            return self.num1
        elif self.num1 == 60:
            print('sin60 = 0.8660254038')
            return self.num1
        elif self.num1 == 45:
            print('sin45 = 0.7071067812')
            return self.num1
        elif self.num1 == 90:
            print('sin90 = 1')
            return self.num1
        elif self.num1 == 120:
            print('sin120 = 0.8660254038')
            return self.num1
        elif self.num1 == 135:
            print('sin135 = 0.7071067812')
            return self.num1
        elif self.num1 == 150:
            print('sin150 = 0.5')
            return self.num1
        elif self.num1 == 180:
            print('sin180 = 0')
            return self.num1
        elif self.num1 == 210:
            print('sin210 = -0.5')
            return self.num1
        elif self.num1 == 225:
            print('sin225 = -0.7071067812')
            return self.num1
        elif self.num1 == 240:
            print('sin240 = -0.8660254038')
            return self.num1
        elif self.num1 == 270:
            print('sin270 = -1')
            return self.num1
        elif self.num1 == 300:
            print('sin300 = -0.8660254038')
            return self.num1
        elif self.num1 == 315:
            print('sin315 = -0.7071067812')
            return self.num1
        elif self.num1 == 330:
            print('sin330 = -0.5')
            return self.num1
        elif self.num1 == 360:
            print('sin360 = 0')
            return self.num1
        elif self.num1 == -30:
            print('sin(-30) = -0.5')
            return self.num1
        elif self.num1 == -45:
            print('sin(-45) = -0.7071067812')
            return self.num1
        elif self.num1 == -60:
            print('sin(-60) = -0.8660254038')
            return self.num1
        elif self.num1 == -90:
            print('sin(-90) = -1')
            return self.num1
        elif self.num1 == -120:
            print('sin(-120) = -0.8660254038')
            return self.num1
        elif self.num1 == -135:
            print('sin(-135) = -0.7071067812')
            return self.num1
        elif self.num1 == -150:
            print('sin(-150) = -0.5')
            return self.num1
        elif self.num1 == -180:
            print('sin(-180) = 0')
            return self.num1
        elif self.num1 == -210:
            print('sin(-210) = 0.5')
            return self.num1
        elif self.num1 == -225:
            print('sin(-225) = 0.7071067812')
            return self.num1
        elif self.num1 == -240:
            print('sin(-240) = 0.8660254038')
            return self.num1
        elif self.num1 == -270:
            print('sin(-270) = 1')
            return self.num1
        elif self.num1 == -300:
            print('sin(-300) = 0.8660254038')
            return self.num1
        elif self.num1 == -315:
            print('sin(-315) = 0.7071067812')
            return self.num1
        elif self.num1 == -330:
            print('sin(-330) = 0.5')
            return self.num1
        elif self.num1 == -360:
            print('sin(-360) = 0')
            return self.num1
        elif self.num1 > 360:
            number = num1 % 360
            if number == 0:
                print(f'sin', num1, '= 0')
            elif number == 30:
                print(f'sin',num1, '= 0.5')
            elif number == 45:
                print(f'sin',num1, '= 0.7071067812')
            elif number == 60:
                print(f'sin',num1, '= 0.8660254038')
            elif number == 90:
                print(f'sin',num1, '= 1')
            elif number == 120:
                print(f'sin',num1, '= 0.8660254038')
            elif number == 135:
                print(f'sin',num1, '= 0.7071067812')
            elif number == 150:
                print(f'sin',num1, '= 0.5')
            elif number == 180:
                print(f'sin',num1, '= 0')
            elif number == 210:
                print(f'sin',num1, '= -0.5')
            elif number == 225:
                print(f'sin',num1, '= -0.7071067812')
            elif number == 240:
                print(f'sin',num1, '= -0.8660254038')
            elif number == 270:
                print(f'sin',num1, '= -1')
            elif number == 300:
                print(f'sin',num1, '= -0.8660254038')
            elif number == 315:
                print(f'sin',num1, '= -0.7071067812')
            elif number == 330:
                print(f'sin',num1, '= -0.5')
            else:
                print("Not a popular degree!")
        elif self.num1 < 360:
            number = num1 * -1 % 360
            if number == 0:
                print(f'sin', num1, '= 0')
            elif number == 30:
                print(f'sin',num1, '= -0.5')
            elif number == 45:
                print(f'sin',num1, '= -0.7071067812')
            elif number == 60:
                print(f'sin',num1, '= -0.8660254038')
            elif number == 90:
                print(f'sin',num1, '= -1')
            elif number == 120:
                print(f'sin',num1, '= -0.8660254038')
            elif number == 135:
                print(f'sin',num1, '= -0.7071067812')
            elif number == 150:
                print(f'sin',num1, '= -0.5')
            elif number == 180:
                print(f'sin',num1, '= 0')
            elif number == 210:
                print(f'sin',num1, '= 0.5')
            elif number == 225:
                print(f'sin',num1, '= 0.7071067812')
            elif number == 240:
                print(f'sin',num1, '= 0.8660254038')
            elif number == 270:
                print(f'sin',num1, '= 1')
            elif number == 300:
                print(f'sin',num1, '= 0.8660254038')
            elif number == 315:
                print(f'sin',num1, '= 0.7071067812')
            elif number == 330:
                print(f'sin',num1, '= 0.5')
            else:
                print("Not a popular degree!")
        else:
            print("Not a popular degree!")

class Cos(Trigonometric_fucntions):
    def __init__(self, num1):
        #super().__init__(self,num1)
        self.num1 = num1

    def result(self, num1):
        if self.num1 == 0:
            print("cos0 = 1")
            return self.num1
        elif self.num1 == 30:
            print('cos30 = 0.8660254038')
            return self.num1
        elif self.num1 == 60:
            print('cos60 = 0.5')
            return self.num1
        elif self.num1 == 45:
            print('cos45 = 0.7071067812')
            return self.num1
        elif self.num1 == 90:
            print('cos90 = 0')
            return self.num1
        elif self.num1 == 120:
            print('cos120 = -0.5')
            return self.num1
        elif self.num1 == 135:
            print('cos135 = -0.7071067812')
            return self.num1
        elif self.num1 == 150:
            print('cos150 = -0.8660254038')
            return self.num1
        elif self.num1 == 180:
            print('cos180 = -1')
            return self.num1
        elif self.num1 == 210:
            print('cos210 = -0.8660254038')
            return self.num1
        elif self.num1 == 225:
            print('cos225 = -0.7071067812')
            return self.num1
        elif self.num1 == 240:
            print('cos240 = -0.5')
            return self.num1
        elif self.num1 == 270:
            print('cos270 = 0')
            return self.num1
        elif self.num1 == 300:
            print('cos300 = 0.5')
            return self.num1
        elif self.num1 == 315:
            print('cos315 = 0.7071067812')
            return self.num1
        elif self.num1 == 330:
            print('cos330 = 0.8660254038')
            return self.num1
        elif self.num1 == 360:
            print('cos360 = 1')
            return self.num1
        elif self.num1 == -30:
            print('cos(-30) = 0.8660254038')
            return self.num1
        elif self.num1 == -45:
            print('cos(-45) = 0.7071067812')
            return self.num1
        elif self.num1 == -60:
            print('cos(-60) = 0.5')
            return self.num1
        elif self.num1 == -90:
            print('cos(-90) = 0')
            return self.num1
        elif self.num1 == -120:
            print('cos(-120) = -0.5')
            return self.num1
        elif self.num1 == -135:
            print('cos(-135) = -0.7071067812')
            return self.num1
        elif self.num1 == -150:
            print('cos(-150) = -0.8660254038')
            return self.num1
        elif self.num1 == -180:
            print('cos(-180) = -1')
            return self.num1
        elif self.num1 == -210:
            print('cos(-210) = -0.8660254038')
            return self.num1
        elif self.num1 == -225:
            print('cos(-225) = -0.7071067812')
            return self.num1
        elif self.num1 == -240:
            print('cos(-240) = -0.5')
            return self.num1
        elif self.num1 == -270:
            print('cos(-270) = 0')
            return self.num1
        elif self.num1 == -300:
            print('cos(-300) = 0.5')
            return self.num1
        elif self.num1 == -315:
            print('cos(-315) = 0.7071067812')
            return self.num1
        elif self.num1 == -330:
            print('cos(-330) = 0.8660254038')
            return self.num1
        elif self.num1 == -360:
            print('cos(-360) = 1')
            return self.num1
        elif self.num1 > 360:
            number = num1 % 360
            if number == 0:
                print(f'cos', num1, '= 1')
            elif number == 30:
                print(f'cos', num1, '= 0.8660254038')
            elif number == 45:
                print(f'cos', num1, '= 0.7071067812')
            elif number == 60:
                print(f'cos', num1, '= 0.5')
            elif number == 90:
                print(f'cos', num1, '= 0')
            elif number == 120:
                print(f'cos', num1, '= -0.5')
            elif number == 135:
                print(f'cos', num1, '= -0.7071067812')
            elif number == 150:
                print(f'cos', num1, '= -0.8660254038')
            elif number == 180:
                print(f'cos', num1, '= -1')
            elif number == 210:
                print(f'cos', num1, '= -0.8660254038')
            elif number == 225:
                print(f'cos', num1, '= -0.7071067812')
            elif number == 240:
                print(f'cos', num1, '= -0.5')
            elif number == 270:
                print(f'cos', num1, '= 0')
            elif number == 300:
                print(f'cos', num1, '= 0.5')
            elif number == 315:
                print(f'cos', num1, '= 0.7071067812')
            elif number == 330:
                print(f'cos', num1, '= 0.8660254038')
            else:
                print("Not a popular degree!")
        elif self.num1 < 360:
            number = num1 * -1 % 360
            if number == 0:
                print(f'cos', num1, '= 1')
            elif number == 30:
                print(f'cos', num1, '= 0.8660254038')
            elif number == 45:
                print(f'cos', num1, '= 0.7071067812')
            elif number == 60:
                print(f'cos', num1, '= 0.5')
            elif number == 90:
                print(f'cos', num1, '= 0')
            elif number == 120:
                print(f'cos', num1, '= -0.5')
            elif number == 135:
                print(f'cos', num1, '= -0.7071067812')
            elif number == 150:
                print(f'cos', num1, '= -0.8660254038')
            elif number == 180:
                print(f'cos', num1, '= -1')
            elif number == 210:
                print(f'cos', num1, '= -0.8660254038')
            elif number == 225:
                print(f'cos', num1, '= -0.7071067812')
            elif number == 240:
                print(f'cos', num1, '= -0.5')
            elif number == 270:
                print(f'cos', num1, '= 0')
            elif number == 300:
                print(f'cos', num1, '= 0.5')
            elif number == 315:
                print(f'cos', num1, '= 0.7071067812')
            elif number == 330:
                print(f'cos', num1, '= 0.8660254038')
            else:
                print("Not a popular degree!")
        else:
            print("Not a popular degree!")


class Tan(Trigonometric_fucntions):

    def __init__(self, num1):
        #super().__init__(self,num1)
        self.num1 = num1

    def result(self, num1):
        if self.num1 == 0:
            print("tan0 = 0")
            return self.num1
        elif self.num1 == 30:
            print('tan30 = 0.5773502692')
            return self.num1
        elif self.num1 == 60:
            print('tan60 = 1.7320508076')
            return self.num1
        elif self.num1 == 45:
            print('tan45 = 1')
            return self.num1
        elif self.num1 == 90:
            print('tan90 = undefined')
            return self.num1
        elif self.num1 == 120:
            print('tan120 = -1.7320508076')
            return self.num1
        elif self.num1 == 135:
            print('tan135 = -1')
            return self.num1
        elif self.num1 == 150:
            print('tan150 = -0.5773502692')
            return self.num1
        elif self.num1 == 180:
            print('tan180 = 0')
            return self.num1
        elif self.num1 == 210:
            print('tan210 = 0.5773502692')
            return self.num1
        elif self.num1 == 225:
            print('tan225 = 1')
            return self.num1
        elif self.num1 == 240:
            print('tan240 = 1.7320508076')
            return self.num1
        elif self.num1 == 270:
            print('tan270 = undefined')
            return self.num1
        elif self.num1 == 300:
            print('tan300 = -1.7320508076')
            return self.num1
        elif self.num1 == 315:
            print('tan315 = -1')
            return self.num1
        elif self.num1 == 330:
            print('tan330 = -0.5773502692')
            return self.num1
        elif self.num1 == 360:
            print('tan360 = 0')
            return self.num1
        elif self.num1 == -30:
            print('tan(-30) = -0.5773502692')
            return self.num1
        elif self.num1 == -45:
            print('tan(-45) = -1')
            return self.num1
        elif self.num1 == -60:
            print('tan(-60) = -1.7320508076')
            return self.num1
        elif self.num1 == -90:
            print('tan(-90) = undefined')
            return self.num1
        elif self.num1 == -120:
            print('tan(-120) = 1.7320508076')
            return self.num1
        elif self.num1 == -135:
            print('tan(-135) = 1')
            return self.num1
        elif self.num1 == -150:
            print('tan(-150) = 0.5773502692')
            return self.num1
        elif self.num1 == -180:
            print('tan(-180) = 0')
            return self.num1
        elif self.num1 == -210:
            print('tan(-210) = -0.5773502692')
            return self.num1
        elif self.num1 == -225:
            print('tan(-225) = -1')
            return self.num1
        elif self.num1 == -240:
            print('tan(-240) = -1.7320508076')
            return self.num1
        elif self.num1 == -270:
            print('tan(-270) = undefined')
            return self.num1
        elif self.num1 == -300:
            print('tan(-300) = 1.7320508076')
            return self.num1
        elif self.num1 == -315:
            print('tan(-315) = 1')
            return self.num1
        elif self.num1 == -330:
            print('tan(-330) = 0.5773502692')
            return self.num1
        elif self.num1 == -360:
            print('tan(-360) = 0')
            return self.num1
        elif self.num1 > 360:
            number = num1 % 360
            if number == 0:
                print(f'tan', num1, '= 0')
            elif number == 30:
                print(f'tan', num1, '= 0.5773502692')
            elif number == 45:
                print(f'tan', num1, '= 1')
            elif number == 60:
                print(f'tan', num1, '= 1.7320508076')
            elif number == 90:
                print(f'tan', num1, '= undefined')
            elif number == 120:
                print(f'tan', num1, '= -1.7320508076')
            elif number == 135:
                print(f'tan', num1, '= -1')
            elif number == 150:
                print(f'tan', num1, '= -0.5773502692')
            elif number == 180:
                print(f'tan', num1, '= 0')
            elif number == 210:
                print(f'tan', num1, '= 0.5773502692')
            elif number == 225:
                print(f'tan', num1, '= 1')
            elif number == 240:
                print(f'tan', num1, '= 1.7320508076')
            elif number == 270:
                print(f'tan', num1, '= undefined')
            elif number == 300:
                print(f'tan', num1, '= -1.7320508076')
            elif number == 315:
                print(f'tan', num1, '= -1')
            elif number == 330:
                print(f'tan', num1, '= -0.5773502692')
            else:
                print("Not a popular degree!")
        elif self.num1 < 360:
            number = num1 * -1 % 360
            if number == 0:
                print(f'tan', num1, '= 0')
            elif number == 30:
                print(f'tan', num1, '= -0.5773502692')
            elif number == 45:
                print(f'tan', num1, '= -1')
            elif number == 60:
                print(f'tan', num1, '= -1.7320508076')
            elif number == 90:
                print(f'tan', num1, '= undefined')
            elif number == 120:
                print(f'tan', num1, '= 1.7320508076')
            elif number == 135:
                print(f'tan', num1, '= 1')
            elif number == 150:
                print(f'tan', num1, '= 0.5773502692')
            elif number == 180:
                print(f'tan', num1, '= 0')
            elif number == 210:
                print(f'tan', num1, '= -0.5773502692')
            elif number == 225:
                print(f'tan', num1, '= -1')
            elif number == 240:
                print(f'tan', num1, '= -1.7320508076')
            elif number == 270:
                print(f'tan', num1, '= undefined')
            elif number == 300:
                print(f'tan', num1, '= 1.7320508076')
            elif number == 315:
                print(f'tan', num1, '= 1')
            elif number == 330:
                print(f'tan', num1, '= 0.5773502692')
            else:
                print("Not a popular degree!")
        else:
            print("Not a popular degree!")

class ConstantValues:
    def __init__(self):
        self.operator2()

    def operator2(self):
        operation_dict2 = {
            'e' : Euler,
            'pi' : Pi
        }

        for symble2 in operation_dict2:
           print(symble2)

        ob_symble = input('Pick an operation: ').lower()
        continue_ = 0
        while continue_ != 'x':
            if ob_symble == 'e':
                ob = Euler
                b = ob.result(self)
            elif ob_symble == 'pi':
                ob = Pi
                b = ob.result(self)
            else:
                print("Error: Please enter 'e' or 'pi'!")
                break
            calculator_function = operation_dict2[ob_symble]
            output = b
            continue_ = input(
                f"\n\tEnter 'n' to start a new calculation or enter 'x' to exit: ").lower()

            if continue_ == 'n':
                ConstantValues()
            else:
                continue_ == 'x'
                #print("Good bye")
                print('\n\t\tCalculator (Made by Kanishka Noori)')
                print('---------------------------------------------------')
                print("Enter '1' for '+', '-', '*', '/', '%' ,'**' operation.")
                print("Enter '2' for trigonometric function.")
                print("Enter '3' for display the 'e' and 'pi' values.")
                print("Enter '4' for calculate the area of 'Circle', 'Square', 'Rectangle' and 'Triangle' .")

                number = input('\n \tEnter the number of operation that you want: ')
                if number == "1":
                    Calculation_Operator() == True
                elif number == "2":
                    Trigonometric_fucntions() == True
                elif number == "3":
                    ConstantValues() == True
                elif number == "4":
                    Area() == True
                else:
                    print('Error: Please enter a number between 1-4!')


class Euler(ConstantValues):
    def result(self):
        print('e = 2.7182818285')

class Pi(ConstantValues):
    def result(self):
        print('pi = 3.1415926536')

class Area:
    def __init__(self):
        self.operator3()

    def operator3(self):
        operation_dict3 = {
            "Enter '1' for calculating the area of 'Circle'." : Circle_Area,
            "Enter '2' for calculating the area of 'Square'." : Square_Area,
            "Enter '3' for calculating the area of 'Rectangle'.": Rectangle_Area,
            "Enter '4' for calculating the area of 'Triangle'.": Triangle_Area
        }

        for symble3 in operation_dict3:
           print(symble3)
        ob_symble = input('The area of which shape do you want calculate: ')

        continue_ = 0
        while continue_ != "x":
            if ob_symble == '1':
                num1 = float(input("Enter the amount of radius: "))
                ob = Circle_Area
                b = ob.c_area(self,num1)
            elif ob_symble == '2':
                 num1 = float(input("Enter the size of side of Square: "))
                 ob = Square_Area
                 b = ob.s_area(self, num1)
            elif ob_symble == '3':
                num1 = float(input("Enter the size of the one side of rectangle: "))
                num2 = float(input("Enter the size of another side of rectangle: "))
                ob = Rectangle_Area
                b = ob.r_area(self, num1, num2)
            elif ob_symble == '4':
                num1 = float(input("Enter the size of the height of Triangle: "))
                num2 = float(input("Enter the size of the base of Triangle: "))
                ob = Triangle_Area
                b = ob.t_area(self, num1, num2)
            else:
                print("Error: Please enter '1', '2', '3', '4' the operator did not found.")
                break

            continue_ = input(
                f"\n\tEnter 'n' to start a new calculation or enter 'x' to exit: ").lower()

            if continue_ == 'n':
                Area()
                break
            else:
                continue_ == 'x'
                #print("Good bye")
                print('\n\t\tCalculator (Made by Kanishka Noori)')
                print('---------------------------------------------------')
                print("Enter '1' for '+', '-', '*', '/', '%' ,'**' operation.")
                print("Enter '2' for trigonometric function.")
                print("Enter '3' for display the 'e' and 'pi' values.")
                print("Enter '4' for calculate the area of 'Circle', 'Square', 'Rectangle' and 'Triangle' .")

                number = input('\n \tEnter the number of operation that you want: ')
                if number == "1":
                    Calculation_Operator() == True
                elif number == "2":
                    Trigonometric_fucntions() == True
                elif number == "3":
                    ConstantValues() == True
                elif number == "4":
                    Area() == True
                else:
                    print('Error: Please enter a number between 1-4!')

class Circle_Area(Area):
    def c_area(self, num1):
            b = 3.14 * num1 ** 2
            print(f"The area of circle that have {num1} radius is {b}.")

class Square_Area(Area):
    def s_area(self, num1):
            b = num1 * num1
            print(f"The area of square that have {num1} length of side is {b}.")

class Rectangle_Area(Area):
    def r_area(self,num1,num2):
        b = num1 * num2
        print(f"The area of rectangle that have {num1} and {num2} is {b}.")

class Triangle_Area(Area):
    def t_area(self,num1,num2):
        b = 0.5 * num1 * num2
        print(f"The area of Triangle that have {num1} height and {num2} base is {b}.")

print('\n\t\tCalculator (Made by Kanishka Noori)')
print('---------------------------------------------------')
print("Enter '1' for '+', '-', '*', '/', '%' ,'**' operation.")
print("Enter '2' for trigonometric function.")
print("Enter '3' for display the 'e' and 'pi' values.")
print("Enter '4' for calculate the area of 'Circle', 'Square', 'Rectangle' and 'Triangle' .")

number = input('\n\tEnter the number of operation that you want: ')
if number == "1":
    Calculation_Operator() == True
elif number == "2":
    Trigonometric_fucntions() == True
elif number == "3":
    ConstantValues() == True
elif number == "4":
    Area() == True
else:
    print('Error: Please enter a number between 1-4!')