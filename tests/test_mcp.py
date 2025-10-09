import pytest

#!/usr/bin/env python3
"""
MCPクライアントのテストスクリプト
"""

import sys
import os
import traceback
import asyncio

# プロジェクトルートをパスに追加
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_imports():
    """インポートをテスト"""
    print("=== インポートテスト ===")
    from src.mcp_client.mcp_tools_factory import create_mcp_tools

    print("O mcp_tools_factory モジュールのインポート成功")
    from src.config import MCP_SERVERS

    print("O config モジュールのインポート成功")
    print("O MCP_SERVERS読み込み成功: " + str(len(MCP_SERVERS)) + "個のサーバー設定")
    assert True


@pytest.mark.asyncio
async def test_mcp_tools_creation():
    """MCPツールの作成をテスト"""
    print("\n=== MCPツール作成テスト ===")
    from src.mcp_client.mcp_tools_factory import create_mcp_tools

    tools = await create_mcp_tools()
    print("MCPツール作成成功: " + str(len(tools)) + "個")
    for i, tool in enumerate(tools, 1):
        print("  " + str(i) + ". " + tool.name + ": " + tool.description[:60] + "...")
    assert True


def test_mcp_servers_config():
    """MCP_SERVERS設定の確認"""
    print("\n=== MCP_SERVERS設定テスト ===")
    from src.config import MCP_SERVERS

    print("設定されたサーバー数: " + str(len(MCP_SERVERS)))
    stdio_count = 0
    http_count = 0
    for server_name, config in MCP_SERVERS.items():
        transport = config.get("transport")
        if transport == "stdio":
            stdio_count += 1
            print("  STDIO: " + server_name + " -> " + config.get("command", "N/A"))
        elif transport == "streamable_http":
            http_count += 1
            print("  HTTP:  " + server_name + " -> " + config.get("url", "N/A"))
        else:
            print("  未知:   " + server_name + " -> " + transport)
    print("O STDIO サーバー: " + str(stdio_count) + "個")
    print("O HTTP サーバー: " + str(http_count) + "個")
    assert True


async def run_all_tests():
    """すべてのテストを実行"""
    print("MCPクライアント テストスイート開始\n")

    results = []

    from src.config import MCP_SERVERS

    print("設定されたサーバー数: " + str(len(MCP_SERVERS)))
    stdio_count = 0
    http_count = 0
    for server_name, config in MCP_SERVERS.items():
        transport = config.get("transport")
        if transport == "stdio":
            stdio_count += 1
            print("  STDIO: " + server_name + " -> " + config.get("command", "N/A"))
        elif transport == "streamable_http":
            http_count += 1
            print("  HTTP:  " + server_name + " -> " + config.get("url", "N/A"))
        else:
            print("  未知:   " + server_name + " -> " + transport)
    print("O STDIO サーバー: " + str(stdio_count) + "個")
    print("O HTTP サーバー: " + str(http_count) + "個")
    assert True
    success = asyncio.run(run_all_tests())
    sys.exit(0 if success else 1)
