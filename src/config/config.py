import dotenv
import os

dotenv.load_dotenv()

config: dict = {
    'db_url': os.getenv('DB_URL')
}