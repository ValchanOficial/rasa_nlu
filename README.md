# Rasa 3.x NLU - Github API


- **python3 -m venv ./venv** - Create a virtual environment
- **source ./venv/bin/activate** - Activate the virtual environment
- **python3 -m pip install -r requirements.txt** - Install dependencies

- **rasa train** - # Train a model
- **rasa run actions** - # Run the action server - http://0.0.0.0:5055
- **rasa shell** - # Talk to the chatbot on the command line
- **/stop** - # Stop the conversation - on the command line  

![rasa](https://github.com/ValchanOficial/rasa_nlu/assets/16228014/09851d76-1779-45b9-8cc6-3775eaf7dda6)

POST http://localhost:5055/webhook  
Payload:
```json
{
    "next_action": "action_name",
    "tracker": {
        "sender_id": "user_id",
        "slots": {
            "slot_name": "slot_value"
        },
        "latest_message": {
            "text": "latest_message_from_user"
        }
    }
}
```



https://rasa.com/docs/rasa/playground/


