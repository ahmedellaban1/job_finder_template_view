import random
from datetime import date


def file_rename(file_name, number_digit):
    min_value = 10 ** (number_digit - 1)
    max_value = (10 ** number_digit) - 1
    name, extension = file_name.split('.')
    random_number = random.randint(min_value, max_value)
    formatted_date = date.today().strftime("%m-%Y")
    return extension, random_number, formatted_date


def company_image_uploader(instance, file_name):
    file = file_rename(file_name, 10)
    return f'Company/{file[2]}/{file[1]}_{instance.name}.{file[0]}'


def category_logo_uploader(instance, file_name):
    file = file_rename(file_name, 10)
    return f'Category/{file[2]}/{file[1]}_{instance.name}.{file[0]}'


def job_apply_cv_uploader(instance, file_name):
    file = file_rename(file_name, 10)
    return f'CVs/{file[2]}/{file[1]}_{instance.job.title}.{file[0]}'


def user_image(instance, file_name):
    file = file_rename(file_name, 10)
    return f'user/{instance.type}/{file[2]}/{instance.username}_{file[1]}_{instance.job.title}.{file[0]}'
