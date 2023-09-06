# Update a task
from task_manager.models import Task, Category  # Import necessary models

def update_task(db, task_id, title=None, description=None, category=None, priority=None, due_date=None):
    task = db.query(Task).filter_by(id=task_id).first()
    if not task:
        return "Task not found."
    
    if title is not None:
        task.title = title
    if description is not None:
        task.description = description
    if category is not None:
        category_obj = db.query(Category).filter_by(name=category).first()
        if not category_obj:
            category_obj = Category(name=category)
            db.add(category_obj)
        task.category = category_obj
    if priority is not None:
        task.priority = priority
    if due_date is not None:
        task.due_date = due_date
    
    db.commit()
    return "Task updated successfully."

# Delete a task
from task_manager.models import Task  # Import necessary model

def delete_task(db, task_id):
    task = db.query(Task).filter_by(id=task_id).first()
    if not task:
        return "Task not found."
    
    db.delete(task)
    db.commit()
    return "Task deleted successfully."
