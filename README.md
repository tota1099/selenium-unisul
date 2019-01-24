# selenium-unisul
Um robô para pegar as notas no minha UNISUL

### Softwares requiridos
* Browser Google Chrome: Versão >= 65.0.3325.0
* Virtualenv: Versão >= 16.0.0
* Pip3: Versão >= 10.0.1
* Python: Versão >= 3

### Instalação
```bash
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

### Configuração

Coloque suas credenciais no arquivo .env
* A variavel "USER_SEMESTRE" possui o formato "ANO - SEMESTRE"
* Exemplo: 2018 - 1, 2018 - 2, 2019 - 1

### Execução
```bash
$ source env/bin/activate
$ python3 unisul_pegar_notas.py
```
