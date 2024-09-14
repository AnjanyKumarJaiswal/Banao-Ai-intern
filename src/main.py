from models.langgraph_integration import LangGraphWorFlow
from fastapi import FastAPI, Query


app = FastAPI()

workflow = LangGraphWorFlow()

@app.get("/execute")
def main(query: str):
    app = workflow.execute_graph(query=query)
    result = app.invoke(query)
    for res in result:
        return {"results": res}
    
if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    