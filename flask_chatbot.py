#!/usr/bin/env python3
"""
Flask Web Version of Financial Analysis Chatbot
A web-based interface for the financial chatbot
"""

from flask import Flask, render_template, request, jsonify
import sys
import os

# Import our chatbot class
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from financial_chatbot import FinancialChatbot

app = Flask(__name__)
chatbot = FinancialChatbot()

@app.route('/')
def home():
    """Render the main chatbot interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'response': 'Please enter a message.'})

        # Get response from chatbot
        bot_response = chatbot.simple_chatbot(user_message)

        return jsonify({'response': bot_response})

    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})

@app.route('/help')
def help_page():
    """Display help information"""
    help_text = chatbot.get_help()
    return jsonify({'response': help_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
