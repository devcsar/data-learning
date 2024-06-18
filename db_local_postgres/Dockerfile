# Usando la imagen base de postgres:15
FROM postgres:15

# Crea la carpeta local_files dentro de la carpeta home del contenedor
RUN mkdir -p /home/local_files

# Establece el directorio de trabajo
WORKDIR /home/local_files

# Comando por defecto para ejecutar cuando el contenedor se inicia
CMD ["bash"]
