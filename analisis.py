import pandas as pd

def leercsv():
    try:
        bd = pd.read_csv("datos_rendimiento_universidad.csv")
        bd["calificacion"] = pd.to_numeric(bd["calificacion"])
        return bd
    except Exception as err:
        print("Error al leer el archivo:", err)


# =================================
# 1. Materias con mayor reprobación
# =================================
def materiasReprobacion(bd):
    try:
        bd["reprobado"] = bd["calificacion"] < 6

        materias = (
            bd.groupby("materia", as_index=False)["reprobado"]
            .mean()
            .sort_values("reprobado", ascending=False)
        )

        print("\nMATERIAS CON MAYOR ÍNDICE DE REPROBACIÓN")
        print(materias.to_string(index=False))

    except Exception as err:
        print(err)


# =================================
# 2. Carreras con mayor promedio
# =================================
def carrerasPromedio(bd):
    try:
        carreras = (
            bd.groupby("carrera", as_index=False)["calificacion"]
            .mean()
            .round(2)
            .sort_values("calificacion", ascending=False)
        )

        print("\nCARRERAS CON MAYOR PROMEDIO")
        print(carreras.to_string(index=False))

    except Exception as err:
        print(err)


# =================================
# 3. Riesgos académicos
# =================================
def riesgosAcademicos(bd):
    try:

        riesgos = bd[(bd["calificacion"] >= 6) & (bd["calificacion"] <= 7)]

        materias = (
            riesgos.groupby("materia", as_index=False)["calificacion"]
            .count()
            .rename(columns={"calificacion": "en_riesgo"})
            .sort_values("en_riesgo", ascending=False)
        )

        semestres = (
            riesgos.groupby("semestre", as_index=False)["materia"]
            .nunique()
            .rename(columns={"materia": "materias_en_riesgo"})
            .sort_values("materias_en_riesgo", ascending=False)
        )

        print("\nRIESGOS ACADÉMICOS")

        print("\nMaterias:")
        print(materias.to_string(index=False))

        print("\nSemestres:")
        print(semestres.to_string(index=False))

    except Exception as err:
        print(err)


# =================================
# 4. Tendencias por semestre
# =================================
def calcularTendencia(bd):
    try:

        tendencia = (
            bd.groupby(["año", "semestre"], as_index=False)["calificacion"]
            .mean()
            .round(1)
        )

        tendencia = tendencia.sort_values(["año", "semestre"])

        print("\nTENDENCIAS POR SEMESTRE")
        print(tendencia.to_string(index=False))

    except Exception as err:
        print(err)


# =================================
# MENÚ PRINCIPAL
# =================================
def main():

    bd = leercsv()

    while True:

        print("\n========= MENÚ DE ANÁLISIS =========")
        print("1. Materias con mayor índice de reprobación")
        print("2. Carreras con mayor promedio")
        print("3. Tendencias por semestre")
        print("4. Riesgos académicos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":
                materiasReprobacion(bd)

            case "2":
                carrerasPromedio(bd)

            case "3":
                calcularTendencia(bd)

            case "4":
                riesgosAcademicos(bd)

            case "5":
                print("Saliendo del programa...")
                break

            case _:
                print("Opción no válida")


if __name__ == "__main__":
    main()