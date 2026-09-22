---
mode: 'agent'
model: GPT-4.1
description: 'Atualizar o app Django Octofit Tracker com suporte a MongoDB, CORS e coleções de usuários, equipes, atividades, leaderboard e treinos.'
---

# Atualizações da App Django

- Todos os arquivos do projeto Django estão no diretório `octofit-tracker/backend/octofit_tracker`.
- O objetivo é atualizar a app Django para gerenciar usuários, equipes, atividades, placar de líderes e treinos.
- Use o ambiente virtual Python existente em `octofit-tracker/backend/venv` quando necessário.

## Tarefas

1. Atualize `settings.py` para conexão MongoDB e CORS.
   - Configure o Django para usar MongoDB com Djongo.
   - Defina o banco de dados como `octofit_db`.
   - Adicione as configurações de `INSTALLED_APPS` necessárias para `octofit_tracker`, `rest_framework` e `djongo`.
   - Habilite CORS para permitir todas as origens, métodos e cabeçalhos.
   - Configure o middleware de CORS corretamente.

2. Atualize os arquivos do app Django para suportar as coleções e endpoints da API:
   - `models.py`
   - `serializers.py`
   - `urls.py`
   - `views.py`
   - `tests.py`
   - `admin.py`

3. Implemente modelos e serializers para as coleções de:
   - usuários
   - equipes
   - atividades
   - placar de líderes
   - treinos

4. Crie views e rotas REST apropriadas para todas as coleções e para a API raiz.

5. Certifique-se de que `/` aponta para a API e que `api_root` está presente em `urls.py`.

6. Atualize `admin.py` para registrar os modelos relevantes da app.

7. Atualize `tests.py` com testes básicos para verificar:
   - criação e listagem de usuários
   - criação e listagem de equipes
   - criação e listagem de atividades
   - criação e listagem de treinos
   - presença do endpoint `api_root` e da rota raiz `/`

## Regras

- Trabalhe somente dentro do diretório `octofit-tracker/backend/octofit_tracker`.
- Mantenha a estrutura Django correta e consistente.
- Use o ORM do Django para os modelos e o framework REST para os endpoints.
- Não crie nenhuma configuração extra de portas públicas além das já definidas no projeto.
- Ao concluir, confirme que a API está acessível via `/` e que a rota `api_root` está funcionando.
