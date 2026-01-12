# Plano2Coordenadas

Sistema de digitalización de lotes urbanos a partir de planos en imagen.
Permite capturar manualmente las coordenadas X,Y de cada esquina de los
lotes mediante clics del mouse y exportarlas automáticamente a Excel.

## Contexto
En muchos proyectos inmobiliarios y catastrales, los planos de
urbanizaciones se encuentran únicamente como imágenes, sin información
digital de coordenadas. Este proceso suele realizarse manualmente,
siendo lento y propenso a errores.

## Solución
Este programa permite digitalizar planos de urbanizaciones con cientos
o miles de lotes (1600+), capturando con precisión las coordenadas de
cada lote y generando un archivo Excel estructurado y reutilizable.

## Características
- Carga de planos en formato imagen
- Captura de coordenadas X,Y mediante clics del mouse
- Permite hacer acercamientos y alejamientos del lote con el scroll del mouse
- Soporte para lotes de 4 esquinas
- Exportación automática a Excel
- Flujo de trabajo simple e intuitivo
- Escalable para grandes volúmenes de lotes

## Tecnologías
- Python 3
- Pillow
- pandas
- openpyxl

## Uso
1. Instalar dependencias:
   ```bash
   pip install -r requisitos.txt
