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
            
            actual_resp = resp['answer']['message']
            expected_resp = "Perfect, we've stored your e-mail! Enjoy the experience at the restaurant"

            self.assertEqual(expected_resp, actual_resp, "Unexpected response")


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

            expected_resp = "Okay, I hope you enjoy the experience at the restaurant"
            actual_resp = resp['answer']['message']

            self.assertEqual(expected_resp, actual_resp, "Unexpected response")



if __name__ == "__main__":
    unittest.main()