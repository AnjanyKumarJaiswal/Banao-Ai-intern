from models.langgraph_integration import LangGraphWorFlow
from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def test():
    return {"msg":"This server is working"}


@app.get("/execute")
async def execute(query:str):
    print("Query Received!!",query)
    workflow =  LangGraphWorFlow()
    results = workflow.execute_graph(query=query).invoke(query)
    return results
    # try:
    #     results = workflow.execute_graph(query=query).invoke(query)
    #     return results
    # except Exception as e:
    #     return {"error": str(e)}
    
if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
    