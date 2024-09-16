from models.llm_model import generate_response
import re
import random

class PlanAgent:
    def split_user_query(self,query):
        print("query received for subtasks")
        prompt = f"Split the following task into 4 subtasks: {query}."
        subtasks_response = generate_response(prompt)
        print("Before Splitting the LIST",subtasks_response)
        if not subtasks_response:
            print("No Response Generated from the Model")
        
        if isinstance(subtasks_response,list):
            subtasks_list = subtasks_response
        else:
            subtasks_list = subtasks_response.splitlines()
        
        subtasks = [subtask.strip() for subtask in subtasks_list if subtask.strip()]
        print("After Splitting the LIST",subtasks)
        
        
        return subtasks
    
    def modify_subtask(self, subtasks):
        if len(subtasks) == 0:
            return print("SubTask is zero")
        index = random.randint(0, len(subtasks) - 1)
        subtasks[index] += " (modified)"
        return subtasks
    
    def delete_subtask(self, subtasks):
        if subtasks:
            subtasks.pop(random.randint(0, len(subtasks) - 1))
        return subtasks
    
    def add_subtask(self, subtasks):
        subtasks.append(f"New Subtask {len(subtasks) + 1}")
        return subtasks
