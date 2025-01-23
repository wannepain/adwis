import spacy 
nlp = spacy.load("en_core_web_md")
# corpus = inicialize_medium_corpus()


def evaluate (history):
    responses = []
    question_intents = []
    
    scores = set()
    for response in history:
        if response["client"]:
            responses.append(response["client"])
            question_intents.append(response["bot"]["Intent"])
    iter = 0
    for response in responses:
        example_responses = history[iter]["bot"]['example_responses']
        question_intent= question_intents[iter]
        score = select_simlar(response, example_responses)
        for record in scores:
            if record[0] == question_intent:
                record[1] += score
                break
            else:
                scores.add([question_intent, score])

def select_simlar(response, example_responses):
    max_similarity = -1
    most_similar_response = None
    
    for example_response in example_responses.values():
        response_doc = nlp(response)
        response_no_stop_words = nlp(' '.join([str(t) for t in response_doc if not t.is_stop]))
        lemmatised_response = nlp(' '.join([str(t.lemma_) for t in response_no_stop_words if not t.is_stop]))
        example_response_doc = nlp(example_response)
        example_response_no_stop_words = nlp(' '.join([str(t) for t in example_response_doc if not t.is_stop]))
        lemmatized_example_response = nlp(' '.join([str(t.lemma_) for t in example_response_no_stop_words]))
    
        similarity = lemmatised_response.similarity(lemmatized_example_response)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_response = example_response

    key_of_most_similar_response = list(example_responses.keys())[list(example_responses.values()).index(most_similar_response)]
    print(key_of_most_similar_response)
    score = int(key_of_most_similar_response)
    return score
    

