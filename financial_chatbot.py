#!/usr/bin/env python3
"""
Financial Analysis Chatbot Prototype
A simple chatbot that responds to predefined financial queries about Microsoft, Tesla, and Apple
based on their 10-K filings analysis.
"""

import datetime

class FinancialChatbot:
    def __init__(self):
        # Financial data from the previous analysis
        self.financial_data = {
            'microsoft': {
                '2024': {'revenue': 245122, 'net_income': 88136},
                '2023': {'revenue': 211915, 'net_income': 72361},
                'growth_rate': 15.7  # 2023 to 2024 revenue growth
            },
            'tesla': {
                '2023': {'revenue': 96773, 'net_income': None},
                '2022': {'revenue': 81462, 'net_income': 12556},
                '2021': {'revenue': 53823, 'net_income': 5524},
                'cagr': 34.0  # Compound Annual Growth Rate 2021-2023
            },
            'apple': {
                '2024': {'revenue': 391035, 'net_income': None},
                '2023': {'revenue': 383285, 'net_income': None},
                '2022': {'revenue': 394328, 'net_income': None},
                'growth_2024': 2.0  # 2023 to 2024 growth
            }
        }

        # Predefined queries and their responses
        self.queries = {
            "what is the total revenue?": self.get_total_revenue,
            "which company has the highest revenue?": self.get_highest_revenue_company,
            "what is tesla's growth rate?": self.get_tesla_growth,
            "how has microsoft's net income changed?": self.get_microsoft_income_change,
            "compare revenue across companies": self.compare_revenues,
            "what is apple's recent performance?": self.get_apple_performance
        }

    def get_total_revenue(self):
        """Calculate total revenue across all companies for latest available year"""
        microsoft_2024 = self.financial_data['microsoft']['2024']['revenue']
        tesla_2023 = self.financial_data['tesla']['2023']['revenue']
        apple_2024 = self.financial_data['apple']['2024']['revenue']

        total = microsoft_2024 + tesla_2023 + apple_2024
        return f"Total combined revenue: Microsoft (2024): ${microsoft_2024:,}M, Tesla (2023): ${tesla_2023:,}M, Apple (2024): ${apple_2024:,}M. Combined total: ${total:,}M"

    def get_highest_revenue_company(self):
        """Identify company with highest revenue"""
        return "Apple has the highest revenue at $391,035M in fiscal 2024, followed by Microsoft at $245,122M (2024), and Tesla at $96,773M (2023)."

    def get_tesla_growth(self):
        """Get Tesla's growth information"""
        cagr = self.financial_data['tesla']['cagr']
        return f"Tesla demonstrates exceptional growth with a compound annual growth rate (CAGR) of approximately {cagr}% from 2021-2023, growing from $53,823M to $96,773M in revenue."

    def get_microsoft_income_change(self):
        """Get Microsoft's net income change"""
        income_2024 = self.financial_data['microsoft']['2024']['net_income']
        income_2023 = self.financial_data['microsoft']['2023']['net_income']
        change = ((income_2024 - income_2023) / income_2023) * 100
        return f"Microsoft's net income increased from ${income_2023:,}M in 2023 to ${income_2024:,}M in 2024, representing a {change:.1f}% increase."

    def compare_revenues(self):
        """Compare revenues across all companies"""
        return """Revenue Comparison (Latest Available Year):
        1. Apple (2024): $391,035M - Market leader with largest revenue base
        2. Microsoft (2024): $245,122M - Strong enterprise and cloud growth
        3. Tesla (2023): $96,773M - Fastest growing but smallest of the three

        Growth Patterns: Tesla shows highest growth rate (~34% CAGR), Microsoft shows steady growth (15.7% YoY), Apple shows modest recovery (2.0% growth in 2024)."""

    def get_apple_performance(self):
        """Get Apple's recent performance"""
        return "Apple's recent performance shows recovery with 2.0% revenue growth in 2024 ($391,035M) after a decline in 2023. Despite slower growth compared to competitors, Apple maintains the largest revenue base among the three tech giants."

    def simple_chatbot(self, user_query):
        """Main chatbot function using if-else logic"""
        user_query_lower = user_query.lower().strip()

        # Direct query matching
        if user_query_lower in self.queries:
            return self.queries[user_query_lower]()

        # Partial matching for flexibility
        elif "revenue" in user_query_lower and ("total" in user_query_lower or "combined" in user_query_lower):
            return self.get_total_revenue()
        elif "highest" in user_query_lower and "revenue" in user_query_lower:
            return self.get_highest_revenue_company()
        elif "tesla" in user_query_lower and "growth" in user_query_lower:
            return self.get_tesla_growth()
        elif "microsoft" in user_query_lower and ("income" in user_query_lower or "profit" in user_query_lower):
            return self.get_microsoft_income_change()
        elif "compare" in user_query_lower and "revenue" in user_query_lower:
            return self.compare_revenues()
        elif "apple" in user_query_lower and "performance" in user_query_lower:
            return self.get_apple_performance()
        elif "help" in user_query_lower or "commands" in user_query_lower:
            return self.get_help()
        else:
            return """Sorry, I can only provide information on predefined queries. Try asking:
            - 'What is the total revenue?'
            - 'Which company has the highest revenue?'
            - 'What is Tesla's growth rate?'
            - 'How has Microsoft's net income changed?'
            - 'Compare revenue across companies'
            - 'What is Apple's recent performance?'
            - 'Help' for this message"""

    def get_help(self):
        """Display available commands"""
        return """Available Financial Queries:
        1. 'What is the total revenue?' - Get combined revenue figures
        2. 'Which company has the highest revenue?' - Revenue leader identification
        3. 'What is Tesla's growth rate?' - Tesla's growth analysis
        4. 'How has Microsoft's net income changed?' - Microsoft profitability trends
        5. 'Compare revenue across companies' - Cross-company revenue comparison
        6. 'What is Apple's recent performance?' - Apple's recent financial performance

        You can also use partial phrases like 'Tesla growth' or 'Microsoft income'."""

def main():
    """Main function to run the chatbot"""
    chatbot = FinancialChatbot()

    print("=" * 60)
    print("Financial Analysis Chatbot - Microsoft, Tesla & Apple")
    print("=" * 60)
    print("Welcome! I can answer questions about financial data from these companies.")
    print("Type 'help' to see available queries or 'quit' to exit.")
    print("=" * 60)

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Chatbot: Thank you for using the Financial Analysis Chatbot!")
                break

            if not user_input:
                print("Chatbot: Please enter a query or type 'help' for available commands.")
                continue

            response = chatbot.simple_chatbot(user_input)
            print(f"Chatbot: {response}")

        except KeyboardInterrupt:
            print("\n\nChatbot: Goodbye!")
            break
        except Exception as e:
            print(f"Chatbot: An error occurred: {e}")

if __name__ == "__main__":
    main()
