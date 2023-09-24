# Pear Admin FastAPI

#### 介绍

本项目是使用 `fastapi_template` 生成的.

本项目将使用 `fastapi` 和 pear admin next(基于layui-vue) 开发一个完善的管理系统

## `Poetry` 包管理器

本项目使用 `poetry`. 这是一种现代依赖关系管理工具.

要运行项目, 请使用以下命令:

```bash
poetry install
poetry run python -m pear_admin_fastapi
```

这将在配置的主机上启动服务器.

您可以在 `/api/docs` 中找到 `swagger` 的文档.

您可以在这里阅读更多关于诗歌的信息：https://python-poetry.org/

## `Docker` 容器部署

您可以使用以下命令使用 `docker` 启动项目:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

如果您想在 `docker` 中使用 `autoreload` 进行开发, 请将 `-f deploy/docker-compose.dev.yml` 添加到您的 `docker` 命令中.

例:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

此命令在端口 `8000` 上公开 Web 应用程序, 挂载当前目录并启用自动重新加载.

但是每次使用以下命令修改 `poetry.lock` 或 `pyproject.toml` 时, 您都必须重新构建:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## 项目结构

```bash
$ tree "pear_admin_fastapi"
pear_admin_fastapi
├── conftest.py  # Fixtures for all tests.
├── db  # module contains db configurations
│   ├── dao  # Data Access Objects. Contains different classes to interact with database.
│   └── models  # Package contains different models for ORMs.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## 项目配置

可以使用环境变量配置此应用程序.

您可以在根目录中创建 `.env` 文件并放置所有环境变量.

所有环境变量都应以 `PEAR_ADMIN_FASTAPI_` 前缀开头.

例如, 如果您在 `pear_admin_fastapi/settings.py` 中看到一个名为 `random_parameter` 的变量, 您应该提供 `PEAR_ADMIN_FASTAPI_RANDOM_PARAMETER`变量来配置值. 可以通过修改 `env_prefix` 属性来更改此行为, 在 `pear_admin_fastapi.settings.Settings.Config` 中.

`.env` 文件的示例:

```bash
PEAR_ADMIN_FASTAPI_RELOAD="True"
PEAR_ADMIN_FASTAPI_PORT="8000"
PEAR_ADMIN_FASTAPI_ENVIRONMENT="dev"
```

您可以在此处阅读有关 `BaseSettings` 类的更多信息: https://pydantic-docs.helpmanual.io/usage/settings/

## `Pre-commit` 项目规范

要安装预提交, 只需在 shell 中运行：

```bash
pre-commit install
```

预提交对于在发布代码之前检查代码非常有用.
它是使用 `.pre-commit-config.yaml` 文件配置的.

默认情况下, 它运行:

* black (格式化您的代码);
* mypy (验证类型);
* iSort (对所有文件中的导入进行排序);
* Flake8 (发现可能的错误);

您可以在此处阅读有关预提交的更多信息: https://pre-commit.com/

## `Migrations` 数据库迁移

如果要迁移数据库, 应运行以下命令:

```bash
# To run all migrations until the migration with revision_id.
alembic upgrade "<revision_id>"

# To perform all pending migrations.
alembic upgrade "head"
```

### 还原迁移

如果要还原迁移, 则应运行:

```bash
# revert all migrations up to: revision_id.
alembic downgrade <revision_id>

# Revert everything.
alembic downgrade base
```

### 生成迁移

要生成迁移, 您应该运行:

```bash
# For automatic change detection.
alembic revision --autogenerate

# For empty file generation.
alembic revision
```
