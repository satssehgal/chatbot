from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import Flask, render_template, request

app = Flask(__name__)

botname='Normam'
chatbot = ChatBot(botname, 
	#storage_adapter='chatterbot.storage.SQLStorageAdapter',
	logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.8
        },
        {
            "import_path": "chatterbot.logic.MathematicalEvaluation",

        },
        {
            "import_path": "chatterbot.logic.UnitConversion",

        },
        {
            "import_path": "profanity_adapter.ProfanityAdapter",

        },
        {
            "import_path": "covid19_adapter.Covid19Adapter",

        },
        {
            "import_path": "alarm.AlarmAdapter",

        },
    ],
 )

@app.route("/")
def home():
    return render_template("index.html", botname=botname)

@app.route("/get")
def get_bot_response():
	userInput=request.args.get('msg')
	return str(chatbot.get_response(userInput))

if __name__ == '__main__':
	app.run(port=5500)
