from utils.canales.entropy_media import calculateRuido, calculatePerdida
from utils.canales.priori.entropy import calculateHPriori
from utils.canales.posteriori.entropy import calculateHPosterioriTotal
from utils.canales.entropia_canal import calculateHCanal
from utils.canales.informacion_mutua import informacionMutuaABSimple, informacionMutuaBASimple
from utils.matrix import printMatrixVerbose  # usar versión verbose

# Canales
C1_prior = [0.70, 0.30]
C1_matrix = [
    [0.7, 0.3],
    [0.4, 0.6]
]

C2_prior = [0.50, 0.50]
C2_matrix = [
    [0.3, 0.3, 0.4],
    [0.3, 0.3, 0.4]
]

C3_prior = [0.25, 0.50, 0.25]
C3_matrix = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.5, 0.5, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]

C4_prior = [0.25, 0.25, 0.25, 0.25]
C4_matrix = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
]

def format_matrix(matrix: list[list]) -> str:
    max_width = max(len(f"{elem:.2f}") for row in matrix for elem in row)
    lines = []
    for row in matrix:
        lines.append(" ".join(f"{elem:>{max_width}.2f}" for elem in row))
    return "\n".join(lines)

def format_prior(prior: list[float]) -> str:
    return "[" + ", ".join(f"{p:.2f}" for p in prior) + "]"

def calcular_metricas(prior, channel):
    return {
        "H(A)": calculateHPriori(prior),
        "H(B)": calculateHPosterioriTotal(prior, channel),
        "H(A|B)": calculateRuido(prior, channel),
        "H(B|A)": calculatePerdida(prior, channel),
        "H(A,B)": calculateHCanal(prior, channel),
        "I(A;B)": informacionMutuaABSimple(prior, channel),
        "I(B;A)": informacionMutuaBASimple(prior, channel)
    }

def main():
    canales = [
        ("C1", C1_prior, C1_matrix),
        ("C2", C2_prior, C2_matrix),
        ("C3", C3_prior, C3_matrix),
        ("C4", C4_prior, C4_matrix),
    ]

    filas = []
    for nombre, prior, matriz in canales:
        metricas = calcular_metricas(prior, matriz)
        filas.append({
            "Canal": nombre,
            "Prior": format_prior(prior),
            "Matriz": format_matrix(matriz),
            **{k: f"{v:.4f}" for k, v in metricas.items()}
        })

    columnas = ["Canal", "Prior", "Matriz", "H(A)", "H(B)", "H(A|B)", "H(B|A)", "H(A,B)", "I(A;B)", "I(B;A)"]

    anchos = {}
    for col in columnas:
        max_len = max(len(fila[col].split("\n")[0]) for fila in filas)
        anchos[col] = max(max_len, len(col))

    header = " | ".join(f"{col:>{anchos[col]}}" for col in columnas)
    sep = "-+-".join("-" * anchos[col] for col in columnas)
    print(header)
    print(sep)

    for fila in filas:
        matriz_lines = fila["Matriz"].split("\n")
        prior_line = fila["Prior"]
        print(" | ".join([
            f"{fila['Canal']:>{anchos['Canal']}}",
            f"{prior_line:>{anchos['Prior']}}",
            f"{matriz_lines[0]:>{anchos['Matriz']}}",
            f"{fila['H(A)']:>{anchos['H(A)']}}",
            f"{fila['H(B)']:>{anchos['H(B)']}}",
            f"{fila['H(A|B)']:>{anchos['H(A|B)']}}",
            f"{fila['H(B|A)']:>{anchos['H(B|A)']}}",
            f"{fila['H(A,B)']:>{anchos['H(A,B)']}}",
            f"{fila['I(A;B)']:>{anchos['I(A;B)']}}",
            f"{fila['I(B;A)']:>{anchos['I(B;A)']}}",
        ]))
        for extra in matriz_lines[1:]:
            print(" | ".join([
                " " * anchos["Canal"],
                " " * anchos["Prior"],
                f"{extra:>{anchos['Matriz']}}",
                " " * anchos["H(A)"],
                " " * anchos["H(B)"],
                " " * anchos["H(A|B)"],
                " " * anchos["H(B|A)"],
                " " * anchos["H(A,B)"],
                " " * anchos["I(A;B)"],
                " " * anchos["I(B;A)"],
            ]))

    print("\nMatriz solo de métricas (filas=metricas, columnas=canales):")
    metric_order = ["H(A)", "H(B)", "H(A|B)", "H(B|A)", "H(A,B)", "I(A;B)", "I(B;A)"]
    matriz_metricas = []
    for m in metric_order:
        matriz_metricas.append([float(fila[m]) for fila in filas])
    row_labels = metric_order
    col_labels = [nombre for nombre, _, _ in canales]
    printMatrixVerbose(matriz_metricas, row_labels, col_labels)

if __name__ == "__main__":
    main()