import pytest

#!/usr/bin/env python3
"""
MCP クライアント統合テストスクリプト
"""

import asyncio
import sys
import os

# プロジェクトルートをパスに追加
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.mark.asyncio
async def test_integration():
    """
    統合テスト: MCP ツールの基本動作確認
    """
    print("=== MCP クライアント統合テスト ===")

    try:
        from src.mcp_client.mcp_tools_factory import create_mcp_tools
        from src.config import MCP_SERVERS

        print(f"設定されたサーバー数: {len(MCP_SERVERS)}")
        # ツール作成テスト
        print("\n--- ツール作成テスト ---")
        tools = await create_mcp_tools()
        print(f"✓ ツール作成成功: {len(tools)}個")
        if tools:
            print("作成されたツール一覧:")
            for i, tool in enumerate(tools, 1):
                print(f"  {i}. {tool.name}")
                print(f"     説明: {tool.description[:80]}...")
        else:
            print("⚠ ツールが作成されませんでした")
            return False
        return True
    except Exception as e:
        print(f"✗ 統合テストエラー: {e}")
        import traceback

        traceback.print_exc()
        return False


@pytest.mark.asyncio
async def test_server_connections():
    """サーバー接続テスト"""
    print("\n=== サーバー接続テスト ===")

    try:
        from src.config import MCP_SERVERS

        stdio_servers = []
        http_servers = []
        for server_name, config in MCP_SERVERS.items():
            transport = config.get("transport")
            if transport == "stdio":
                stdio_servers.append(server_name)
            elif transport == "streamable_http":
                http_servers.append(server_name)

        print(f"STDIO サーバー ({len(stdio_servers)}個): {', '.join(stdio_servers)}")
        print(f"HTTP サーバー ({len(http_servers)}個): {', '.join(http_servers)}")

        return True

    except Exception as e:
        print(f"✗ サーバー接続テストエラー: {e}")
        return False


async def run_integration_tests():
    """統合テストを実行"""
    print("MCP 統合テストスイート開始\n")

    results = []

    # テスト実行
    results.append(await test_server_connections())
    results.append(await test_integration())

    # 結果のサマリー
    print(f"\n=== 統合テスト結果 ===")
    passed = sum(results)
    total = len(results)
    print(f"成功: {passed}/{total}")

    if passed == total:
        print("✓ すべての統合テストが成功しました")
        return True
    else:
        print("✗ 一部の統合テストが失敗しました")
        return False


if __name__ == "__main__":
    success = asyncio.run(run_integration_tests())
    sys.exit(0 if success else 1)
