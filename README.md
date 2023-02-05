# AYUR CHATBOT

## Abstract: 
A chatbot which envisions the users about their body type based on Indian traditional medicine (Ayurveda). The bot is composed of the basic architecture of RASA where the two main components are natural language understanding and dialogue management. Our body is composed of doshas according to the ayurvedic books which are primarily of 3 categories namely the Vata, Pitta, and Kapha describing the perpetual features of our interests and invoking a better understanding of ourselves. The results depict the probability of the user having a particular dosha as their foremost quality compared to others. 
    
## RASA Model Architecture:

![alt text](https://rasa.com/docs/rasa/img/architecture.png)


## NLU PIPELINE:
NLU is the part that handles intent classification, entity extraction, and response retrieval. In the image the NLU Pipeline process the user utterances whose intent needs to be found. 
    
## DIALOGUE POLICIES:
The dialogue management component decides the following action in a conversation based on the context. 


## ACTION SERVER:
Whenever the assistant predicts the custom action, the model sends the POST request to the action server with a json payload including the name of the expected action, the conversation ID, the contents of the tracker and the contents of the domain. When the action is about to complete it returns a json payload of responses and events. See the API spec for details about the request and response payloads. The model then returns the responses to the user and adds the events to the conversation tracker.

## TRACKER STORE:
The assistant’s conversations are stored here. Rasa supports the implementation of different store types and can be customized as well.
    
## LOCK STORE:
Rasa locks conversations while messages are being actively processed and use a ticket lock mechanism to ensure that incoming messages for a specific conversation ID are processed in the proper sequence. As a result, many Rasa servers can be run simultaneously as replicated services, and clients are no longer required to transmit messages to the same node when using a particular discussion ID.

## ARCHITECTURE OF NLU USED:
Dual Intent and Entity Transformer (DIET) is the lightweight, multitask transformer architecture used for NLU. This handles both intent classification and entity recognition together. DIET uses a sequence model that takes word order into account, thereby offering better performance. It's also a more compact model with a plug-and-play, modular architecture. Additionally, DIET is not only considerably faster to train but also parallels large-scale pre-trained language models in performance. It outperforms fine-tuning BERT and improves upon the current state of the art on a complex NLU dataset. Achieving state-of-the-art accuracy may no longer mean sacrificing efficiency.


