
def divide_numbers():

    try:
        a = int(input("Ingresa el numerador: "))  # a / b
        b = int(input("Ingresa el denominador: "))
        result = a / b
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
    except ValueError:
        print("Por favor, ingresa solo números")
    except Exception as error:
        print(type(error))
    else:
        print(result)
        return result
    finally:
        print("Gracias por usar nuestra calculadora.")


divide_numbers()
