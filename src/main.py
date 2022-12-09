from unittest.mock import patch
from bot import WhatsappBot
import unittest

class TestConsumer(unittest.TestCase):
    @patch('bot.WhatsappBot._get_intent')
    def test_my_bot_2(self, intent):
        my_bot_2 = WhatsappBot(language="es")
        expected_resp = {
                    "answer": {
                        "id": 0,
                        "message": "Perfecto, hemos guardado tu e-mail! Disfruta de la experiencia en el restaurante.",
                    },
                    "action": "hangup"
                }
        resp = my_bot_2.message("no quiero recibir nada", "ask_for_email")
        self.assertEquals(expected_resp, resp, f"Unexpected response")



if __name__ == "__main__":

    unittest.main()
    my_bot = WhatsappBot(language="en")  # Bot should re instantiated for each conversation
    my_bot_2 = WhatsappBot(language="es")
    my_bot_3 = WhatsappBot(language="en")

    # Some examples of how a conversation might start
    # Conv 1
    my_bot.message("Yes, I would like to receive notifications", "newsletter")

    # Conv 2
    my_bot.message("No, I would hate to receive notifications", "newsletter")

    # Conv 3
    my_bot.message("My email is info@bookline.io", "ask_for_email")

    # Conv 4
    my_bot.message("My email is not_a_valid_email.com", "ask_for_email")

    # Conv 5
    my_bot.message("This should not happen, so bot should hangup", "ask_for_card")

    # Example of a full conversation
    # Conv
    my_bot.message("Yes, I would like to receive notifications", "newsletter")  # bot status changes to expectingEmail
    my_bot.message("abc email", "newsletter")  # invalid email, bot status is still expecting email
    my_bot.message("abc@email.com", "newsletter")  # valid email, bot inserts email and sends hangup

    # Conv 2
    my_bot_2.message("No quiero recibir nada", "ask_for_email")

    # Conv 3
    my_bot_3.message("Yes, I'd love to!", "newsletter")
    my_bot_3.message("I prefer to get by notifications by post")
    my_bot_3.message("My address is 742 Evergreen Terrace")
    my_bot_3.message("I don't want emails")
