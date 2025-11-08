#!/usr/bin/env python3
"""
ransomware_simulator_safe.py
Simulação segura — NÃO ENCRIPTA nem apaga arquivos originais.
Requer digitar 'SIMULATE' e só opera em ./sandbox_ransom
"""

import os, shutil, time, sys
from pathlib import Path

SANDBOX_DIR = Path('./sandbox_ransom').resolve()
BACKUP_DIR = SANDBOX_DIR / 'backups'
LOG_FILE = SANDBOX_DIR / 'simulation_log.txt'

def require_confirmation():
    confirm = input("Para executar a simulação, digite SIMULATE: ").strip()
    if confirm != "SIMULATE":
        print("Confirmação não fornecida. Abortando.")
        sys.exit(1)

def ensure_sandbox():
    if not SANDBOX_DIR.exists():
        print(f"Diretório sandbox não encontrado: {SANDBOX_DIR}. Crie-o e coloque arquivos de teste.")
        sys.exit(1)
    # Proteção extra: não permitir execução fora de ./sandbox_ransom
    if str(SANDBOX_DIR) not in str(Path.cwd()):
        print("Por segurança, rode este script no diretório do projeto que contenha ./sandbox_ransom")
        sys.exit(1)

def run_simulation():
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    this_backup = BACKUP_DIR / timestamp
    this_backup.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] Iniciando simulação\n")
        for p in SANDBOX_DIR.iterdir():
            if p.is_file() and not p.name.startswith("simulation") and p.suffix != ".py":
                # Backup
                shutil.copy2(p, this_backup / p.name)
                # Create simulated 'encrypted' file (no real encryption)
                sim_file = SANDBOX_DIR / (p.name + ".SIMULATED_ENCRYPTED")
                with open(sim_file, "w", encoding="utf-8") as sf:
                    sf.write("SIMULAÇÃO — ESTE ARQUIVO FOI MARCADO COMO 'ENCRIPTADO' PARA FINS EDUCATIVOS.\n")
                    sf.write(f"Arquivo original: {p.name}\nTimestamp: {timestamp}\n")
                log.write(f"[{timestamp}] Arquivo simulado: {p.name} -> {sim_file.name}\n")
        # Criar nota de resgate fictícia
        with open(SANDBOX_DIR / "nota_de_resgate_SIMULADA.txt", "w", encoding="utf-8") as note:
            note.write("NOTA DE RESGATE (SIMULADA): este é um exemplo educacional. NÃO faça pagamentos reais.\n")
        log.write(f"[{timestamp}] Simulação concluída.\n")
    print("Simulação concluída. Verifique sandbox_ransom/ e simulation_log.txt")

if __name__ == "__main__":
    ensure_sandbox()
    require_confirmation()
    run_simulation()
