import unittest
from unittest.mock import patch
from bot import WhatsappBot


class TestConv_1(unittest.TestCase):
    def test_confirm(self):
        with patch.object(WhatsappBot, '_get_intent', return_value='confirm') as mock_method:
            my_bot = WhatsappBot(language="en")

            expected_resp = {
                        "answer": {
                            "id": 0,
                            "message": "Great! Please, let me know your e-mail",
                        },
                        "action": "continue"
                    }
            resp = my_bot.message("Yes, I would like to receive notifications", "newsletter")
            actual_message = resp['answer']['message']
            print("Input: Yes, I would like to receive notifications", "newsletter")
            print(f"Output: {actual_message}")

            self.assertEqual(expected_resp, resp, "Unexpected response")

    @patch('api.BooklineAPI.insert_customer_email')
    def test_give_email_1st(self, email):
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            my_bot = WhatsappBot(language="en")
            my_bot.conversation_status = "expectingEmail"
            

            expected_resp = {
                        "answer": {
                            "id": 0,
                            "message": "It seems that this e-mail is not valid. Please make sure it's correct",
                        },
                        "action": "continue"
                    }
            resp = my_bot.message("abc email", "newsletter")
            actual_message = resp['answer']['message']
            print("Input: abc email")
            print(f"Output: {actual_message}")

            self.assertEqual(expected_resp, resp, "Unexpected response")

    @patch('api.BooklineAPI.insert_customer_email')
    def test_give_email_2nd(self, email):
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            my_bot = WhatsappBot(language="en")
            my_bot.conversation_status = "expectingEmail"

            expected_resp = {
                        "answer": {
                            "id": 0,
                            "message": "Perfect, we've stored your e-mail! Enjoy the experience at the restaurant",
                        },
                        "action": "continue"
                    }
            resp = my_bot.message("abc@email.com", "newsletter")
            actual_message = resp['answer']['message']
            print("Input: abc@email.com")
            print(f"Output: {actual_message}")

            self.assertEqual(expected_resp, resp, "Unexpected response")


class TestConv_2(unittest.TestCase):
    @patch('api.BooklineAPI.insert_customer_email')
    def test_my_bot_2(self, email):
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            my_bot_2 = WhatsappBot(language="es")
            my_bot_2._get_intent("undefined")
            
            expected_resp = {
                        "answer": {
                            "id": 0,
                            "message": "Este e-mail no parece válido. Por favor, revisalo de nuevo",
                        },
                        "action": "continue"
                    }
            
            
            resp = my_bot_2.message("No quiero recibir nada", "ask_for_email")
            actual_message = resp['answer']['message']
            print("Input: No quiero recibir nada")
            print(f"Output: {actual_message}")

            self.assertEqual(expected_resp, resp, "Unexpected response")



class TestConv_3(unittest.TestCase):
    def test_confirm(self):
        with patch.object(WhatsappBot, '_get_intent', return_value='confirm') as mock_method:
            my_bot_3 = WhatsappBot(language="en")
            my_bot_3._get_intent("confirm")
            my_bot_3.conversation_status = "start"

            expected_resp = {
                        "answer": {
                            "id": 0,
                            "message": "Great! Please, let me know your e-mail",
                        },
                        "action": "continue"
                    }
            resp = my_bot_3.message("Yes, I'd love to!", "newsletter")
            actual_message = resp['answer']['message']
            print("Input: Yes, I'd love to!")
            print(f"Output: {actual_message}")

            self.assertEqual(expected_resp, resp, "Unexpected response")


    def test_enter_email_1st(self):
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            my_bot_3 = WhatsappBot(language="en")
            my_bot_3._get_intent("undefined")
            my_bot_3.conversation_status = "expectingEmail"
    
            expected_resp = {
                        "answer": {
                            "id": 0,
                            "message": "It seems that this e-mail is not valid. Please make sure it's correct",
                        },
                        "action": "continue"
                    }
            resp = my_bot_3.message("I prefer to get my notifications by post", "newsletter")
            actual_message = resp['answer']['message']
            print("Input: I prefer to get my notifications by post")
            print(f"Output: {actual_message}")

            self.assertEqual(expected_resp, resp, "Unexpected response")


    def test_enter_email_2nd(self):
        with patch.object(WhatsappBot, '_get_intent', return_value='undefined') as mock_method:
            my_bot_3 = WhatsappBot(language="en")
            my_bot_3._get_intent("undefined")
            my_bot_3.conversation_status = "expectingEmail"
    
            expected_resp = {
                        "answer": {
                            "id": 0,
                            "message": "It seems that this e-mail is not valid. Please make sure it's correct",
                        },
                        "action": "continue"
                    }
            resp = my_bot_3.message("My address is 742 Evergreen Terrace", "newsletter")
            actual_message = resp['answer']['message']
            print("Input: My address is 742 Evergreen Terrace")
            print(f"Output: {actual_message}")

            self.assertEqual(expected_resp, resp, "Unexpected response")

    @patch('api.BooklineAPI.insert_customer_email')
    def test_reject_emails(self, email):
        with patch.object(WhatsappBot, '_get_intent', return_value='reject') as mock_method:
            my_bot_3 = WhatsappBot(language="en")
            my_bot_3._get_intent("reject")
            my_bot_3.conversation_status = "expectingEmail"
            

            expected_resp = {
                        "answer": {
                            "id": 0,
                            "message": "Okay, I hope you enjoy the experience at the restaurant",
                        },
                        "action": "continue"
                    }
            resp = my_bot_3.message("I don't want emails", "newsletter")
            actual_message = resp['answer']['message']
            print("Input: I don't want emails")
            print(f"Output: {actual_message}")

            self.assertEqual(expected_resp, resp, "Unexpected response")


if __name__ == "__main__":
    unittest.main()