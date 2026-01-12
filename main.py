# Plano2Coordenadas
# Autor: Ruben Giurfa
import cv2
import pandas as pd
import numpy as np

# Cargar imagen
imagen_original = cv2.imread("girasoles-2.jpg")  # ← Cambia si tu imagen tiene otro nombre
if imagen_original is None:
    raise ValueError("No se pudo cargar la imagen. Verifica el nombre o la ruta.")

# Variables globales
puntos = []
casas = []
zoom = 1.0
offset = [0, 0]
arrastrando = False
inicio_arrastre = (0, 0)

# Función para mostrar la imagen con zoom y desplazamiento
def mostrar_imagen():
    h, w = imagen_original.shape[:2]
    vista = cv2.resize(imagen_original, (int(w * zoom), int(h * zoom)))
    h_vista, w_vista = vista.shape[:2]

    offset[0] = min(max(offset[0], 0), max(0, w_vista - 1))
    offset[1] = min(max(offset[1], 0), max(0, h_vista - 1))

    view_width = min(1200, w_vista - offset[0])
    view_height = min(800, h_vista - offset[1])

    view = vista[offset[1]:offset[1]+view_height, offset[0]:offset[0]+view_width]
    return view

# Evento de clic
def click_event(event, x, y, flags, param):
    global puntos, imagen_original, offset, zoom, arrastrando, inicio_arrastre

    if event == cv2.EVENT_LBUTTONDOWN:
        real_x = int((offset[0] + x) / zoom)
        real_y = int((offset[1] + y) / zoom)
        puntos.append((real_x, real_y))
        print(f"🟢 Punto registrado: ({real_x}, {real_y})")

        # Radio de punto dinámico según zoom
        radio = max(2, int(4 * zoom))
        cv2.circle(imagen_original, (real_x, real_y), radio, (0, 0, 255), -1)

        if len(puntos) == 4:
            casas.append(puntos.copy())
            puntos.clear()

    elif event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            zoom_nuevo = min(5.0, zoom * 1.1)
        else:
            zoom_nuevo = max(0.2, zoom * 0.9)
        factor = zoom_nuevo / zoom
        offset[0] = int((offset[0] + x) * factor - x)
        offset[1] = int((offset[1] + y) * factor - y)
        zoom = zoom_nuevo

    elif event == cv2.EVENT_RBUTTONDOWN:
        arrastrando = True
        inicio_arrastre = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and arrastrando:
        dx = x - inicio_arrastre[0]
        dy = y - inicio_arrastre[1]
        offset[0] -= dx
        offset[1] -= dy
        inicio_arrastre = (x, y)

    elif event == cv2.EVENT_RBUTTONUP:
        arrastrando = False

# Ventana e interacción
cv2.namedWindow("Plano Interactivo", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Plano Interactivo", click_event)

print("🖱 Haz clic en las 4 esquinas por casa (en orden horario)")
print("🖱 Arrastra para desplazarte, gira la rueda del mouse para hacer zoom")
print("🔚 Presiona 'q' para terminar")

while True:
    vista = mostrar_imagen()
    cv2.imshow("Plano Interactivo", vista)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

# Guardar coordenadas en Excel
datos = []
for i, casa in enumerate(casas):
    datos.append({
        'Casa': i + 1,
        'XSI1': casa[0][0], 'YSI2': casa[0][1],
        'XSD1': casa[1][0], 'YSD2': casa[1][1],
        'XID1': casa[2][0], 'YID2': casa[2][1],
        'XII1': casa[3][0], 'YII2': casa[3][1],
    })

df = pd.DataFrame(datos)
df.to_excel("coordenadas_casas.xlsx", index=False)
print("✅ Coordenadas guardadas en 'coordenadas_casas.xlsx'")


