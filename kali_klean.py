#!/usr/bin/env python3
# ---------------------------------------------------------
# Kali-Clean - By R.G.M - 2025
# ---------------------------------------------------------
import subprocess
import os
import shutil

# 🎨 Colores
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def banner():
    print(f"""
{CYAN}{BOLD}=============================================
     Kali-Clean: Script de Limpieza para Kali Linux
                  By R.G.M - 2025
============================================={RESET}
""")

def run_command(cmd, description):
    print(f"\n{BLUE}[+] {description}...{RESET}")
    try:
        subprocess.run(cmd, shell=True, check=True)
        print(f"{GREEN}[✔] Hecho ✅{RESET}")
    except subprocess.CalledProcessError:
        print(f"{RED}[X] Error al ejecutar: {cmd}{RESET}")

def folder_size(path):
    """Calcula el tamaño de una carpeta"""
    total = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if os.path.exists(fp):
                try:
                    total += os.path.getsize(fp)
                except OSError:
                    pass
    return total

def human_readable_size(size):
    """Convierte bytes a formato legible (MB, GB, TB)"""
    for unit in ['B','KB','MB','GB','TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

def clean_logs():
    before = folder_size("/var/log")
    run_command("sudo journalctl --vacuum-size=100M", "Limpiando logs de systemd")
    run_command("sudo find /var/log -type f -exec truncate -s 0 {} \;", "Vaciando archivos de log en /var/log")
    after = folder_size("/var/log")
    freed = before - after
    print(f"{GREEN}[✔] Espacio liberado en logs: {human_readable_size(freed)}{RESET}")

def clean_cache():
    run_command("sudo apt autoremove -y", "Eliminando paquetes innecesarios")
    run_command("sudo apt autoclean -y", "Limpiando paquetes obsoletos")
    run_command("sudo apt clean -y", "Vaciando caché de APT")

def clean_trash():
    trash_path = os.path.expanduser("~/.local/share/Trash")
    if os.path.exists(trash_path):
        before = folder_size(trash_path)
        shutil.rmtree(trash_path, ignore_errors=True)
        os.makedirs(trash_path, exist_ok=True)
        after = folder_size(trash_path)
        freed = before - after
        print(f"{GREEN}[✔] Espacio liberado en papelera: {human_readable_size(freed)}{RESET}")
    else:
        print(f"{YELLOW}[✔] Papelera ya está vacía{RESET}")

def clean_duplicates():
    """Usa fdupes para buscar y borrar duplicados"""
    print(f"\n{CYAN}{BOLD}--- Escaneo de duplicados en /home ---{RESET}")
    try:
        subprocess.run("sudo apt install -y fdupes", shell=True, check=True)
        subprocess.run("fdupes -r /home", shell=True, check=True)
        print(f"\n{YELLOW}¿Quieres borrar duplicados automáticamente? (s/N){RESET}")
        choice = input("> ").strip().lower()
        if choice == "s":
            subprocess.run("fdupes -rdN /home", shell=True, check=True)
            print(f"{GREEN}[✔] Duplicados eliminados{RESET}")
        else:
            print(f"{YELLOW}[i] No se borraron duplicados (opción por defecto){RESET}")
    except subprocess.CalledProcessError:
        print(f"{RED}[X] Error ejecutando fdupes{RESET}")

def clean_all():
    total_before = shutil.disk_usage("/").used
    clean_logs()
    clean_cache()
    clean_trash()

    # 🔹 Preguntar si se quiere buscar duplicados
    print(f"\n{YELLOW}¿Quieres buscar archivos duplicados? (s/N){RESET}")
    choice = input("> ").strip().lower()
    if choice == "s":
        clean_duplicates()

    total_after = shutil.disk_usage("/").used
    freed = total_before - total_after
    print(f"\n{CYAN}{BOLD}==== RESUMEN FINAL ===={RESET}")
    print(f"{GREEN}[✔] Espacio total liberado: {human_readable_size(freed)} 🚀{RESET}")

if __name__ == "__main__":
    banner()
    clean_all()
