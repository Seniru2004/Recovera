from tools import (
    contract_tool,
    monitoring_tool,
    incident_tool,
    email_tool,
    finance_tool
)


class ToolRouter:

    def run(self, tool_name):

        if tool_name == "contract":
            return contract_tool.run()

        if tool_name == "monitoring":
            return monitoring_tool.run()

        if tool_name == "incident":
            return incident_tool.run()

        if tool_name == "email":
            return email_tool.run()

        if tool_name == "finance":
            return finance_tool.run()

        raise Exception(f"Unknown tool: {tool_name}")