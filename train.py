from app import chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pathlib


trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    str(pathlib.Path().absolute())+'/english/',
)
