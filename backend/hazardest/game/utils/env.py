import os

import dotenv

dotenv_filename = f'.env.{os.getenv("HAZARDEST_ENV")}'
try:
    dotenv_path = dotenv.find_dotenv(filename=dotenv_filename, raise_error_if_not_found=True)
except OSError:
    raise ValueError(
        'Must set HAZARDEST_ENV to the key of a .env file in the project directory. e.g. "local" for .env.local')

env_config = {
    **dotenv.dotenv_values(dotenv_path),  # load env variables
    **os.environ,  # override loaded values with environment variables
}
