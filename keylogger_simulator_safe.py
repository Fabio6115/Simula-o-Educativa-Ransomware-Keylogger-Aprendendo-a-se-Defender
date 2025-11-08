#!/usr/bin/env python3
"""
keylogger_simulator_safe.py
Lê ./sandbox_keylogger/sample_input.txt e gera artefatos simulados.
NÃO captura teclas reais, NÃO envia e-mails.
"""

import os, time, sys
from pathlib import Path

SANDBOX = Path("./sandbox_keylogger").resolve()
INPUT_FILE = SANDBOX / "sample_input.txt"
LOG_FILE = SANDBOX / "keylog_simulated.txt"
OUTGOING = SANDBOX / "outgoing_simulated_mail.eml"

def require_confirmation():
    confirm = input("Para executar a simulação do keylogger, digite SIMULATE_KEY: ").strip()
    if confirm != "SIMULATE_KEY":
        print("Confirmacao não fornecida. Abortando.")
        sys.exit(1)

def ensure_input():
    if not INPUT_FILE.exists():
        print(f"Crie {INPUT_FILE} com texto que represente teclas digitadas.")
        sys.exit(1)

def run():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    # Criar log formatado
    with open(LOG_FILE, 'w', encoding='utf-8') as log:
        log.write(f"SIMULAÇÃO DE KEYLOGGER — {timestamp}\n\n")
        log.write(content)
    # Criar 'email' simulado (não enviado)
    with open(OUTGOING, 'w', encoding='utf-8') as eml:
        eml.write("From: attacker@example.com\nTo: exfil@example.com\nSubject: SIMULATED KEYLOG EXFILTRATION\n\n")
        eml.write("Este é um exemplo de corpo de e-mail contendo o keylog (simulado):\n\n")
        eml.write(content)
    print("Simulação do keylogger concluída — verifique keylog_simulated.txt e outgoing_simulated_mail.eml")

if __name__ == "__main__":
    require_confirmation()
    ensure_input()
    run()
