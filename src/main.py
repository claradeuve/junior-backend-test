from bot import WhatsappBot

if __name__ == "__main__":

    my_bot = WhatsappBot(language="en")  # Bot should re instantiated for each conversation
    my_bot_2 = WhatsappBot(language="es")
    my_bot_3 = WhatsappBot(language="en")

    # Some examples of how a conversation might start
    # Conv 1
    my_bot.message("Yes, I would like to receive notifications", "newsletter")

    # Conv 2
    my_bot.message("No, I would hate to receive notifications", "newsletter")

    # Conv 3
    my_bot.message("Which kind of notifications would I get?", "newsletter")
    # Alternativa al inicio de conversación de tipo 'newsletter'. El intent no quedaría determinado,
    # y se volvería a instar al usuario a dar una respuesta de 'sí' o 'no'.
    # Si contestara 'yes' (u otra respuesta con intent afirmativo), la conversación continuaría y seguiría el mismo itinerario que 'Conv 1'
    # Si contesara 'no' (u otra respuesta con intent negativo), la conversación finalizaría, al igual que en el caso de 'Conv 2'

    # Conv 4
    my_bot.message("My email is info@bookline.io", "ask_for_email")

    # Conv 5
    my_bot.message("My email is not_a_valid_email.com", "ask_for_email")

    # Conv 6
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
    my_bot_3.message("I prefer to get my notifications by post", "newsletter")
    my_bot_3.message("My address is 742 Evergreen Terrace", "newsletter")
    my_bot_3.message("I don't want emails", "newsletter")

    # Conv 4
    my_bot_4.message("Which kind of notifications would I get?", "newsletter")
    my_bot_4.message("Alright, I would like to receive notifications", "newsletter")
    my_bot_4.message("My email is my_name@yahoo.es", "newsletter")

