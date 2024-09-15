from models.llm_model import generate_response

class ToolAgent:
    def final_feedback(self,subtasks):
        print("to generate final output subtasks received :)")
        results = []
        for subtask in subtasks[1:]:
            print(f"Processing subtask: {subtask}")
            prompt = f"Process this subtask briefly: {subtask}"
            output = generate_response(prompt)
            if not output:
                print("No Response Generated from the Model")
            results.append(output.strip())
        return results