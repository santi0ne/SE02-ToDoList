from behave import given, when, then
from pexpect.popen_spawn import PopenSpawn
import sys

APP_PATH = f'"{sys.executable}" main.py'

@given('the To-Do list is empty')
def step_impl(context):
    context.child = PopenSpawn(APP_PATH, encoding='utf-8', timeout=5)

@when('the user selects option "{option}"')
def step_impl(context, option):
    context.child.expect("Enter your choice.*")
    context.child.sendline(option)

@when('enters the task "{task}"')
def step_impl(context, task):
    context.child.expect("Enter the task to add:")
    context.child.sendline(task)

@then('the task "{task}" should be added')
def step_impl(context, task):
    context.child.expect("Task added.")
    

# Scenario 2

@given('a task "{task}" exists')
def step_impl(context, task):
    context.child = PopenSpawn(APP_PATH, encoding='utf-8', timeout=5)
    context.child.expect("Enter your choice.*")
    context.child.sendline("1")
    context.child.expect("Enter the task to add:")
    context.child.sendline(task)
    context.child.expect("Task added.")

@then('the output should contain "1. [-] {task}"')
def step_impl(context, task):
    context.child.expect("Enter your choice.*")
    context.child.sendline("2")
    context.child.expect(f"1. \\[-\\] {task}")


# Scenario 3

@when('enters "{index}"')
def step_impl(context, index):
    context.child.sendline(index)

@then('the task "{task}" should be marked complete')
def step_impl(context, task):
    context.child.expect("Task marked as complete.")
    context.child.expect("Enter your choice.*")
    context.child.sendline("2")  # list tasks
    context.child.expect(f"1. \\[x\\] {task}")


# Scenario 4

@given('tasks "{task}" and "English homework" exist')
def step_impl(context, task):
    context.child = PopenSpawn(APP_PATH, encoding='utf-8', timeout=5)
    context.child.expect("Enter your choice.*")
    context.child.sendline("1")
    context.child.expect("Enter the task to add:")
    context.child.sendline(task)
    context.child.expect("Task added.")
    context.child.expect("Enter your choice.*")
    context.child.sendline("1")
    context.child.expect("Enter the task to add:")
    context.child.sendline("English homework")
    context.child.expect("Task added.")

@then('only task "{task}" should remain')
def step_impl(context, task):
    context.child.expect(f"Task 'English homework' deleted.")
    context.child.expect("Enter your choice.*")
    context.child.sendline("2")  # list tasks
    context.child.expect(f"1. \\[-\\] {task}")


# Scenario 5

@when('enters new description "{new_description}"')
def step_impl(context, new_description):
    context.child.sendline(new_description)

@then('the task description should change')
def step_impl(context):
    context.child.expect("Task updated.")


# Scenario 6

@given('multiple tasks exist')
def step_impl(context):
    context.child = PopenSpawn(APP_PATH, encoding='utf-8', timeout=5)
    context.child.expect("Enter your choice.*")
    context.child.sendline("1")
    context.child.expect("Enter the task to add:")
    context.child.sendline("Math homework")
    context.child.expect("Task added.")
    context.child.expect("Enter your choice.*")
    context.child.sendline("1")
    context.child.expect("Enter the task to add:")
    context.child.sendline("English homework")
    context.child.expect("Task added.")
    context.child.expect("Enter your choice.*")
    context.child.sendline("1")
    context.child.expect("Enter the task to add:")
    context.child.sendline("Cooking")
    context.child.expect("Task added.")

@when('confirms with "{decision}"')
def step_impl(context, decision):
    context.child.sendline(decision)

@then('all tasks should be cleared')
def step_impl(context):
    context.child.expect("All tasks cleared.")
    context.child.expect("Enter your choice.*")
    context.child.sendline("2") 
    context.child.expect("No tasks found.")