import unittest
from unittest.mock import patch
from bot import WhatsappBot


class TestNewsletter(unittest.TestCase):
    @patch('api.BooklineAPI.insert_customer_email')
    def test_conv1(self, email):
        with patch.object(WhatsappBot, '_get_intent', return_value='confirm') as mock_method:
            my_bot = WhatsappBot(language="en")
            my_bot.message("Yes, I would like to receive notifications", "newsletter")
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            my_bot.message("abc email", "newsletter")
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            resp = my_bot.message("abc@email.com", "newsletter")
            
        expected_message = "Perfect, we've stored your e-mail! Enjoy the experience at the restaurant"
        actual_message = resp['answer']['message']

        expected_action = "continue"
        actual_action = resp['action']

        self.assertEqual(expected_message, actual_message, "Unexpected message")
        self.assertEqual(expected_action, actual_action, "Unexpected action")

    
    def test_conv3(self):
        with patch.object(WhatsappBot, '_get_intent', return_value='confirm') as mock_method:
            my_bot_3 = WhatsappBot(language="en")
            my_bot_3.message("Yes, I'd love to!", "newsletter")
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            my_bot_3.message("I prefer to get my notifications by post", "newsletter")
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            my_bot_3.message("My address is 742 Evergreen Terrace", "newsletter")
        with patch.object(WhatsappBot, '_get_intent', return_value='reject') as mock_method:
            resp = my_bot_3.message("I don't want emails", "newsletter")

        expected_message = "Okay, I hope you enjoy the experience at the restaurant"
        actual_message = resp['answer']['message']

        expected_action = "continue"
        actual_action = resp['action']

        self.assertEqual(expected_message, actual_message, "Unexpected message")
        self.assertEqual(expected_action, actual_action, "Unexpected action")


    @patch('api.BooklineAPI.insert_customer_email')
    def test_conv4(self, email):
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            my_bot4 = WhatsappBot(language="en")
            my_bot4.message("Which kind of notifications would I get?", "newsletter")
        with patch.object(WhatsappBot, '_get_intent', return_value='confirm') as mock_method:
            my_bot4.message("Alright, I would like to receive notifications", "newsletter")
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            resp = my_bot4.message("My email is my_name@yahoo.es", "newsletter")
            
        expected_message = "Perfect, we've stored your e-mail! Enjoy the experience at the restaurant"
        actual_message = resp['answer']['message']

        expected_action = "continue"
        actual_action = resp['action']

        self.assertEqual(expected_message, actual_message, "Unexpected message")
        self.assertEqual(expected_action, actual_action, "Unexpected action")

    
    def test_conv5(self):
        with patch.object(WhatsappBot, '_get_intent', return_value='reject') as mock_method:
            my_bot_5 = WhatsappBot(language="en")
            resp = my_bot_5.message("No, I would hate to receive notifications", "newsletter")

        expected_message = "Okay, I hope you enjoy the experience at the restaurant"
        actual_message = resp['answer']['message']

        expected_action = "hangup"
        actual_action = resp['action']

        self.assertEqual(expected_message, actual_message, "Unexpected message")
        self.assertEqual(expected_action, actual_action, "Unexpected action")
   



class TestAskForEmail(unittest.TestCase):
    @patch('api.BooklineAPI.insert_customer_email')
    def test_conv2(self, email):
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            my_bot_2 = WhatsappBot(language="es")
            resp = my_bot_2.message("No quiero recibir nada", "ask_for_email")
            
        expected_message = "Este e-mail no parece válido. Por favor, revisalo de nuevo"
        actual_message = resp['answer']['message']

        expected_action = "continue"
        actual_action = resp['action']

        self.assertEqual(expected_message, actual_message, "Unexpected message")
        self.assertEqual(expected_action, actual_action, "Unexpected action")


if __name__ == "__main__":
    unittest.main()