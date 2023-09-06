import click
from task_manager.database import create_database, get_db
from task_manager.models import User, Category, Task
from task_manager.tasks import quicksort

@click.group()
def cli():
    pass

@click.command()
@click.option('--username', prompt='Enter username', help='User username')
def add_user(username):
    db = next(get_db())
    user = User(username=username)
    db.add(user)
    db.commit()
    print(f"User {username} added.")

@click.command()
@click.option('--title', prompt='Enter title', help='Task title')
@click.option('--description', prompt='Enter description', help='Task description')
@click.option('--username', prompt='Enter username', help='User username')
@click.option('--category', prompt='Enter category', help='Task category')
def add_task(title, description, username, category):
    db = next(get_db())
    user = db.query(User).filter_by(username=username).first()
    if not user:
        print(f"User {username} does not exist. Please add the user first.")
        return

    category_obj = db.query(Category).filter_by(name=category).first()
    if not category_obj:
        category_obj = Category(name=category)
        db.add(category_obj)

    task = Task(title=title, description=description, user=user, category=category_obj)
    db.add(task)
    db.commit()
    print(f"Task '{title}' added for user {username} in category {category}.")

@click.command()
@click.option('--username', prompt='Enter username', help='User username')
def list_tasks(username):
    db = next(get_db())
    user = db.query(User).filter_by(username=username).first()
    if not user:
        print(f"User {username} does not exist.")
        return

    tasks = user.tasks
    if not tasks:
        print(f"No tasks found for user {username}.")
    else:
        print(f"Tasks for user {username}:")
        sorted_tasks = quicksort(tasks)
        for task in sorted_tasks:
            print(f"- {task.title} ({task.category.name})")

cli.add_command(add_user)
cli.add_command(add_task)
cli.add_command(list_tasks)

if __name__ == '__main__':
    create_database()
    cli()
