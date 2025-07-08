Feature: To-Do List Management
  Users can manage their tasks using a command-line interface.

  Scenario: Add a new task
    Given the To-Do list is empty
    When the user selects option "1"
    And enters the task "Math homework"
    Then the task "Math homework" should be added

  Scenario: List tasks
    Given a task "Math homework" exists
    When the user selects option "2"
    Then the output should contain "1. [-] Math homework"

  Scenario: Mark a task as complete
    Given a task "Math homework" exists
    When the user selects option "3"
    And enters "1"
    Then the task "Math homework" should be marked complete

  Scenario: Delete a task
    Given tasks "Math homework" and "English homework" exist
    When the user selects option "4"
    And enters "2"
    Then only task "Math homework" should remain

  Scenario: Clear all tasks
    Given multiple tasks exist
    When the user selects option "5"
    And confirms with "y"
    Then all tasks should be cleared
