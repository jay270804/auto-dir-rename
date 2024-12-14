Feature: Directory renaming script
  As a user
  I want to rename directories in a specified path
  So that they follow a desired numeric format.

  Scenario: Successfully renaming directories in a clean folder
    Given I have a directory at "D:/4.\Courses"
    And the directory contains subdirectories
    |   subdir       |
    |   Projects     |
    |   Courses      |
    |   Backup       |
    When I run the renaming script
    Then the subdirectories should be renamed
    |   result    |
    | 1. Projects |
    | 2. Courses  |
    | 3. Backup   |


  Scenario: Handling conflicts with existing names
    Given I have a directory at "D:/ConflictDir"
    And the directory contains subdirectories
    |   subdir       |
    |   1. Projects  |
    |   Courses      |
    |   Backup       |
    When I run the renaming script
    Then the subdirectories should be renamed
    |   result    |
    | 1. Courses  |
    | 2. Backup   |
    | 3. Projects |


  # Scenario: Invalid path provided
  #   Given I provide an invalid path "D:/InvalidDir"
  #   When I run the renaming script
  #   Then I should see an error message "Directory path is invalid or inaccessible."
