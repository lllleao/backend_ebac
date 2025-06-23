# 🐦 Twitter Clone - Backend

Este é o backend de um clone simplificado do Twitter, desenvolvido com Django e Django REST Framework. A aplicação permite funcionalidades essenciais como criação de contas, autenticação, criação de posts e comentários, além de personalização de perfis com avatar e bio.

---

## 🚀 Funcionalidades

- Cadastro de usuários
- Login e autenticação com JWT
- Criação, listagem e exclusão de **posts**
- Criação e exclusão de **comentários**
- Perfil de usuário com:
  - Avatar personalizável
  - Edição da bio

---

## 🛠️ Tecnologias e Bibliotecas

### 🔧 **Stack principal**
- **Python 3.12**
- **Django 5.2** — Web framework principal
- **Django REST Framework 3.16.0** — Criação de APIs REST
- **Poetry 2.1.2** — Gerenciador de dependências e ambientes

### 📦 Bibliotecas utilizadas

| Biblioteca                          | Finalidade                                                                 |
|-------------------------------------|----------------------------------------------------------------------------|
| `djangorestframework-simplejwt`    | Autenticação baseada em JSON Web Tokens (JWT)                             |
| `django-cors-headers`              | Permitir requisições de outros domínios (ex: frontend separado)           |
| `pillow`                           | Manipulação de arquivos de imagem (upload de avatar)                      |
| `python-decouple`                  | Separação de variáveis de ambiente de forma segura                        |
| `pytest` + `factory-boy`           | Escrita de testes automatizados (opcional)                                |
| `gitpython`                        | (Opcional) Manipulação de repositórios Git, se necessário futuramente     |

---

## ⚙️ Instalação

```bash
# Clone o repositório
git clone https://github.com/lllleao/backend_ebac.git
cd backend_ebac

# Crie e ative o ambiente virtual
python -m venv env
env/Scripts/Activate.ps1

# Instale o Poetry se ainda não tiver
pip install poetry

# Instale as dependências
poetry install

# Execute as migrações
poetry run python manage.py migrate

# Inicie o servidor de desenvolvimento
poetry run python manage.py runserver
