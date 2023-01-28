from application.config.paths import FILES_OUTPUT_PATH
from application.body.usersgenerator import generate_users
from application.body.request_to_api import get_csv_file_data_and_calculate


def write_users_into_file(filename: str = None, count: int = 100) -> None:
    path_to_file = FILES_OUTPUT_PATH.joinpath(f"{filename}.txt")
    with open(path_to_file, mode="w") as file:
        for user in generate_users(number=count):
            file.write(f"{user.name}  {user.email}\n")


def write_average_data_into_file(filename: str = None, link: str = None) -> None:
    path_to_file = FILES_OUTPUT_PATH.joinpath(f"{filename}.txt")
    with open(path_to_file, mode="w") as file:
        result = get_csv_file_data_and_calculate(link)
        file.write(
            f" Average height is {result['average_height']} sm, Average width is {result['average_weight']} kg\n"
        )
