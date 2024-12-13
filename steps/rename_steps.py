from behave import given, when, then

@given('I have a directory at "{path}"')
def step_set_directory(context, path):
    """ function to set the target directory """
    print(path)
    assert False



@given('the directory contains subdirectories')
def step_set_subdirectory(context):
    """ function to set subdir passed in context.table """
    pass


@when('I run the renaming script')
def step_rename_function(context):
    """ function to rename the sub-directories in target directory """
    pass


@then('the subdirectories should be renamed')
def step_check_result(context):
    """ function to compare result with context.table """
    for row in context.table:
        print(row['result'])
    assert False

