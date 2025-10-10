# config.py
"""
プロジェクト全体の定数を管理するモジュール
"""

import json
import os

# ========================================
# プロジェクトルートディレクトリ
# ========================================
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# JSONファイルから設定を読み込み
_config_path = os.path.join(ROOT_DIR, "mcp_server.json")
with open(_config_path, "r", encoding="utf-8") as f:
    MCP_SERVERS = json.load(f)


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
OLLAMA_MODEL_PREFIX = ("llama3.1", "gpt-oss")  # 必要に応じて追加
