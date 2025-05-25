# SALAX---THIS-IS-BRUTE-FORCE
# SALAX - Instagram Bruteforce Tester (Para fins educacionais)

**Salax** é um script avançado de brute force assíncrono desenvolvido para **fins educacionais e testes de segurança em ambientes controlados**. Ele simula tentativas de login no Instagram utilizando múltiplas senhas de forma paralela e discreta, respeitando técnicas modernas de evasão e requisições similares às reais feitas por navegadores.

> **Atenção:** Este projeto é destinado apenas ao uso **ético**, em ambientes **legitimamente autorizados**. Qualquer uso fora desses termos é de total responsabilidade do operador.

---

## Características

- [x] Geração dinâmica de `enc_password`
- [x] Requisições HTTPS realistas com headers atualizados
- [x] Extração automática de `csrf_token`, `device_id` e `mid`
- [x] Compatível com proxy (BrightData ou direto)
- [x] Assíncrono com `aiohttp` para maior desempenho
- [x] Respostas do servidor visíveis para debugging
- [x] Modo stealth com cookies e headers personalizáveis

---

## Requisitos

- Python 3.8+
- Termux, Linux ou ambiente com suporte a SSL + asyncio
- Instalar dependências:

```bash
pip install aiohttp aiohttp-socks requests
