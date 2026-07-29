from agent.state import AgentState


class Planner:

    def next_tool(self, state: AgentState):

        order = [
            "contract",
            "monitoring",
            "incident",
            "email",
            "finance"
        ]

        for tool in order:
            if tool not in state.completed_tools:
                return tool

        return None