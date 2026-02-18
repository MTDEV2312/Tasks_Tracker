import json
import sys
from datetime import datetime

taskObject = {
    "id": "",
    "description": "",
    "status": "todo",
    "createdAt": "",
    "updatedAt": ""
}

ID = 0

def loadID():
    global ID
    try:
        with open("task.json","r") as file:
            tasks = json.load(file)
            if tasks:
                for task in tasks:
                    if task["id"] > ID:
                        ID = task["id"]
    except (FileNotFoundError, json.JSONDecodeError):
        print("No existing tasks found. Starting fresh.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python Task_Tracker.py [command] [args]")
        print("Commands: add, update, delete, mark-in-progress, mark-done, list")
        return
    
    command = sys.argv[1]
    loadID()
    
    if command == "add" and len(sys.argv) > 2:
        AddTask(sys.argv[2])
    elif command == "update" and len(sys.argv) > 3:
        UpdateTask(int(sys.argv[2]), sys.argv[3])
    elif command == "delete" and len(sys.argv) > 2:
        DeleteTask(int(sys.argv[2]))
    elif command == "mark-in-progress" and len(sys.argv) > 2:
        UpdateTaskStatus(int(sys.argv[2]), "in-progress")
    elif command == "mark-done" and len(sys.argv) > 2:
        UpdateTaskStatus(int(sys.argv[2]), "done")
    elif command == "list":
        ViewTasks(sys.argv[2] if len(sys.argv) > 2 else None)
    else:
        print("Invalid command or missing arguments")
            
        
def AddTask(description):
    global ID
    ID += 1
    
    try:
        with open("task.json","r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    
    new_task = {
        "id": ID,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    
    with open("task.json","w") as file:
        json.dump(tasks, file, indent=2)
    
    print(f"Task added successfully (ID: {ID})")

def ViewTasks(status_filter=None):
    try:
        with open("task.json","r") as file:
            tasks = json.load(file)
        
        if not tasks:
            print("No tasks found.")
            return
        
        filtered_tasks = tasks
        if status_filter and status_filter in ["todo", "in-progress", "done"]:
            filtered_tasks = [t for t in tasks if t["status"] == status_filter]
        
        print("\n------------------------------")
        print("Tasks:")
        for task in filtered_tasks:
            print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
        print("------------------------------\n")
    except FileNotFoundError:
        print("No tasks found.")
            

def UpdateTask(taskID, new_description):
    try:
        with open("task.json","r") as file:
            tasks = json.load(file)
        
        for task in tasks:
            if task["id"] == taskID:
                task["description"] = new_description
                task["updatedAt"] = datetime.now().isoformat()
                break
        
        with open("task.json","w") as file:
            json.dump(tasks, file, indent=2)
        
        print(f"Task {taskID} updated successfully")
    except FileNotFoundError:
        print("No tasks found.")

def DeleteTask(taskID):
    try:
        with open("task.json","r") as file:
            tasks = json.load(file)
        
        remaining_tasks = [t for t in tasks if t["id"] != taskID]
        
        with open("task.json","w") as file:
            json.dump(remaining_tasks, file, indent=2)
        
        print(f"Task {taskID} deleted successfully")
    except FileNotFoundError:
        print("No tasks found.")

def UpdateTaskStatus(taskID, new_status):
    try:
        with open("task.json","r") as file:
            tasks = json.load(file)
        
        for task in tasks:
            if task["id"] == taskID:
                task["status"] = new_status
                task["updatedAt"] = datetime.now().isoformat()
                break
        
        with open("task.json","w") as file:
            json.dump(tasks, file, indent=2)
        
        print(f"Task {taskID} marked as {new_status}")
    except FileNotFoundError:
        print("No tasks found.")



if __name__ == "__main__":
    main()