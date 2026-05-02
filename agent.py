from memory import OmniMemory
from brain import OmniBrain
from agent_actions import OmniActions
from executor import OmniExecutor
import sys

class OmniAgent:
    def __init__(self):
        try:
            self.memory = OmniMemory()
            self.brain = OmniBrain()
            self.actions = OmniActions()
            self.executor = OmniExecutor()
            self.status()
        except Exception as e:
            print(f"Failed to initialize Agent: {e}")
            sys.exit(1)

    def status(self):
        print("\n" + "="*40)
        print(" OMNI-AGENT V1.2 | SELF-CORRECTING")
        print("="*40)

    def learn_and_test_bit(self, task_name, task_desc):
        print(f"\n[Thinking] Researching bits for: {task_name}...")
        
        # 1. Ask the Brain for the initial code
        knowledge = self.brain.research_task(task_desc)
        
        if "ERROR:" in knowledge:
            print(f"[!] {knowledge}")
            return

        # 2. Extract code and write it to disk
        self.memory.learn(task_name, knowledge)
        filename = self.actions.extract_and_create_file(task_name, knowledge)
        
        # 3. Test execution if it's a Python script
        if filename and filename.endswith(".py"):
            exec_result = self.executor.run_python_file(filename)
            
            # 4. If it fails, initiate the self-correction loop!
            if not exec_result["success"]:
                print("\n[Self-Correction] Code failed. Asking Brain to fix it...")
                fix_prompt = f"""
                The previous Python script had an error. Please fix the code.
                Error message received: {exec_result['error']}
                
                Original Task: {task_desc}
                Provide the corrected file output wrapped in ```python and ```.
                """
                
                fixed_knowledge = self.brain.research_task(fix_prompt)
                
                if "ERROR:" not in fixed_knowledge:
                    # Overwrite file with fixed code
                    self.actions.extract_and_create_file(task_name, fixed_knowledge)
                    print("[Self-Correction] Fixed script written to disk. Re-testing...")
                    
                    # Final test run
                    self.executor.run_python_file(filename)
                else:
                    print("[!] Self-Correction aborted due to brain quota or model error.")

if __name__ == "__main__":
    bot = OmniAgent()
    print("\nFormat: Task Name | Description")
    print("Type 'exit' to shut down.")
    
    while True:
        try:
            user_input = input("\nAgent Prompt > ")
            if user_input.lower() == 'exit':
                print("Powering down...")
                break
                
            if "|" in user_input:
                name, desc = user_input.split("|", 1)
                bot.learn_and_test_bit(name.strip(), desc.strip())
            else:
                print("Format Error: Please use 'Task Name | Description'")
        except KeyboardInterrupt:
            print("\nShutting down safely.")
            break