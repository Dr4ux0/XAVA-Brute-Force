# SALAX - Ferramenta Avançada de Força Bruta para Instagram (Edição 2025)

**Salax** é uma ferramenta moderna e altamente personalizável para testes de força bruta no login web do Instagram, desenvolvida com foco em **segurança ofensiva, evasão e desempenho assíncrono**.

Criada para fins **educacionais**, **testes de intrusão autorizados** e **pesquisas sobre autenticação web**, Salax entrega desempenho, modularidade e precisão.

---

## ⚠️ AVISO LEGAL

Este software é fornecido **exclusivamente para uso ético e educacional**. O uso indevido da ferramenta para fins ilegais ou sem permissão é **estritamente proibido**. O autor **não se responsabiliza por qualquer uso indevido**.

---

## Funcionalidades

* [x] Suporte ao login AJAX do Instagram 2025
* [x] Geração automática de `enc_password` com timestamp válido
* [x] Coleta dinâmica de:

  * `csrf_token`
  * `device_id`
  * `mid`
* [x] Suporte a cookies e cabeçalhos legítimos
* [x] Detecção de sucesso via `checkpoint_url` ou `userId`
* [x] Requisições assinadas com `aiohttp` e `ClientSession`
* [x] Atrasos programados para reduzir bloqueios
* [x] Funciona **sem proxies** (modo stealth)

---

## Pré-requisitos

* Python 3.8+
* Termux, Linux, WSL ou qualquer ambiente com suporte a SSL e operações assíncronas
* Instalação de dependências:

> ⚠️ **Importante:** A instalação de dependências com `pip` **não deve ser feita diretamente no sistema**. Use um ambiente virtual para evitar conflitos e manter seu sistema seguro.

### Criar e ativar um ambiente virtual (exemplo):

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```
## Dependecias

```bash
pip install aiohttp requests aiohttp_socks urllib3 itertools
```

---

## Uso

```bash
python salax.py
```

### Entradas

* `Nome de usuário:` Nome do usuário alvo do Instagram
* `Arquivo de senhas:` Caminho para o arquivo de senhas (`pass.txt`)

### Exemplo

```bash
Nome de usuário: luizinho33k
Arquivo de senhas: pass.txt
```

### Saída esperada

```bash
[+] Sucesso -> luizinho33k:senha123
```

Em caso de sucesso, a combinação é salva no arquivo `good.txt`.

---

## Arquitetura

* **Total sincronização com headers e cookies esperados pelo Instagram Web**
* **Login através do endpoint oficial `ajax/login`**
* **Ignora verificação SSL com `verify=False`**
* **Assíncrono para maior desempenho, mesmo com atrasos anti-bloqueio**

---

## Estrutura do Código

* `Logo()` – Exibe o banner da ferramenta
* `GetCSRF_Token()` – Captura o CSRF token e `device_id`
* `Get_MID()` – Obtém o cookie `mid` via `shared_data`
* `generate_enc_password()` – Geração legítima do campo de senha criptografada
* `attempt_login()` – Envia o POST com todos os dados
* `main()` – Gerencia as execuções, tentativas e atrasos

---

## Contribuição

Quer colaborar? Faça um fork. Teste, ajuste e envie melhorias.

---

## Autor

**FaLaH**
Email: `flaaah777@gmail.com`
Instagram: `@root.falah`
Pesquisador em desenvolvimento subterrâneo e segurança ofensiva

### Editado por

**Dr4ux0**
Email: `dr4ux0@proton.me`

---

## Licença

MIT License – Use como quiser, **com ética e responsabilidade**.
