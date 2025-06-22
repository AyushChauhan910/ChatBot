#!/usr/bin/env python3
"""
Demo Script for Financial Analysis Chatbot
This script demonstrates the chatbot functionality with automated testing
"""

from financial_chatbot import FinancialChatbot
import time

def run_demo():
    """Run automated demo of the chatbot"""
    print("=" * 70)
    print("FINANCIAL ANALYSIS CHATBOT - AUTOMATED DEMO")
    print("=" * 70)

    # Initialize chatbot
    chatbot = FinancialChatbot()

    # Test queries
    test_queries = [
        "What is the total revenue?",
        "Which company has the highest revenue?",
        "What is Tesla's growth rate?",
        "How has Microsoft's net income changed?",
        "Compare revenue across companies",
        "What is Apple's recent performance?",
        "Tesla growth",  # Test partial matching
        "Microsoft income",  # Test partial matching
        "help",  # Test help command
        "What is Google's revenue?"  # Test unknown query
    ]

    print("Testing all predefined queries...\n")

    for i, query in enumerate(test_queries, 1):
        print(f"Test {i}: {query}")
        print("-" * 50)

        # Simulate user input
        response = chatbot.simple_chatbot(query)
        print(f"Response: {response}")
        print()

        # Small delay for readability
        time.sleep(0.5)

    print("=" * 70)
    print("DEMO COMPLETED SUCCESSFULLY")
    print("=" * 70)
    print("All queries processed successfully!")
    print("The chatbot is ready for interactive use.")
    print("\nTo start interactive mode, run: python financial_chatbot.py")
    print("To start web interface, run: python flask_chatbot.py")

if __name__ == "__main__":
    run_demo()
