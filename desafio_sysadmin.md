# 🐧 Desafio SysAdmin Junior: Operação "Clean & Deploy"

**Alvo:** Servidor `servidor-ubuntu-prod-01` (Simulado)

**Contexto:** Você foi contratado para arrumar a casa. O servidor está uma bagunça, deixada por um estagiário e um desenvolvedor desorganizado.

**Missão:** Navegar, limpar, organizar, configurar permissões e gerar relatórios.

---

## 🚀 Instruções Iniciais

1. Certifique-se de ter rodado o script `diretorios.py`
2. Abra seu terminal
3. Entre na pasta da simulação:

```bash
cd simulacao_servidor
```

**⚠️ REGRA DE OURO:** Não saia desta pasta raiz durante o exercício.

**Marque com um `x` dentro dos colchetes `[ ]` conforme concluir as tarefas.**

---

## 🟢 FASE 1: Reconhecimento e Navegação (Tarefas 01-15)

*Entenda o terreno antes de agir.*

- [ ] **01.** Liste o conteúdo da pasta atual para visualizar a raiz do sistema
- [ ] **02.** Identifique quais pastas simulam a estrutura padrão do Linux (`etc`, `var`, `home`)
- [ ] **03.** Entre no diretório `home`
- [ ] **04.** Liste o conteúdo para ver quais usuários existem no sistema
- [ ] **05.** Entre no diretório do usuário `estagiario`
- [ ] **06.** Liste todos os arquivos, incluindo os ocultos (use a flag correta no `ls`)
- [ ] **07.** Verifique o tamanho dos arquivos de forma legível para humanos (flag `-h`)
- [ ] **08.** Volte um nível para o diretório `home`
- [ ] **09.** Entre no diretório `sysadmin`
- [ ] **10.** Entre na subpasta `scripts`
- [ ] **11.** Liste o conteúdo e tente deduzir para que serve cada script apenas pelo nome
- [ ] **12.** Volte diretamente para a raiz da simulação (`simulacao_servidor`) sem usar `cd ..` repetidamente
- [ ] **13.** Navegue até a pasta de logs do sistema: `var/log`
- [ ] **14.** Verifique se o arquivo `syslog` existe nesta pasta
- [ ] **15.** Navegue até a pasta de sites: `var/www`

---

## 🟡 FASE 2: Análise de Conteúdo e Riscos (Tarefas 16-30)

*Leia os arquivos. Informação é poder.*

- [ ] **16.** Liste os projetos web existentes em `var/www`
- [ ] **17.** Entre na pasta `api_rest_flask`
- [ ] **18.** Leia o conteúdo do arquivo `.env.example` (comando `cat`)
- [ ] **19.** Volte para a raiz e vá até a pasta do usuário `sysadmin`
- [ ] **20.** Leia o arquivo `LEIA-ME.txt`
- [ ] **21.** Leia o arquivo `inventario_rede.csv`. Observe os IPs listados
- [ ] **22.** **AUDITORIA:** Leia o arquivo `senhas_temporarias.txt`
- [ ] **23.** Reflita: Por que deixar senhas neste arquivo é uma falha grave de segurança?
- [ ] **24.** Vá até `home/estagiario` e leia o arquivo `duvidas_para_senior.txt`
- [ ] **25.** Vá até o diretório simulado `/etc`
- [ ] **26.** Leia o arquivo `passwd`. Identifique o UID do usuário `www-data`
- [ ] **27.** Ainda em `/etc`, leia o arquivo `group`
- [ ] **28.** Identifique quem faz parte do grupo `sudo`
- [ ] **29.** Leia o arquivo `/etc/hostname` para descobrir o nome da máquina
- [ ] **30.** Leia o arquivo `/etc/hosts` e veja o IP local

---

## 🟠 FASE 3: A Grande Limpeza (Tarefas 31-55)

*O usuário `estagiario` deixou lixo pessoal no servidor. Limpe.*

- [ ] **31.** Vá para `home/estagiario`
- [ ] **32.** Entre na pasta `Downloads`
- [ ] **33.** O arquivo `vscode_installer.deb` não deve estar no servidor. Remova-o (`rm`)
- [ ] **34.** Remova o arquivo `meme_engracado.jpg`. Servidor é para trabalho
- [ ] **35.** Volte para a raiz do `estagiario`
- [ ] **36.** Entre na pasta `faculdade/tcc`
- [ ] **37.** Liste os arquivos. Há muitas versões do mesmo documento
- [ ] **38.** Renomeie `tcc_final_DEFINITIVO.docx` para `BACKUP_TCC.docx` (`mv`)
- [ ] **39.** Mova o arquivo `BACKUP_TCC.docx` para a pasta raiz do usuário `estagiario` (`mv`)
- [ ] **40.** Agora que salvou o backup, apague o arquivo `tcc_final_v1.docx`
- [ ] **41.** Apague o arquivo `tcc_final_v2_agora_vai.docx`
- [ ] **42.** Volte um nível
- [ ] **43.** Remova o diretório `faculdade` e todo seu conteúdo restante (`rm -r`)
- [ ] **44.** Vá para a pasta `testes_python`
- [ ] **45.** O arquivo `teste_loop_infinito.py` consome CPU. Apague-o imediatamente
- [ ] **46.** Crie um diretório chamado `scripts_uteis` na home do `estagiario` (`mkdir`)
- [ ] **47.** Mova o arquivo `hello.py` para dentro de `scripts_uteis`
- [ ] **48.** Remova o diretório `testes_python` (agora vazio)
- [ ] **49.** Crie uma pasta temporária chamada `LIXEIRA`
- [ ] **50.** Mova o arquivo `apostila_linux_basico.pdf` (que estava em `Downloads`) para a `LIXEIRA`
- [ ] **51.** Liste o conteúdo da `LIXEIRA` para confirmar
- [ ] **52.** Decidimos que não precisamos de lixeira. Remova a pasta `LIXEIRA` e tudo dentro dela
- [ ] **53.** Remova a pasta `Downloads` vazia, se tiver sobrado
- [ ] **54.** Volte para a raiz do `estagiario`
- [ ] **55.** Crie um arquivo vazio chamado `.limpo` para sinalizar que terminou (`touch`)

---

## 🔵 FASE 4: Preparação para Deploy (Tarefas 56-75)

*Configurando a aplicação Flask em `var/www`.*

- [ ] **56.** Navegue até `var/www/api_rest_flask`
- [ ] **57.** Crie um diretório para logs da aplicação chamado `logs`
- [ ] **58.** Entre no diretório `logs`
- [ ] **59.** Crie dois arquivos vazios: `app.log` e `error.log`
- [ ] **60.** Volte para a pasta da aplicação (`..`)
- [ ] **61.** Renomeie o arquivo de configuração `.env.example` para `.env` (Produção)
- [ ] **62.** Volte para `var/www`
- [ ] **63.** Vamos fazer um backup de segurança. Crie a pasta `backups`
- [ ] **64.** Copie a pasta `api_rest_flask` inteira para dentro de `backups` (`cp -r`)
- [ ] **65.** Entre novamente na aplicação original `api_rest_flask`
- [ ] **66.** O diretório `docker` foi depreciado. Remova-o completamente
- [ ] **67.** Crie uma estrutura de pastas `media/uploads/2023` (use `mkdir -p`)
- [ ] **68.** Crie um arquivo de texto `config_test.txt` com o conteúdo `teste 123` (use `echo` e redirecionamento `>`)
- [ ] **69.** Visualize o conteúdo de `config_test.txt` para confirmar
- [ ] **70.** Adicione uma nova linha `teste 456` ao final desse mesmo arquivo (use `>>`)
- [ ] **71.** Verifique se as duas linhas estão lá
- [ ] **72.** Na verdade, esse arquivo era inútil. Renomeie-o para `LEIAME.md`
- [ ] **73.** Edite a data de modificação do diretório `migrations` para o momento atual (`touch`)
- [ ] **74.** Liste a estrutura de arquivos da pasta atual
- [ ] **75.** Volte para a raiz da simulação

---

## 🔴 FASE 5: Administração e Permissões (Tarefas 76-90)

*Protegendo os dados.*

**Nota:** Se você não tiver `sudo` na sua máquina real, execute os comandos para praticar a sintaxe, mesmo que dê erro de permissão, ou use nos arquivos que você criou.

- [ ] **76.** Vá para `home/sysadmin`
- [ ] **77.** **CRÍTICO:** Remova o arquivo `senhas_temporarias.txt` que contém senhas expostas
- [ ] **78.** Vá para `var/www/api_rest_flask`
- [ ] **79.** O arquivo `.env` contém segredos. Remova a permissão de leitura para "outros" (`chmod o-r .env`)
- [ ] **80.** O arquivo `wsgi.py` é o executável principal. Garanta que o dono tenha leitura/escrita e o grupo apenas leitura (`chmod 640 wsgi.py`)
- [ ] **81.** Torne o diretório `logs` acessível para escrita por todos (apenas para teste, use `chmod 777 logs`)
- [ ] **82.** Verifique as permissões listando com `ls -l`
- [ ] **83.** Volte para `home/sysadmin/scripts`
- [ ] **84.** O script `backup_diario.sh` precisa ser executável. Adicione permissão de execução (`chmod +x`)
- [ ] **85.** Faça o mesmo para `check_disk.sh`
- [ ] **86.** Tente executar o script `./check_disk.sh`
- [ ] **87.** Vá para `home/dev_senior/.ssh`
- [ ] **88.** A chave privada `id_rsa` está muito exposta. Mude a permissão para 600 (apenas o dono lê/escreve)
- [ ] **89.** Verifique se a permissão mudou corretamente
- [ ] **90.** Simule a criação de um usuário: `echo "novo_dev:x:1005:1005::/home/novo_dev:/bin/bash" >> ../../../etc/passwd` (Simulando um `useradd` manual)

---

## 🟣 FASE 6: Relatórios e Evidências (Tarefas 91-100)

*Prove que você trabalhou. Gere arquivos de texto com as saídas dos comandos.*

- [ ] **91.** Volte para a raiz `simulacao_servidor`
- [ ] **92.** Crie um diretório chamado `RELATORIO_FINAL`
- [ ] **93.** Liste recursivamente toda a pasta `home/estagiario` e salve em `RELATORIO_FINAL/limpeza_estagiario.txt` (`ls -R > ...`)
- [ ] **94.** Use o comando `find` para listar todos os arquivos `.py` no servidor e salve em `RELATORIO_FINAL/todos_scripts_python.txt`
- [ ] **95.** Use o comando `grep` para buscar a palavra `password` ou `secret` dentro de `var/www` e salve o resultado em `RELATORIO_FINAL/auditoria_segredos.txt` (Dica: `grep -r`)
- [ ] **96.** Liste as permissões detalhadas da pasta do Flask e salve em `RELATORIO_FINAL/permissoes_app.txt`
- [ ] **97.** Mostre as últimas 10 linhas do arquivo `var/log/syslog` e salve em `RELATORIO_FINAL/ultimos_logs.txt` (`tail`)
- [ ] **98.** Crie um arquivo `RELATORIO_FINAL/autor.txt` e escreva seu nome dentro dele
- [ ] **99.** Execute o comando `history` (se disponível no seu shell) e tente salvar em `RELATORIO_FINAL/meus_comandos.txt`
- [ ] **100.** **FINALIZAÇÃO:** Parabéns! Você completou a simulação. Envie seu relatório final para o professor

---

## Dicas Importantes

| Comando | Uso | Exemplo |
|---------|-----|---------|
| `cd` | Navegar entre diretórios | `cd var/www` |
| `ls` | Listar arquivos | `ls -la` |
| `pwd` | Ver caminho atual | `pwd` |
| `mkdir` | Criar diretório | `mkdir logs` |
| `rm` | Remover arquivo | `rm arquivo.txt` |
| `rm -r` | Remover diretório | `rm -r pasta/` |
| `mv` | Mover/renomear | `mv antigo.txt novo.txt` |
| `cp` | Copiar arquivo | `cp origem.txt destino.txt` |
| `chmod` | Mudar permissões | `chmod 755 script.sh` |
| `cat` | Ver conteúdo | `cat arquivo.txt` |
| `grep` | Buscar texto | `grep "palavra" arquivo.txt` |
| `find` | Procurar arquivos | `find . -name "*.py"` |
| `touch` | Criar arquivo vazio | `touch novo.txt` |
| `echo` | Escrever/redirecionar | `echo "texto" > arquivo.txt` |

---

**Boa sorte e estude bem! 🎓**
