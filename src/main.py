from handlers.instagram_handler import send_messages_to_users
from handlers.file_handler import read_usernames_from_file
from handlers.gpt_handler import generate_test_message

if __name__ == "__main__":
    # filepath = "src/data/profiles.txt"
    # usernames = read_usernames_from_file(filepath)
    # mensagem = "Olá! Essa é uma mensagem automática personalizada para mais de um perfil."
    # send_messages_to_users(usernames, mensagem)
    print(generate_test_message())
