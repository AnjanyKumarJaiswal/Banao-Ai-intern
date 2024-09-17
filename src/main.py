from models.langgraph_integration import LangGraphWorFlow
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React app URL for Vite
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def test():
    return {"msg":"This server is working"}


@app.get("/execute")
async def execute(query:str):
    print("Query Received!!",query)
    try:
        workflow =  LangGraphWorFlow()
        results = workflow.execute_graph(query=query).invoke(query)
        if isinstance(results, list):
            response_text = "\n\n".join(results)
        else:
            response_text = results
        
        return {"response": response_text}
    
    except Exception as e:
        return {"error": str(e)}
    
if __name__ =="__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
    