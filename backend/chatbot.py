import spacy
nlp = spacy.load("en_core_web_md")

def check_sim (question_intents, response):
  max_similarity = -1
  most_similar_entry = None
  for entry in question_intents:
    # Create a doc for the Question_Text of each entry
    question_doc = nlp(entry)

    # Calculate similarity
    response_doc = nlp(response)
    response_no_stop_words = nlp(' '.join([str(t) for t in response_doc if not t.is_stop]))
    similarity = response_no_stop_words.similarity(question_doc)

    # Track the entry with the highest similarity score
    if similarity > max_similarity:
        max_similarity = similarity
        most_similar_entry = entry

  return most_similar_entry

def respond(history,corpus):
  """
  asks question after latest client response

  Args:
    history: array eg.: [{"bot":corpus[id],"client":"I like drawing"}, ...]
    corpus: Question corpus for chatbot 
  """

  if len(history) == 0:
  # question id = 0
    history.append({"bot":corpus[0], "client":None})
  else:
    prev_question_data = history[len(history)-1]["bot"]
    prev_questions_intents = prev_question_data["following_intent"]
    response = history[len(history)-1]['client']

    most_similar_entry = check_sim(prev_questions_intents, response)

    q_iteration = 0
    for question in corpus:
      if question["Intent"] == most_similar_entry:
        history.append({"bot":question, "client": None})
      else:
        q_iteration += 1