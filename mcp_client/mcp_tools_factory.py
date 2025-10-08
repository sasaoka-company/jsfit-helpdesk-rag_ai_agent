from typing import List
from langchain_core.tools import Tool
from langchain_mcp_adapters.client import MultiServerMCPClient
from config import MCP_SERVERS
from logger import get_logger

logger = get_logger(__name__)


async def create_mcp_tools() -> List[Tool]:
    logger.info(">>> MCP ツール作成開始（langchain-mcp-adapters使用）")

    # JSONから動的にserver_connectionsを構築
    server_connections = {}

    for server_name, server_config in MCP_SERVERS.items():
        transport = server_config.get("transport")

        if transport == "stdio":
            server_connections[server_name] = {
                "command": server_config["command"],
                "args": server_config["args"],
                "transport": "stdio",
            }
            logger.info(
                f">>> STDIO サーバー '{server_name}' を追加: {server_config['command']}"
            )

        elif transport == "streamable_http":
            server_connections[server_name] = {
                "url": server_config["url"],
                "transport": "streamable_http",
            }
            logger.info(
                f">>> HTTP サーバー '{server_name}' を追加: {server_config['url']}"
            )
        else:
            logger.warning(
                f">>> 未知のtransport '{transport}' をスキップ: {server_name}"
            )

    logger.info(f">>> サーバー接続設定: {server_connections}")

    try:
        # MultiServerMCPClientのインスタンスを作成（正しい引数形式）
        logger.info(">>> MultiServerMCPClient インスタンス作成中...")
        client = MultiServerMCPClient(server_connections)
        logger.info(">>> MultiServerMCPClient インスタンス作成完了")

        # ツールを取得
        logger.info(">>> ツール取得開始...")
        tools = await client.get_tools()
        logger.info(f">>> ツール取得完了: {len(tools)}個のツールを取得")

        # 取得したツールの詳細をログ出力
        for i, tool in enumerate(tools):
            logger.info(f">>> ツール{i+1}: {tool.name} - {tool.description}")

        logger.info(">>> MCP ツール作成完了（langchain-mcp-adapters使用）")
        return tools

    except Exception as e:
        logger.error(f">>> MCP ツール作成エラー（langchain-mcp-adapters使用）: {e}")
        logger.error(f">>> エラー詳細: {type(e).__name__}: {str(e)}")
        raise
