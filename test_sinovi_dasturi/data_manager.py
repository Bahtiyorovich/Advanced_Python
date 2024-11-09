import json
import os

def load_questions():
    """Savollarni questions.json faylidan yuklaydigan funksiya"""
    with open('questions.json', 'r') as file:
        return json.load(file)


def load_results():
    """User ma'lumotlarini results.json faylidan o'qiydigan funksiya"""
    if not os.path.exists('results.json'):
        return [] #agar fayl mavjud bo'lmasa bo'sh ro'yxat yaratadi

    with open('results.json', 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return [] #fayl bo'sh yoki noto'g'ri formatda bo'lsa bo'sh ro'yxat qaytaradi


def save_results(results):
    """User natijalarini results.json fayliga yozadigan funksiya"""
    with open('results.json', 'w') as file:
        json.dump(results, file, indent = 4)

def update_user_score(user_name, score):
    """Userning mavjud natijalarini yangilaydi"""
    results = load_results()
    for user in results:
        if user["name"] == user_name:
            user['score'] = score
            save_results(results)
            return

    results.append({"name": user_name, "score": score})
    save_results(results)






















































































