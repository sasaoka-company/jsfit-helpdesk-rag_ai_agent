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
    try:
        from mcp_client.mcp_tools_factory import create_mcp_tools

        print("O mcp_tools_factory モジュールのインポート成功")

        from config import MCP_SERVERS

        print("O config モジュールのインポート成功")
        print(
            "O MCP_SERVERS読み込み成功: " + str(len(MCP_SERVERS)) + "個のサーバー設定"
        )

        return True
    except Exception as e:
        print("X インポートエラー: " + str(e))
        traceback.print_exc()
        return False


async def test_mcp_tools_creation():
    """MCPツールの作成をテスト"""
    print("\n=== MCPツール作成テスト ===")
    try:
        from mcp_client.mcp_tools_factory import create_mcp_tools

        tools = await create_mcp_tools()
        print("O MCPツール作成成功: " + str(len(tools)) + "個のツール")
        for i, tool in enumerate(tools, 1):
            print(
                "  " + str(i) + ". " + tool.name + ": " + tool.description[:60] + "..."
            )
        return True
    except Exception as e:
        print("X MCPツール作成エラー: " + str(e))
        traceback.print_exc()
        return False


def test_mcp_servers_config():
    """MCP_SERVERS設定の確認"""
    print("\n=== MCP_SERVERS設定テスト ===")
    try:
        from config import MCP_SERVERS

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
        return True
    except Exception as e:
        print("X MCP_SERVERS設定エラー: " + str(e))
        traceback.print_exc()
        return False


async def run_all_tests():
    """すべてのテストを実行"""
    print("MCPクライアント テストスイート開始\n")

    results = []

    # 同期テスト
    results.append(test_imports())
    results.append(test_mcp_servers_config())

    # 非同期テスト
    results.append(await test_mcp_tools_creation())

    # 結果のサマリー
    print("=== テスト結果 ===")
    passed = sum(results)
    total = len(results)
    print("成功: " + str(passed) + "/" + str(total))

    if passed == total:
        print("O すべてのテストが成功しました")
        return True
    else:
        print("X 一部のテストが失敗しました")
        return False


if __name__ == "__main__":
    success = asyncio.run(run_all_tests())
    sys.exit(0 if success else 1)
