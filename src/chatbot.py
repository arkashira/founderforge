import json
import time
from dataclasses import dataclass
from typing import List
import threading

@dataclass
class Conversation:
    questions: List[str]
    answers: List[str]

class Chatbot:
    def __init__(self):
        self.conversations = []
        self.knowledge_base = {
            "What is Python?": "Python is a programming language.",
            "What is AI?": "AI stands for Artificial Intelligence.",
        }
        self.answer_lock = threading.Lock()

    def answer(self, question):
        if question in self.knowledge_base:
            return self.knowledge_base[question]
        else:
            return None

    def hand_off_to_human(self, question):
        return f"Handing off to human mentor for question: {question}"

    def log_conversation(self, question, answer):
        conversation = Conversation([question], [answer])
        self.conversations.append(conversation)

    def get_answer(self, question):
        start_time = time.time()
        attempts = 0
        while attempts < 3:
            answer = self.answer(question)
            if answer is not None:
                self.log_conversation(question, answer)
                return answer
            attempts += 1
            if time.time() - start_time > 3:
                break
        return self.hand_off_to_human(question)

    def main(self):
        while True:
            question = input("User: ")
            answer = self.get_answer(question)
            print("Chatbot:", answer)

    def slow_answer(self, question):
        time.sleep(5)
        return self.knowledge_base.get(question)

    def get_answer_with_timeout(self, question):
        result = []
        def target():
            answer = self.slow_answer(question)
            with self.answer_lock:
                result.append(answer)
        thread = threading.Thread(target=target)
        thread.start()
        thread.join(timeout=3)
        if thread.is_alive():
            return self.hand_off_to_human(question)
        with self.answer_lock:
            return result[0] if result else self.hand_off_to_human(question)

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.main()
