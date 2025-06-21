from app.infrastructure.config import Base, engine
from app.infrastructure.database.models import task, todo_list
from colorama import init, Fore

def create_tables():

    try:
        init(autoreset=True)
        Base.metadata.create_all(bind=engine)
        print(Fore.GREEN + "✅ Database available! Tables created successfully.")
    except Exception as e:
        print(Fore.RED + f"❌ Failed to create tables: {e}")

if __name__ == "__main__":
    create_tables()
