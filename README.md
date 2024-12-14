# auto-dir-rename
A python automation function that renames the directories to a sorted numeric format.
Following BDD method.

Sample Gherkin Feature:

<pre >
Feature: Directory renaming script  
  As a user
  I want to rename directories in a specified path  
  So that they follow a desired numeric format.    

  Scenario: Successfully renaming directories in a clean folder  
    Given I have a directory at "D:/TestDir"  
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
</pre>
