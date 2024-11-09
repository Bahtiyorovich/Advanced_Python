from test_manager import start_test

def main():
    """Dastur boshqaruvi, userga qayta sinovdan o'tish imkoniyati beriladi"""
    while True:
        user_name = input("Ismingizni kiriting >>> ").strip()
        if not user_name:
            print("Iltimos, ismingizni kiriting!")
            continue

        print(f"{user_name}, agar avval sinovdan o'tgan bo'lsangiz, natijangiz yangilanadi.")
        start_test(user_name)

        retry = input("Yana test sinovida qatnashasizmi? (ha/yo'q): >>> ").lower()
        if retry != 'ha':
            print("Test sinovi yakunlandi!")
            break

if __name__ == "__main__":
    main()