from application.config.paths import FILES_INPUT_PATH
from application.logging.loggers import get_core_logger
from faker import Faker

fake = Faker()


def to_create_file(file_name: str = None) -> None:
    logger = get_core_logger()
    path_to_file = FILES_INPUT_PATH.joinpath(f"{file_name}.txt")
    with open(path_to_file, mode="w") as file:
        file.write(f"{fake.text()}")
    logger.info(f"Path to file: {path_to_file}")


def to_read_file(file_name: str = None) -> None:
    path_to_file = FILES_INPUT_PATH.joinpath(f"{file_name}.txt")
    file_contents = path_to_file.read_text()
    print(file_contents)
