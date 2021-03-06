
def finanzasPersonales(mes):
    patrimonio_total = []
    gastos_mensuales = []
    valor_setup_pc = 32707
    sueldoMensual = 0
    sueldo_anual_total = []

    print(f"FINANZAS PERSONALES HASTA {mes}: ")
    print("*******************************************************************************************")

    print("CALCULO DE SUELDO MENSUAL")
    print("*******************************************************************************************")
    print(" ")

# SUELDO MENSUAL:

    def sueldo_mensual(mes, cantidad_dias_3_horas_y_media, cantidad_dias_4_horas, cantidad_dias_4_horas_y_media, cantidad_dias_8_horas, progresar, ife, comida, vicios, gym):

        dias_3_horas_y_media = cantidad_dias_3_horas_y_media
        paga_dias_3_horas_y_media = 1345
        paga0 = dias_3_horas_y_media*paga_dias_3_horas_y_media

        dias_4_horas = cantidad_dias_4_horas
        paga_dias_4_horas = 1540
        paga1 = dias_4_horas*paga_dias_4_horas

        dias_4_horas_y_media = cantidad_dias_4_horas_y_media
        paga_dias_4_horas_y_media = 1730
        paga2 = dias_4_horas_y_media*paga_dias_4_horas_y_media

        dias_8_horas = cantidad_dias_8_horas
        paga_dias_8_horas = 3270
        paga3 = dias_8_horas*paga_dias_8_horas

        paga_moderacion_mensual = paga0 + paga1 + paga2 + paga3

        patrimonio_total.append(paga_moderacion_mensual)

        # INGRESOS EXTRA MENSUALES

        progresar = progresar
        ife = ife
        ingresos_extra_total = progresar + ife
        patrimonio_total.append(ingresos_extra_total)

        print(
            f"SUELDO MENSUAL {mes}: {paga_moderacion_mensual + ingresos_extra_total}")
        print(" ")

        sueldoMensual = paga_moderacion_mensual + ingresos_extra_total
        sueldo_anual_total.append(sueldoMensual)

        # GASTOS EXTRA MENSUALES
        
        comidA = comida
        vicioS = vicios
        gyM = gym
        gastos_extra = comidA + vicioS + gyM
        gastos_mensuales.append(gastos_extra)
        print(
            f"GASTOS EXTRA {mes}: \ncomida = {comidA} \nvicios = {vicioS} \ngym = {gyM} \n")
        print(" ")
        print(f"el sueldo mensual de {mes} despues de descontar los gastos extra mensuales es de {paga_moderacion_mensual + ingresos_extra_total - gastos_extra}")
        print("*******************************************************************************************")

        # MESES TRABAJADOS
    
    sueldo_mensual("mayo", 1, 6, 5, 0, 12840, 9000, 5000, 3000, 3200)

    sueldo_mensual("junio", 0, 10, 0, 0, 6400, 9000, 5000, 3000, 3200)

    sueldo_mensual("julio", 0, 10, 0, 0, 6400, 0, 5000, 3000, 3200)

    sueldo_mensual("agosto", 0, 10, 0, 0, 6400, 0, 5000, 3000, 3200)

    sueldo_mensual("septiembre", ife=0, progresar=6400, cantidad_dias_3_horas_y_media=0, cantidad_dias_4_horas=10, cantidad_dias_4_horas_y_media=0, cantidad_dias_8_horas=0, comida=5000, gym=3200, vicios=3000)

    sueldo_mensual(mes="octubre", cantidad_dias_3_horas_y_media=0, cantidad_dias_4_horas=10, cantidad_dias_4_horas_y_media=0, cantidad_dias_8_horas=0, ife=0, progresar=6400, comida=5000, vicios=3000, gym=3200)

    sueldo_mensual("noviembre",0,10,0,0,6400,0,5000,vicios=3000,gym=3200)

    sueldo_mensual("diciembre",0,10,0,0,6400,0,comida=5000,vicios=3000,gym=3200)


# BALANCE GENERAL DE FINANZAS

    print(" ")
    print(" ")
    print(" ")
    print("BALANCE GENERAL DE FINANZAS:")

    print("*******************************************************************************************")
    print(f".patrimonio total hasta {mes}: {sum(sueldo_anual_total)}")
    print("*******************************************************************************************")



    print("*******************************************************************************************")
    print(
        f".gastos extra acumulados al mes de {mes}: {sum(gastos_mensuales)} pesos")
    print("*******************************************************************************************")

# PATRIMONIO TOTAL

    def calculo_patrimonio_total():
        print("*******************************************************************************************")
        print(
            f".patrimonio en {mes} despues de descontar los gastos extras : {sum(patrimonio_total) - sum(gastos_mensuales)}")
        print("*******************************************************************************************")

    calculo_patrimonio_total()

# GASTO UNICO EN SETUP

    def gasto_unico_setup_pc():
        recursos_para_setup = sum(patrimonio_total) - sum(gastos_mensuales)
        print(
            f".patrimonio en {mes} despues de comprar el setup de la pc es de {recursos_para_setup - valor_setup_pc} pesos ")
        print("*******************************************************************************************")
        print(f"TOTAL: {recursos_para_setup - valor_setup_pc}")

    gasto_unico_setup_pc()


finanzasPersonales(mes="diciembre")
# COLOCAR LOS MESES TRAABAJADOS DESDE ACA!!!
