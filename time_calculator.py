def add_time(hora_inicial, duracion, dia=False):
    # Convertir la hora inicial a un formato de 24 horas
    am_pm = (hora_inicial.split(" "))[1]
    hora_inicial = hora_inicial.replace("AM", "").replace("PM", "")
    horas_inicial = int(hora_inicial.split(":")[0])
    minutos_inicial = int(hora_inicial.split(":")[1])

    # Dividir la duración en horas y minutos
    horas = int(duracion.split(":")[0])
    minutos = int(duracion.split(":")[1])

    # Sumar las horas y minutos a la hora inicial
    horas_final = horas_inicial + horas
    minutos_final = minutos_inicial + minutos

    # # Inicializar la variable `dia_final`
    # dia_final = None

    # Verificar si el número de minutos es mayor que 59
    if minutos_final > 59:
        minutos_final = minutos_final - 60
        horas_final = horas_final + 1

    # Verificar si el número de horas es mayor que 23
    contador = 0
    if horas_final > 12:
        while horas_final > 12:
            horas_final = horas_final - (12)
            contador += 1

    if horas_inicial < 12 and horas_final >= 12:  # and am_pm == "PM":
        contador += 1
    # Cambios de signo am-pm
    nday = 0  # cuenta dias nuevos
    for sign in range(contador):
        if am_pm == "AM":
            am_pm = "PM"
        else:
            am_pm = "AM"
            nday += 1

    # Imprimir el resultado final
    if dia:
        new_day = day_after(dia, nday)
        if nday == 0:
            hora_final = f"{horas_final}:{minutos_final:02} {am_pm}, {new_day}"
        if nday == 1:
            hora_final = (
                f"{horas_final}:{minutos_final:02} {am_pm}, {new_day} (next day)"
            )
        if nday > 1:
            hora_final = f"{horas_final}:{minutos_final:02} {am_pm}, {new_day} ({nday} days later)"
    else:
        if nday == 1:
            hora_final = f"{horas_final}:{minutos_final:02} {am_pm} (next day)"
        if nday > 1:
            hora_final = f"{horas_final}:{minutos_final:02} {am_pm} ({nday} days later)"
        if nday == 0:
            hora_final = f"{horas_final}:{minutos_final:02} {am_pm}"

    print(hora_final)
    return hora_final


def day_after(day, nday):
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    ind = days.index(
        day.lower().capitalize()
    )  # convierto el dia ingresado a mayuscula inicial y todo lo demas minusculas para que coincida con mi lista de dias
    new_day = (ind + nday) % 7
    new_day = days[new_day]
    return new_day
