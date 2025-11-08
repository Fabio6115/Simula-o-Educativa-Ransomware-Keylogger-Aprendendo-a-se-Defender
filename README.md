# Simula-o-Educativa-Ransomware-Keylogger-Aprendendo-a-se-Defender

1. Visão geral

Este repositório demonstra, de modo controlado e seguro:

Ransomware (simulado): criação de arquivos de teste e uma rotina que simula encriptação (não cifra bytes reais); gera uma "nota de resgate" fictícia.

Keylogger (simulado): processamento de um arquivo de texto sample_input.txt que representa uma sequência de "teclas" para demonstrar como um keylogger poderia armazenar e transmitir logs — sem capturar teclas reais.

Reflexão e defesa: documentação detalhada de detecção, mitigação, backup, EDR/AV, análise de artefatos e exercícios de resposta a incidentes.

2. Requisitos e ambiente de laboratório

MUITO IMPORTANTE: configure um laboratório isolado. Recomendações:

Use máquinas virtuais (VirtualBox, VMware, QEMU).

Crie snapshots antes de qualquer experimento.

Isolar a VM da rede real (usar rede NAT com firewall estrito ou interface host-only). Para testes de exfiltração simulada, use uma VM controladora separada em rede isolada.

Instalar ferramentas defensivas na VM: ferramentas de monitoramento de processo, Sysmon (Windows), auditd (Linux), Wireshark para captura de tráfego em laboratório, e um EDR/antivírus de teste (com logs ativados).

3. Simulação de Ransomware

  3.1. Verificar que diretório alvo == ./sandbox_ransom
2. Pedir confirmação textual: usuário deve digitar SIMULATE
3. Criar backup em ./sandbox_ransom/backups/timestamp/
4. Para cada arquivo de teste na pasta:
    a. Criar cópia: filename.original_copy
    b. Criar arquivo filename.SIMULATED_ENCRYPTED contendo:
       - texto: "SIMULAÇÃO: este arquivo foi 'encriptado' para fins educacionais."
       - metadados: original filename, timestamp
5. Gerar nota_de_resgate.txt na pasta com instruções fictícias (sem instruções reais de pagamento)
6. Log completo em simulation_log.txt

3.4. Exemplo seguro — script de simulação:

Este código é seguro: só opera em ./sandbox_ransom e substitui por mensagens de simulação. Copie para ransomware_simulator_safe.py.

Como usar o ransomware_simulator_safe.py:

Crie pasta ./sandbox_ransom e coloque alguns arquivos de texto pequenos .

Rode python ransomware_simulator_safe.py no diretório do projeto.

Digite SIMULATE quando solicitado.

Verifique os backups em sandbox_ransom/backups/ e os arquivos .SIMULATED_ENCRYPTED.


4. Simulação de Keylogger
 
6. 1. Verificar existência de ./sandbox_keylogger/sample_input.txt
2. Pedir confirmação textual
3. Ler conteúdo do arquivo (representa "teclas")
4. Aplicar processamento: timestamps, agrupamento por sessão fictícia
5. Gerar arquivo de log keylog_simulated.txt com formatação clara
6. Criar arquivo outgoing_simulated_mail.eml com cabeçalhos simulados e o conteúdo do log.

Como usar:

Crie ./sandbox_keylogger/sample_input.txt com conteúdo que represente digitação.

Rode python keylogger_simulator_safe.py e digite SIMULATE_KEY quando solicitado.

Verifique os arquivos gerados.

5. Exercícios práticos (aplicáveis à defesa)

Detecção baseada em EDR/AV: rode o simulador e observe os alerts do antivírus/EDR (se instalado). Compare com o log do sistema e identifique eventos correlacionados.

Análise de arquivos: usar sha256sum nos artefatos criados; aprender a diferenciar arquivos legítimos de artefatos simulados.

Monitoramento de processos: durante a execução (simulada), capture ps, top (Linux) ou Process Explorer (Windows) para ver processos ativos.

Rede: execute Wireshark na interface de laboratório enquanto gera o outgoing_simulated_mail.eml — observe que nenhum tráfego de e-mail real foi enviado.

Honeypot de arquivos: configurar uma pasta canário com arquivos que disparem alertas quando acessados (pode ser feita com scripts que logam leituras).

Resposta a incidente: executar plano de resposta: isolar VM, coletar logs, restaurar snapshot, analisar indicadores.

6. Medidas de defesa (prevenção, detecção e resposta)
Prevenção

Backups regulares e verificados (3-2-1 rule).

Application whitelisting (somente apps permitidos).

Patching e gerenciamento de vulnerabilidades.

Privilégios mínimos (contas sem direitos administrativos para tarefas diárias).

Políticas de e-mail (filtragem de anexos e sandboxes de anexos).

Detecção

EDR com heurística e comportamento (procmon, criação em massa de arquivos, renomeação em lote).

Monitoramento de integridade de arquivos (tripwire, OSQuery).

Logs de sistema/endpoint (Sysmon no Windows, auditd no Linux).

Análise de tráfego de rede para padrões de exfiltração: conexões a IPs incomuns, DNS tunneling, grandes picos de tráfego.

Resposta

Isolar hosts afetados (rede e snapshots).

Coletar evidências com preservação de cadeia de custódia.

Recuperar a partir de backups verificados.

Notificação às partes interessadas e às autoridades, conforme exigido.

Revisão pós-incidente e lições aprendidas.



