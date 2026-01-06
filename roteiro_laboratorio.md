# 🐧 Roteiro de Laboratório: Administração de Servidores Linux

## Contexto

Você acaba de ser contratado como Junior SysAdmin. Sua primeira tarefa é organizar e auditar os projetos web hospedados no servidor de desenvolvimento da empresa.

---

## 📋 Instruções Iniciais

1. Execute o script Python fornecido pelo professor para gerar o ambiente
2. Todos os comandos devem ser executados dentro da pasta `simulacao_servidor`
3. Abra seu terminal e entre na pasta:

```bash
cd ~/simulacao_servidor
```

(ajuste o caminho se necessário)

---

## 🟢 Missão 1: O Site Estático (Manutenção)

### Contexto

O servidor web Nginx precisa de uma página de "Em Manutenção" para ser exibida quando os outros sites caírem. Atualmente, essa estrutura não existe.

### Tarefas

- [ ] Navegue até a pasta `/var/www`
- [ ] Crie um diretório chamado `site_manutencao`
- [ ] Entre neste diretório
- [ ] Crie um arquivo vazio chamado `index.html` e outro chamado `estilos.css`
- [ ] Por segurança, tire a permissão de escrita do arquivo `index.html` para "outros" e "grupo" (deixe apenas o dono ler e escrever - 644 ou `rw-r--r--`)

### 📝 Prova de Execução

Para provar que realizou a tarefa, execute o comando abaixo dentro da pasta `var/www` e salve o resultado:

```bash
ls -lR site_manutencao > ../../../prova_missao_1.txt
```

---

## 🔵 Missão 2: Legado PHP (Yii Framework)

### Contexto

O sistema financeiro feito em PHP Yii é antigo. O arquivo de configuração contém senhas e não pode ser perdido, mas precisamos renomeá-lo para uma nova versão e manter um backup do antigo.

### Tarefas

- [ ] Localize a pasta do projeto `site_financeiro_yii` (dica: use o comando `find` ou navegue até `var/www`)
- [ ] Entre na subpasta `protected/config`
- [ ] Crie uma cópia de segurança do arquivo `main.php` com o nome `main.php.bak`
- [ ] Renomeie o arquivo original `main.php` para `main_v2.php`
- [ ] Liste o conteúdo da pasta para garantir que o backup e o novo arquivo existem

### 📝 Prova de Execução

Estando dentro de `protected/config`, execute:

```bash
ls -la > ../../../../../prova_missao_2.txt
```

---

## ⚪ Missão 3: API Flask (Python Microservice)

### Contexto

A API em Flask tem uma pasta de migrações de banco de dados (`migrations/versions`) que está vazia e não está sendo usada. O líder técnico pediu para remover essa pasta específica para limpar o projeto e criar um arquivo de log para monitoramento.

### Tarefas

- [ ] Vá até o diretório `var/www/api_rest_flask`
- [ ] Remova o diretório `migrations` e todo o seu conteúdo
- [ ] Crie uma pasta chamada `logs_app`
- [ ] Mova o arquivo `.env.example` para dentro da pasta `docker` (simulando uma reestruturação)

### 📝 Prova de Execução

Na raiz do projeto Flask (`var/www/api_rest_flask`), execute:

```bash
tree > ../../../prova_missao_3.txt
```

*Caso não tenha o `tree` instalado, use:*

```bash
ls -R > ../../../prova_missao_3.txt
```

---

## 🟣 Missão 4: Portal Django (Notícias)

### Contexto

O portal de notícias está acumulando muitos arquivos estáticos misturados. Além disso, precisamos verificar se o usuário `www-data` existe no sistema para rodar esse projeto corretamente.

### Tarefas

- [ ] Navegue até `var/www/portal_noticias_django`
- [ ] Crie um arquivo chamado `admin_user.txt`
- [ ] Use o comando `cat` no arquivo `/etc/passwd` (caminho relativo a partir de onde você está: `../../../etc/passwd`) e use o `grep` para filtrar a linha do usuário `www-data`
- [ ] **Desafio de Redirecionamento:** Salve o resultado desse filtro dentro do arquivo `admin_user.txt` que você criou no passo 2 (Dica: use `>`)
- [ ] Copie a pasta `static` inteira para dentro de `media`, simulando uma fusão de assets

### 📝 Prova de Execução

Dentro da pasta do projeto Django, execute:

```bash
cat admin_user.txt > ../../../prova_missao_4.txt && ls -F media/ >> ../../../prova_missao_4.txt
```

---

## 🟢 Missão 5: Chat Node.js (Realtime)

### Contexto

A aplicação Node.js precisa de suas variáveis de ambiente configuradas para rodar. Além disso, a pasta `node_modules` foi corrompida (simulação) e precisa ser deletada para uma reinstalação limpa.

### Tarefas

- [ ] Entre na pasta `var/www/chat_realtime_node`
- [ ] O arquivo `.env` já existe. Use o comando `cat` para ler seu conteúdo na tela
- [ ] Adicione uma nova linha ao final desse arquivo `.env` com o texto `DB_HOST=localhost` (Você pode usar um editor de texto como `nano` ou `vi`, ou usar o comando `echo "DB_HOST=localhost" >> .env`)
- [ ] Remova completamente a pasta `node_modules` e tudo que tem dentro dela (⚠️ cuidado com este comando!)
- [ ] Mude as permissões do arquivo `package.json` para que todos possam ler, escrever e executar (777) - **Atenção:** Isso é uma prática ruim de segurança, mas vamos fazer para testar o comando `chmod`

### 📝 Prova de Execução

Dentro da pasta do projeto Node, execute:

```bash
cat .env > ../../../prova_missao_5.txt && ls -l package.json >> ../../../prova_missao_5.txt
```

---

## 🏁 Finalização

Ao terminar:

- [ ] Volte para a raiz `simulacao_servidor`. Você deve ter 5 arquivos de prova (`prova_missao_1.txt` até `prova_missao_5.txt`)
- [ ] Compacte esses arquivos para enviar ao professor (opcional, se souber usar o `tar` ou `zip`)

---

## 📚 Resumo de Comandos Utilizados

| Missão | Comandos Principais | Objetivo |
|--------|-------------------|----------|
| 1 | `mkdir`, `touch`, `chmod` | Criar estrutura com permissões corretas |
| 2 | `cp`, `mv` | Backup e renomeação de configurações |
| 3 | `rm -r`, `mkdir`, `mv` | Limpeza e reorganização de arquivos |
| 4 | `cat`, `grep`, `>`, `cp -r` | Auditoria de usuários e fusão de assets |
| 5 | `cat`, `echo >>`, `rm -r`, `chmod` | Configuração de ambiente e permissões |

---

**Boa sorte com o laboratório! 🎓**
