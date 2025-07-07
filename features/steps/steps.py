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
    context.child.expect(f"1. [-] {task}")
