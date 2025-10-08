# config.py
"""
プロジェクト全体の定数を管理するモジュール
"""

import json
import os

# JSONファイルから設定を読み込み
_config_path = os.path.join(os.path.dirname(__file__), "mcp_server.json")
with open(_config_path, "r", encoding="utf-8") as f:
    MCP_SERVERS = json.load(f)

# ========================================
# 後方互換性のための定数（既存コード用）
# ========================================
# 最初のHTTPサーバーの設定を取得
# _first_http_server = None
# for server_name, config in MCP_SERVERS.items():
#     if config.get("transport") == "streamable_http":
#         _first_http_server = config
#         break

# HTTP_SERVER_URL = (
#     _first_http_server["url"] if _first_http_server else "http://127.0.0.1:8001/mcp"
# )
# HTTP_TIMEOUT = 30  # デフォルト値として保持

# 最初のSTDIOサーバーの設定を取得
# _first_stdio_server = None
# for server_name, config in MCP_SERVERS.items():
#     if config.get("transport") == "stdio":
#         _first_stdio_server = config
#         break

# STDIO_PYTHON_EXECUTABLE = _first_stdio_server["command"] if _first_stdio_server else ""
# STDIO_SERVER_SCRIPT = (
#     _first_stdio_server["args"][0]
#     if _first_stdio_server and _first_stdio_server.get("args")
#     else ""
# )

# ========================================
# 使用するLLMモデル
# ========================================
LLM_MODEL = "llama3.1:8b"
# LLM_MODEL = "gpt-oss:20b"  # 20Bパラメータモデル - 処理時間が長いため注意
# LLM_MODEL = "openai:gpt-5-nano"
# LLM_MODEL = "google_genai:gemini-2.5-flash-lite"
# LLM_MODEL = "anthropic:claude-3-haiku-20240307"

# ローカルモデル（Ollama）の識別子
# Ollamaライブラリに含まれるモデルのプレフィックス
OLLAMA_MODEL_PREFIX = ("llama3.1", "gpt-oss", "mistral")  # 必要に応じて追加
