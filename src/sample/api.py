from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.sample.agent import HelpDeskAgent
from src.sample.agent import AgentState
from src.sample.agent import AgentSubGraphState
from src.sample.configs import Settings
from src.sample.prompts import HelpDeskAgentPrompts
from src.mcp_client.mcp_tools_factory import create_mcp_tools
from src.sample.models import AgentResult
from src.logger import get_logger

# ロガー設定
logger = get_logger(__name__)

app = FastAPI()


class AgentRequest(BaseModel):
    pass


# 起動コマンド：
# uvicorn src.sample.api:app --reload --port 8000
@app.post("/agent", response_model=AgentResult)
async def run_agent_api(request: AgentRequest):
    try:
        # MCPツールを取得（必須条件）
        tools = await create_mcp_tools()
        # 設定・プロンプトを用意
        settings = Settings()
        prompts = HelpDeskAgentPrompts()

        # エージェントを初期化
        agent = HelpDeskAgent(settings=settings, tools=tools, prompts=prompts)

        # テスト用クエリ
        query = create_query()

        # # create_planのテスト
        # test_create_plan(agent, query)

        # select_toolsのテスト
        test_select_tool(agent, query)

        # # エージェントワークフローを実行
        # result = agent.run_agent(request.question)
        # return result

        return create_test_agent_result(request.question)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def test_create_plan(agent: HelpDeskAgent, query: str) -> dict:
    state = AgentState(question=query)

    plan_result = agent.create_plan(state=state)

    logger.info(f'★plan_result["plan"]: {plan_result["plan"]}')

    return plan_result


def test_select_tool(agent: HelpDeskAgent, query: str) -> None:
    # プラン作成
    plan_result = test_create_plan(agent, query)

    sub_state = AgentSubGraphState(
        question=query,
        plan=plan_result["plan"],
        subtask=plan_result["plan"][0],  # 最初のサブタスクを選択
        challenge_count=0,
        is_completed=False,
    )

    tool_result = agent.select_tools(state=sub_state)

    logger.info(f"★tool_result: {tool_result}")
    logger.info(f"★tool_result['messages'][-1]: {tool_result['messages'][-1]}")

    return tool_result


def create_query() -> str:
    query = """
    お世話になっております。

    現在、XYZシステムの利用を検討しており、以下の2点についてご教示いただければと存じます。

    1. パスワードに利用可能な文字の制限について
    当該システムにてパスワードを設定する際、使用可能な文字の範囲（例：英数字、記号、文字数制限など）について詳しい情報をいただけますでしょうか。安全かつシステムでの認証エラーを防ぐため、具体的な仕様を確認したいと考えております。

    2. 最新リリースの取得方法について
    最新のアップデート情報をどのように確認・取得できるかについてもお教えいただけますと幸いです。

    お忙しいところ恐縮ですが、ご対応のほどよろしくお願い申し上げます。
    """

    return query


def create_test_agent_result(question: str) -> AgentResult:
    from src.sample.models import Plan, Subtask

    plan = Plan(subtasks=["subtask1", "subtask2"])
    subtask1 = Subtask(
        task_name="subtask1",
        tool_results=[],
        reflection_results=[],
        is_completed=False,
        subtask_answer="",
        challenge_count=0,
    )
    subtask2 = Subtask(
        task_name="subtask2",
        tool_results=[],
        reflection_results=[],
        is_completed=False,
        subtask_answer="",
        challenge_count=0,
    )

    return AgentResult(
        question=question,
        plan=plan,
        subtasks=[subtask1, subtask2],
        answer="This is a test answer.",
    )
