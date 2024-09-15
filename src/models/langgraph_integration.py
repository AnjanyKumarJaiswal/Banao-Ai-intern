from langgraph.graph import StateGraph
from agents.plan_agent import PlanAgent
from agents.tool_agent import ToolAgent

plan_agent = PlanAgent()
tool_agent = ToolAgent()

workflow = StateGraph(dict)

class LangGraphWorFlow:
    
    def execute_graph(self,query):
        workflow.add_node("PlanAgent" , plan_agent.split_user_query)
        workflow.add_node("ToolAgent",tool_agent.final_feedback)
        
        workflow.add_edge("PlanAgent", "ToolAgent")
        
        workflow.set_entry_point("PlanAgent")
        workflow.set_finish_point("ToolAgent")
        
        app=workflow.compile()
        
        return app
        
    
        
        