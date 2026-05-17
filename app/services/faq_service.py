from rapidfuzz import fuzz
import json
import os

APP_LANG = os.getenv("APP_LANG", "en")
FAQ_PATH = os.path.join(os.path.dirname(__file__), f"../data/{APP_LANG}/faq.json")


class FAQService:
    def __init__(self):
        with open(FAQ_PATH, "r", encoding="utf-8") as f:
            self.faq_data = json.load(f)

    def find_answer(self, user_question: str):
        user_question = user_question.lower()
        best_score = 0
        best_answer = None

        for item in self.faq_data:
            score = fuzz.partial_ratio(user_question, item["question"])

            if score > best_score:
                best_score = score
                best_answer = item["answer"]

        # threshold
        print(best_score)
        if best_score > 70:
            return best_answer

        return None


faq_service = FAQService()
