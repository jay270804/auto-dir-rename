import os
from behave import given, when, then

@given('I have a directory at "{path}"')
def step_set_directory(context, path):
    """ function to set the target directory """
    context.target_directory = path
    pass


@given('the directory contains subdirectories')
def step_set_subdirectory(context):
    """ function to set subdir passed in context.table """
    context.sub_dir_list = [row['subdir'] for row in context.table]
    # print(sub_dir_list)


@when('I run the renaming script')
def step_rename_function(context):
    """ function to rename the sub-directories in target directory """

    target_directory=context.target_directory

    if context.sub_dir_list:
        sub_dir_list=context.sub_dir_list
    else:
        sub_dir_list=os.listdir(target_directory)

    for index, dir in enumerate(sub_dir_list, start=1):
        old_path=os.path.join(target_directory, dir)
        new_path=os.path.join(target_directory,f"{index}. {dir}")

        try:
            if os.path.isdir(old_path):
                os.rename(old_path,new_path)
                print(f"Directory renamed from {dir} to {index}. {dir}")
        except Exception as e:
            print(e)


@then('the subdirectories should be renamed')
def step_check_result(context):
    """ function to compare result with context.table """
    for row in context.table:
        print(row['result'])
    pass


