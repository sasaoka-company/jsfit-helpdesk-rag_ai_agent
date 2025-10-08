# config.py
"""
プロジェクト全体の定数を管理するモジュール
"""

import json
import os

# JSONファイルから設定を読み込み
_config_path = os.path.join(os.path.dirname(__file__), "mcp_server.json")
with open(_config_path, "r", encoding="utf-8") as f:
    _config = json.load(f)

# ========================================
# MCPサーバー設定（HTTP方式用）
# ========================================
HTTP_SERVER_URL = _config["HTTP_SERVER_URL"]  # デフォルトのHTTPサーバーURL
HTTP_TIMEOUT = _config["HTTP_TIMEOUT"]  # タイムアウト設定（秒）

# ========================================
# MCPサーバー設定（標準入出力方式用）
# ========================================
STDIO_PYTHON_EXECUTABLE = _config["STDIO_PYTHON_EXECUTABLE"]  # Python実行ファイルのパス
STDIO_SERVER_SCRIPT = _config["STDIO_SERVER_SCRIPT"]  # MCPサーバースクリプトのパス

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
