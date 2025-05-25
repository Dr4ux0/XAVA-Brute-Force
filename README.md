# SALAX


# SALAX - BruteForce Avançado para Instagram (Edição 2025)

**Salax** é uma ferramenta moderna e altamente personalizada para testes de força bruta no login web do Instagram, desenvolvida com **foco em análise de segurança, evasão e velocidade assíncrona**.

Criado para fins **educacionais**, **pentests com autorização** e **pesquisa sobre autenticação web**, Salax entrega desempenho, modularidade e precisão.

---

## âš ï¸ AVISO LEGAL

Este software é fornecido **exclusivamente para uso ético e educacional**. O uso indevido da ferramenta para fins ilegais ou sem permissão é **estritamente proibido**. O autor **não se responsabiliza** por qualquer ação imprópria.

---

## Funcionalidades

- [x] Login Web AJAX do Instagram 2025
- [x] Geração automática de `enc_password` com timestamp válido
- [x] Coleção dinâmica de:
  - `csrf_token`
  - `id_do_dispositivo`
  - `meio`
- [x] Suporte a cookies e cabeçalhos legítimos
- [x] Detecção de sucesso via `checkpoint_url` ou `userId`
- [x] Execução de assinatura com `aiohttp` e `ClientSession`
- [x] Atrasos programados para reduzir bloqueios
- [x] Totalmente **sem dependência de proxies** (modo stealth)

---

## Pré-requisitos

- Python 3.8+
- Termux, Linux, WSL ou ambiente com suporte a SSL e assíncrono
- Instalar as dependências:

```bash
pip install aiohttp solicitações
```

---

## Uso

```bash
python salax.py
```

### Entradas

- `Username:` ​​Nome do usuário alvo do Instagram
- `Arquivo de lista de senhas:` Caminho para o arquivo de senhas (`pass.txt`)

### Exemplo

```bash
Nome de usuário: verve15k
Arquivo de lista de senhas: pass.txt
```

### Saidatenta

```bash
[+] Sucesso -> verve15k:senha123
```

Em caso de sucesso, a combinação é salva no arquivo `good.txt`.

---

## Arquitetura

- **Sincronização total com headers e cookies esperados pela web do Instagram**
- **Efetue login via endpoint oficial `ajax/login`**
- **Ignorar SSL com `verify=False`**
- **Assincrono para máximo throughput, mesmo com delays anti-bloqueio**

---

## Estrutura do Código

- `Logo()` – Apresentação visual da ferramenta
- `GetCSRF_Token()` – Captura de CSRF + device_id da página
- `Get_MID()` – Obter o cookie `mid` via `shared_data`
- `generate_enc_password()` – Geração legítima do campo de senha criptografada
- `attempt_login()` – Envia o POST com o pacote completo
- `main()` – Gerencia execuções, atrasos e atrasos

---

## Contribuição

Deseja expandir uma ferramenta? Garfo. Teste, ajuste, veja melhorias.

---

## Autor

**FaLaH**  
E-mail: `flaaah777@gmail.com`  
Instagram: `@root.falah`  
Pesquisador de desenvolvimento subterrâneo e segurança ofensiva

---

## Licença

Licença MIT – Faça que quiser, **desde que com ética e ciência**.
