from application.body.request_to_api import get_astronaut_from_json
from application.body.write_to_file import write_users_into_file, write_average_data_into_file
from application.body.actions_with_files import to_create_file, to_read_file
import asyncio

if __name__ == "__main__":
    asyncio.run(get_astronaut_from_json())
    write_users_into_file(filename="generated_users", count=100)
    write_average_data_into_file(
        filename="average", link="https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"
    )
    to_create_file(file_name="text")
    to_read_file(file_name="text")
