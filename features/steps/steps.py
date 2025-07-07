from behave import given, when, then
from pexpect.popen_spawn import PopenSpawn
import sys

APP_PATH = f'"{sys.executable}" main.py'  # Runs with the same Python interpreter
to_do_list = []

@given('the To-Do list is empty')
def step_impl(context):
    context.child = PopenSpawn(APP_PATH, encoding='utf-8', timeout=5)
    global to_do_list
    to_do_list = []

@when('the user selects option "{option}"')
def step_impl(context, option):
    context.child.expect("Enter your choice.*")
    context.child.sendline(option)

@when('enters the task "{task}"')
def step_impl(context, task):
    context.child.expect("Enter the task to add:")
    context.child.sendline(task)
    global to_do_list
    to_do_list.append(task)

@then('the task "{task}" should be added')
def step_impl(context, task):
    assert task in to_do_list, 'Task added'


# SCENARIO 2

@given('a task "{task}" exists')
def step_impl(context, task):
    context.child = PopenSpawn(APP_PATH, encoding='utf-8', timeout=5)
    global to_do_list
    to_do_list.append(task)
    assert task not in to_do_list, 'No tasks found.'

@when('the user selects option "{option}"')
def step_impl(context, option):
    context.child.expect("Enter your choice.*")
    context.child.sendline(option)

@then('the output should contain "1. [-] {task}"')
def step_impl(context, task):
    context.child.expect(f"1. [-] {task}")

