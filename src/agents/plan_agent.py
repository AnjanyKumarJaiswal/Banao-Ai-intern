from models.llm_model import generate_response
import re
import random

class PlanAgent:
    def split_user_query(self,query):
        prompt = f"Split the following task into 4 subtasks: {query}."
        subtasks_response = generate_response(prompt)
        subtasks_string = subtasks_response[0] if isinstance(subtasks_response, list) else subtasks_response
        subtasks = re.split(r'\*\*Subtask \d+:\*\*', subtasks_string)
        subtasks = [subtask.strip() for subtask in subtasks if subtask.strip()]
    
        return subtasks
    
    def modify_subtask(self, subtasks):
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