**AI Agent 機能を提供する API サーバー**

このプロジェクトは、MCP サーバーと通信する AI エージェント機能を提供する、API サーバです。
MCP サーバーは標準入出力(STDIO)、Streamable HTTP の両方式をサポートします。

# 1. 機能

- **MCP サーバとの通信**: 標準入出力(STDIO)、Streamable HTTP 両方式の MCP サーバと通信可能
- **自律的ツール選択**: AI エージェントが最適な MCP ツールを自動選択
- **API 提供**: FastAPI により、REST エンドポイントでの利用

# 2. 前提条件

- Python 3.12 以上
- [uv](https://docs.astral.sh/uv/) (Python パッケージマネージャー)
- モデル実行環境：Ollama
- LLM モデル：切替可能（現状はハードコーディング）
- 仮想環境（`.venv`）が作成されていること

# 3. 開発環境セットアップ

## 3-1. Git 設定

以下コマンドにより、チェックアウト時、コミット時に改行コードを変更しないようにします。（`.gitattributes` のままになります）

```powershell
git config --global core.autocrlf false
```

## 3-2. 依存関係のインストール

以下コマンドにより、`pyproject.toml`で定義されているライブラリをインストールします。

```powershell
uv sync
```

# 4. サーバ起動

```powershell
uvicorn agent_api:app --reload --port 8000
```

## （参考）ブラウザから Swagger UI を利用

http://127.0.0.1:8000/docs

# 5. テスト実行

```powershell
uv run pytest tests/ -v
```
