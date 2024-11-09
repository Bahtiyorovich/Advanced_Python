from data_manager import load_results, load_questions, update_user_score

def get_rank(score):
    """User bali asosida jadvalda o'rinni qaytaradi"""
    results = load_results()
    sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)
    for rank, user in enumerate(sorted_results, start=1):
        if user["score"] == score:
            return rank
    return len(sorted_results) + 1

def start_test(user_name):
    """Test sinovini boshlaydi va noto'g'ri javob berilguncha davom ettiradi"""
    questions = load_questions()
    score = 0

    for question in questions:
        print(f"Savol: {question['question']}")
        user_answer = input("Javob: ")

        if user_answer.lower() != question['answer'].lower():
            print("Noto'g'ri javob, test sinovi yakunlandi")
            break

        score += 1  # To'g'ri javob uchun ballni oshiramiz

    # Userning natijasini yangilash va saqlash
    update_user_score(user_name, score)
    rank = get_rank(score)
    print(f"Test natijalari: {user_name} {score} bal to'pladi, {rank}-o'rinni egalladi.\n")
