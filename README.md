# kali-clean 

-Liberador de espacio para **Kali Linux** que permite limpiar el sistema de manera segura y eficiente. 
-Su objetivo es optimizar el uso del disco eliminando archivos innecesarios, logs, caché y papelera. Además, ofrece la opción de detectar y borrar archivos duplicados de manera opcional.
-Desarrollado en python3.



## 🔹 Características

- Limpieza de **logs del sistema** (`/var/log` y `journalctl`).  
- Eliminación de **caché de APT** y paquetes huérfanos.  
- Vaciado de la **papelera de usuario**.  
- Opción opcional de **buscar y eliminar archivos duplicados** en `/home`.  
- Visualización de **espacio liberado** antes y después de la limpieza.  
- Interfaz **colorida y amigable** en terminal.  



## 🔹 Instalación

-1º Clona este repositorio:

git clone https://github.com/tuusuario/kali-clean.git
cd kali-clean


-2º Dale permisos de ejecución:

chmod +x kali-clean.py


-3º Ejecución:

sudo python3 kali_clean.py

![kalicleamimg](https://github.com/user-attachments/assets/bbf563b7-f50c-4f1d-bd4d-bc96abc98810)

