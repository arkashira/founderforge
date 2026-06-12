import pytest
from src.chatbot import Chatbot

def test_answer():
    chatbot = Chatbot()
    question = "What is Python?"
    answer = chatbot.answer(question)
    assert answer == "Python is a programming language."

def test_hand_off_to_human():
    chatbot = Chatbot()
    question = "What is the meaning of life?"
    answer = chatbot.hand_off_to_human(question)
    assert answer.startswith("Handing off to human mentor")

def test_log_conversation():
    chatbot = Chatbot()
    question = "What is AI?"
    answer = chatbot.answer(question)
    chatbot.log_conversation(question, answer)
    assert len(chatbot.conversations) == 1

def test_get_answer():
    chatbot = Chatbot()
    question = "What is Python?"
    answer = chatbot.get_answer(question)
    assert answer == "Python is a programming language."

def test_get_answer_hand_off():
    chatbot = Chatbot()
    question = "What is the meaning of life?"
    answer = chatbot.get_answer(question)
    assert answer.startswith("Handing off to human mentor")

def test_get_answer_timeout():
    chatbot = Chatbot()
    question = "What is the meaning of life?"
    chatbot.knowledge_base = {question: "Answer after 5 seconds"}
    answer = chatbot.get_answer_with_timeout(question)
    assert answer.startswith("Handing off to human mentor")
