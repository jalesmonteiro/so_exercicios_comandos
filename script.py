import os
import shutil
import random
from datetime import datetime

# Nome da pasta raiz da simulação
ROOT_DIR = "simulacao_servidor"

def criar_arquivo(path, conteudo=""):
    """Cria um arquivo com conteúdo opcional."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(conteudo)
    except Exception as e:
        print(f"Erro ao criar {path}: {e}")

def criar_estrutura():
    # 1. Limpeza do ambiente anterior
    if os.path.exists(ROOT_DIR):
        shutil.rmtree(ROOT_DIR)
        print(f"[-] Ambiente anterior removido.")

    print(f"[+] Construindo servidor Ubuntu simulado em '{ROOT_DIR}'...")
    os.makedirs(ROOT_DIR)

    # ==========================================
    # 2. ESTRUTURA DE DIRETÓRIOS DO SISTEMA (FHS)
    # ==========================================
    dirs_sistema = [
        "bin", "boot", "dev", "etc/apt", "etc/cron.d", "etc/nginx/sites-available", 
        "etc/nginx/sites-enabled", "etc/ssh", "etc/systemd/system", "etc/network",
        "home/dev_senior", "home/estagiario", "home/sysadmin",
        "lib", "media", "mnt", "opt/backup_tools", "proc", "root", "run", "sbin", 
        "srv", "sys", "tmp", "usr/bin", "usr/lib", "usr/local/bin", "usr/share",
        "var/backups", "var/cache/apt", "var/lib/mysql", "var/log/nginx", "var/log/apache2", 
        "var/spool/cron", "var/www"
    ]

    for d in dirs_sistema:
        os.makedirs(os.path.join(ROOT_DIR, d), exist_ok=True)

    # ==========================================
    # 3. ARQUIVOS DE SISTEMA E CONFIGURAÇÃO
    # ==========================================
    
    binarios = ["bash", "ls", "cp", "mv", "rm", "cat", "grep", "mkdir", "chmod", "chown", "python3", "vi", "nano", "docker", "git", "node", "npm"]
    for b in binarios:
        criar_arquivo(f"{ROOT_DIR}/bin/{b}", "#!/bin/bash\necho 'Simulacao'")

    conteudo_passwd = """root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
sysadmin:x:1000:1000:Sys Admin,,,:/home/sysadmin:/bin/bash
dev_senior:x:1001:1001:Desenvolvedor Senior,,,:/home/dev_senior:/bin/bash
estagiario:x:1002:1002:Estagiario,,,:/home/estagiario:/bin/bash
"""
    criar_arquivo(f"{ROOT_DIR}/etc/passwd", conteudo_passwd)
    
    conteudo_group = """root:x:0:
sudo:x:27:sysadmin
www-data:x:33:
devs:x:1001:dev_senior,estagiario
docker:x:999:sysadmin,dev_senior
"""
    criar_arquivo(f"{ROOT_DIR}/etc/group", conteudo_group)

    criar_arquivo(f"{ROOT_DIR}/etc/hostname", "servidor-ubuntu-prod-01")
    criar_arquivo(f"{ROOT_DIR}/etc/hosts", "127.0.0.1 localhost\n192.168.1.10 servidor-prod")
    criar_arquivo(f"{ROOT_DIR}/etc/nginx/nginx.conf", "user www-data;\nworker_processes auto;")

    # ==========================================
    # 4. LOGS
    # ==========================================
    logs = ["Iniciado servico SSH", "Usuario root logado", "Falha de autenticacao user=estagiario", "Docker container started", "Node process crashed"]
    conteudo_syslog = ""
    for _ in range(20):
        data = datetime.now().strftime("%b %d %H:%M:%S")
        conteudo_syslog += f"{data} servidor-prod systemd[1]: {random.choice(logs)}\n"
    criar_arquivo(f"{ROOT_DIR}/var/log/syslog", conteudo_syslog)

    # ==========================================
    # 5. PROJETOS WEB
    # ==========================================
    
    # --- PHP (Yii) ---
    base_yii = f"{ROOT_DIR}/var/www/site_financeiro_yii"
    dirs_yii = ["protected/config", "protected/controllers", "protected/models", "protected/views/site", "protected/runtime", "assets", "css"]
    for d in dirs_yii:
        os.makedirs(f"{base_yii}/{d}", exist_ok=True)
    criar_arquivo(f"{base_yii}/index.php", "<?php Yii::createWebApplication($config)->run();")
    criar_arquivo(f"{base_yii}/protected/config/main.php", "<?php return array('name'=>'Finanças');")

    # --- Python (Django Avançado) ---
    base_django = f"{ROOT_DIR}/var/www/portal_noticias_django"
    dirs_django = [
        "apps/core/migrations", "apps/noticias/migrations", "apps/noticias/templates/noticias",
        "logs", "media/uploads", "portal", "static/css", "staticfiles", "venv/bin"
    ]
    for d in dirs_django:
        os.makedirs(f"{base_django}/{d}", exist_ok=True)
    criar_arquivo(f"{base_django}/manage.py", "#!/usr/bin/env python\nimport os...")
    criar_arquivo(f"{base_django}/.env", "SECRET_KEY=django-secret")

    # --- Python (Flask API Rest Microservice) ---
    base_flask = f"{ROOT_DIR}/var/www/api_rest_flask"
    dirs_flask = ["app/api/v1/endpoints", "docker", "migrations/versions"]
    for d in dirs_flask:
        os.makedirs(f"{base_flask}/{d}", exist_ok=True)
    criar_arquivo(f"{base_flask}/wsgi.py", "from app.main import app")
    criar_arquivo(f"{base_flask}/.env.example", "FLASK_ENV=development")

    # --- JS (Node.js - Chat Realtime) ---
    base_node = f"{ROOT_DIR}/var/www/chat_realtime_node"
    dirs_node = [
        "src/config", "src/controllers", "src/models", "src/routes/v1", 
        "public/js", "logs", "node_modules/express" 
    ]
    for d in dirs_node:
        os.makedirs(f"{base_node}/{d}", exist_ok=True)
    criar_arquivo(f"{base_node}/package.json", '{"name": "chat", "version": "1.0.0", "scripts": {"dev": "nodemon"}}')
    criar_arquivo(f"{base_node}/.env", "PORT=3000")

    # ==========================================
    # 6. ARQUIVOS DE USUÁRIOS (Expandido)
    # ==========================================
    
    # --- Usuário: Sysadmin (Focado em manutenção e scripts) ---
    home_sys = f"{ROOT_DIR}/home/sysadmin"
    os.makedirs(f"{home_sys}/scripts", exist_ok=True)
    os.makedirs(f"{home_sys}/logs_audit", exist_ok=True)
    os.makedirs(f"{home_sys}/.ssh", exist_ok=True)
    
    # Arquivos ocultos importantes
    criar_arquivo(f"{home_sys}/.bash_history", "sudo apt update\nsudo apt upgrade\ntail -f /var/log/syslog\nexit")
    criar_arquivo(f"{home_sys}/.ssh/authorized_keys", "ssh-rsa AAAAB3NzaC1yc2E... user@laptop-admin")
    
    # Scripts de administração
    criar_arquivo(f"{home_sys}/scripts/backup_diario.sh", "#!/bin/bash\n# Script critico de backup\ntar -czf /var/backups/web_$(date +%F).tar.gz /var/www\necho 'Backup realizado'")
    criar_arquivo(f"{home_sys}/scripts/check_disk.sh", "#!/bin/bash\ndf -h | grep sda1")
    criar_arquivo(f"{home_sys}/scripts/reset_firewall.sh", "#!/bin/bash\nuft disable\nuft enable")
    
    # Relatórios e Riscos de Segurança
    criar_arquivo(f"{home_sys}/inventario_rede.csv", "IP,Hostname,OS\n192.168.1.10,srv-prod,Ubuntu\n192.168.1.11,srv-db,CentOS")
    criar_arquivo(f"{home_sys}/LEIA-ME.txt", "ATENÇÃO: Não rodar o script de firewall sem avisar a equipe.")
    criar_arquivo(f"{home_sys}/senhas_temporarias.txt", "mysql_root: Batata123\nwifi_visitantes: BemVindo2023") # Risco de segurança para treinar grep

    # --- Usuário: Dev Senior (Focado em dev, configs pessoais e chaves) ---
    home_dev = f"{ROOT_DIR}/home/dev_senior"
    os.makedirs(f"{home_dev}/projetos/pessoais", exist_ok=True)
    os.makedirs(f"{home_dev}/.config/nvim", exist_ok=True)
    os.makedirs(f"{home_dev}/.ssh", exist_ok=True)
    
    # Configurações Pessoais
    criar_arquivo(f"{home_dev}/.gitconfig", "[user]\n  name = Dev Senior\n  email = dev@empresa.com\n[core]\n  editor = vim")
    criar_arquivo(f"{home_dev}/.vimrc", "set number\nset syntax=on\ncolorscheme gruvbox")
    
    # Chaves SSH (Simuladas)
    criar_arquivo(f"{home_dev}/.ssh/id_rsa", "-----BEGIN OPENSSH PRIVATE KEY-----\n(Simulacao de chave privada - NAO COMPARTILHE)\n...MIIEowIBAAKCAQEA...\n-----END OPENSSH PRIVATE KEY-----")
    criar_arquivo(f"{home_dev}/.ssh/id_rsa.pub", "ssh-rsa AAAAB3... dev@workstation")
    criar_arquivo(f"{home_dev}/.ssh/known_hosts", "github.com ssh-rsa AAAAB...")
    
    # Projetos e Documentos
    criar_arquivo(f"{home_dev}/projetos/pessoais/ideia_app.md", "# Ideia de App\nFazer um Uber para passeadores de cachorro.")
    criar_arquivo(f"{home_dev}/projetos/script_automacao.py", "import os\nprint('Automatizando tudo...')")
    criar_arquivo(f"{home_dev}/relatorio_performance_api.pdf", "[Binario simulado PDF]")
    criar_arquivo(f"{home_dev}/todo_sprint.md", "- [x] Corrigir bug no login\n- [ ] Refatorar API v1\n- [ ] Code review do estagiário")

    # --- Usuário: Estagiário (Focado em aprendizado, bagunça e erros comuns) ---
    home_est = f"{ROOT_DIR}/home/estagiario"
    os.makedirs(f"{home_est}/Downloads", exist_ok=True)
    os.makedirs(f"{home_est}/faculdade/tcc", exist_ok=True)
    os.makedirs(f"{home_est}/testes_python", exist_ok=True)
    os.makedirs(f"{home_est}/Desktop", exist_ok=True)
    
    # Histórico e Configs
    criar_arquivo(f"{home_est}/.bash_history", "cd /var/www\nls\npwd\npython3\nexit\nrm -rf / (comando perigoso simulado)\ngit push origin master --force")
    
    # Arquivos de Estudo/Trabalho
    criar_arquivo(f"{home_est}/testes_python/hello.py", "print('Ola mundo')")
    criar_arquivo(f"{home_est}/testes_python/teste_loop_infinito.py", "while True: pass")
    criar_arquivo(f"{home_est}/duvidas_para_senior.txt", "1. Como saio do Vim?\n2. Onde ficam os logs do Nginx?\n3. Apaguei uma pasta sem querer, tem lixeira?")
    
    # Bagunça típica (Arquivos "finais" múltiplos)
    criar_arquivo(f"{home_est}/faculdade/tcc/tcc_final_v1.docx", "[Binario simulado]")
    criar_arquivo(f"{home_est}/faculdade/tcc/tcc_final_v2_agora_vai.docx", "[Binario simulado]")
    criar_arquivo(f"{home_est}/faculdade/tcc/tcc_final_DEFINITIVO.docx", "[Binario simulado]")
    
    # Downloads
    criar_arquivo(f"{home_est}/Downloads/vscode_installer.deb", "[Binario simulado]")
    criar_arquivo(f"{home_est}/Downloads/apostila_linux_basico.pdf", "[Binario simulado]")
    criar_arquivo(f"{home_est}/Downloads/meme_engracado.jpg", "[Binario simulado imagem]")
    
    print("[+] Servidor simulado pronto!")
    print(f"[!] Entre na pasta: cd {ROOT_DIR}")

if __name__ == "__main__":
    criar_estrutura()
