small_corpus = [
 {
        "ID": "1",
        "Intent": "General",
        "Question_Text": "Hi! I’m here to help you explore your skills and interests. Ready to start?",
        "Follow_Up": "",
        "Expected_Answers": ["Yes", "No"],
        "Next_Step_Yes": "2",
        "Next_Step_No": "0",
        "following_intent": [] #add all categories
    },
    {
        "ID": "2",
        "Intent": "Interest Identification",
        "Question_Text": "What’s something you really enjoy doing in your free time?",
        "following_intent": []
    },
    {
        "ID": "4",
        "Intent": "Skill Discovery",
        "Question_Text": "Have you ever been told you’re good at something? If so, what is it?",
        "following_intent": []
    },
    {
        "ID": "6",
        "Intent": "Value Identification",
        "Question_Text": "What’s more important to you: creativity, logic, or helping others?",
        "following_intent": []
    },
    {
        "ID": "7",
        "Intent": "Goal Setting",
        "Question_Text": "Do you have any goals for your future? If yes, can you describe one?",
        "following_intent": []
    },
    {
        "ID": "8",
        "Intent": "Activity Preference",
        "Question_Text": "Do you prefer working on long-term projects or short, quick tasks?",
        "following_intent": []
    },
    {
        "ID": "9",
        "Intent": "Personal Reflection",
        "Question_Text": "If you could choose any job without thinking about money, what would it be?",
        "following_intent": []
    },
    {
        "ID": "10",
        "Intent": "Interest Expansion",
        "Question_Text": "Would you like to explore careers related to your interests or try something completely new?",
        "following_intent": []
    },
    {
        "ID": "11",
        "Intent": "Learning Style",
        "Question_Text": "How do you prefer to learn new things?",
        "following_intent": []
    }

]

medium_corpus = [
    {
        "ID": "1",
        "Intent": "General",
        "Question_Text": "Hi! I’m here to help you explore your skills and interests. Ready to start?",
        "Follow_Up": "",
        "Expected_Answers": ["Yes", "No"],
        "Next_Step_Yes": "2",
        "Next_Step_No": "0"
    },
    {
        "ID": "2",
        "Intent": "Interest Identification",
        "Question_Text": "What’s something you really enjoy doing in your free time?",
        "Follow_Up": "Can you share why you enjoy it?",
        "Expected_Answers": ["Sports", "Reading", "Art", "Music", "Other"],
        "Next_Step_Yes": "3",
        "Next_Step_No": "0"
    },
    {
        "ID": "3",
        "Intent": "Interest Identification",
        "Question_Text": "Do you prefer working with people, technology, or ideas?",
        "Follow_Up": "Why do you feel this suits you best?",
        "Expected_Answers": ["People", "Technology", "Ideas"],
        "Next_Step_Yes": "4",
        "Next_Step_No": "0"
    },
    {
        "ID": "4",
        "Intent": "Skill Discovery",
        "Question_Text": "Have you ever been told you’re good at something? If so, what is it?",
        "Follow_Up": "How did you discover this skill?",
        "Expected_Answers": ["Yes", "No"],
        "Next_Step_Yes": "5",
        "Next_Step_No": "6"
    },
    {
        "ID": "5",
        "Intent": "Skill Discovery",
        "Question_Text": "Do you enjoy learning new skills or improving the ones you already have?",
        "Follow_Up": "What motivates you to learn?",
        "Expected_Answers": ["Yes", "No"],
        "Next_Step_Yes": "6",
        "Next_Step_No": "8"
    },
    {
        "ID": "6",
        "Intent": "Value Identification",
        "Question_Text": "What’s more important to you: creativity, logic, or helping others?",
        "Follow_Up": "Why do you value this most?",
        "Expected_Answers": ["Creativity", "Logic", "Helping others"],
        "Next_Step_Yes": "7",
        "Next_Step_No": "8"
    },
    {
        "ID": "7",
        "Intent": "Goal Setting",
        "Question_Text": "Do you have any goals for your future? If yes, can you describe one?",
        "Follow_Up": "What inspired this goal?",
        "Expected_Answers": ["Yes", "No"],
        "Next_Step_Yes": "8",
        "Next_Step_No": "10"
    },
    {
        "ID": "8",
        "Intent": "Activity Preference",
        "Question_Text": "Do you prefer working on long-term projects or short, quick tasks?",
        "Follow_Up": "What do you like about that?",
        "Expected_Answers": ["Long-term projects", "Short tasks"],
        "Next_Step_Yes": "9",
        "Next_Step_No": "10"
    },
    {
        "ID": "9",
        "Intent": "Personal Reflection",
        "Question_Text": "If you could choose any job without thinking about money, what would it be?",
        "Follow_Up": "What excites you about this job?",
        "Expected_Answers": ["Free text"],
        "Next_Step_Yes": "10",
        "Next_Step_No": "10"
    },
    {
        "ID": "10",
        "Intent": "Interest Expansion",
        "Question_Text": "Would you like to explore careers related to your interests or try something completely new?",
        "Follow_Up": "What draws you to this choice?",
        "Expected_Answers": ["Related to interests", "Something new"],
        "Next_Step_Yes": "11",
        "Next_Step_No": "12"
    },
    {
        "ID": "11",
        "Intent": "Learning Style",
        "Question_Text": "How do you prefer to learn new things?",
        "Follow_Up": "What methods have worked best for you in the past?",
        "Expected_Answers": ["Reading", "Watching videos", "Hands-on experience", "Listening to others"],
        "Next_Step_Yes": "12",
        "Next_Step_No": "13"
    },
    {
        "ID": "12",
        "Intent": "Learning Style",
        "Question_Text": "Do you like working on your own or in groups?",
        "Follow_Up": "Why do you think that works best for you?",
        "Expected_Answers": ["Alone", "In groups"],
        "Next_Step_Yes": "13",
        "Next_Step_No": "14"
    },
    {
        "ID": "13",
        "Intent": "Learning Style",
        "Question_Text": "Do you prefer structured learning or more flexible, self-paced learning?",
        "Follow_Up": "Why do you prefer this approach?",
        "Expected_Answers": ["Structured", "Flexible"],
        "Next_Step_Yes": "14",
        "Next_Step_No": "15"
    },
    {
        "ID": "14",
        "Intent": "Personality",
        "Question_Text": "Do you enjoy fast-paced environments, or do you prefer working at your own pace?",
        "Follow_Up": "Why does this type of environment appeal to you?",
        "Expected_Answers": ["Fast-paced", "Steady pace", "Both"],
        "Next_Step_Yes": "15",
        "Next_Step_No": "16"
    },
    {
        "ID": "15",
        "Intent": "Personality",
        "Question_Text": "Would you describe yourself as more introverted or extroverted?",
        "Follow_Up": "How do you think this affects your work preferences?",
        "Expected_Answers": ["Introverted", "Extroverted", "Both"],
        "Next_Step_Yes": "16",
        "Next_Step_No": "17"
    },
    {
        "ID": "16",
        "Intent": "Work Environment",
        "Question_Text": "Do you thrive in a competitive or collaborative work environment?",
        "Follow_Up": "What makes this type of environment comfortable for you?",
        "Expected_Answers": ["Competitive", "Collaborative"],
        "Next_Step_Yes": "17",
        "Next_Step_No": "18"
    },
    {
        "ID": "17",
        "Intent": "Career Exploration",
        "Question_Text": "Have you explored different career paths before, or is this your first time thinking about it?",
        "Follow_Up": "What motivated you to start exploring?",
        "Expected_Answers": ["Yes", "No"],
        "Next_Step_Yes": "18",
        "Next_Step_No": "19"
    },
    {
        "ID": "18",
        "Intent": "Career Exploration",
        "Question_Text": "Are you interested in exploring careers that are in high demand or ones that allow for creativity and flexibility?",
        "Follow_Up": "Why does this option appeal to you?",
        "Expected_Answers": ["High demand", "Creative & flexible"],
        "Next_Step_Yes": "19",
        "Next_Step_No": "20"
    },
    {
        "ID": "19",
        "Intent": "Career Exploration",
        "Question_Text": "Would you prefer a job that requires formal education or one where you can learn through experience?",
        "Follow_Up": "Why do you lean toward this?",
        "Expected_Answers": ["Formal education", "Learning through experience"],
        "Next_Step_Yes": "20",
        "Next_Step_No": "21"
    },
    {
        "ID": "20",
        "Intent": "Strengths",
        "Question_Text": "What would you say is your greatest strength?",
        "Follow_Up": "Can you think of a recent example where you demonstrated this strength?",
        "Expected_Answers": ["Problem-solving", "Creativity", "Communication", "Technical skills", "Other"],
        "Next_Step_Yes": "21",
        "Next_Step_No": "22"
    },
       {
        "ID": "21",
        "Intent": "Challenges",
        "Question_Text": "What is something you find difficult or challenging in your work or studies?",
        "Follow_Up": "How do you typically overcome this?",
        "Expected_Answers": ["Time management", "Motivation", "Procrastination", "Technical difficulties", "Other"],
        "Next_Step_Yes": "22",
        "Next_Step_No": "23"
    },
    {
        "ID": "22",
        "Intent": "Challenges",
        "Question_Text": "Do you feel more motivated by a challenge or prefer more straightforward tasks?",
        "Follow_Up": "Why do you think that is?",
        "Expected_Answers": ["Challenge", "Straightforward"],
        "Next_Step_Yes": "23",
        "Next_Step_No": "24"
    },
    {
        "ID": "23",
        "Intent": "Lifestyle",
        "Question_Text": "Do you want a career that offers work-life balance or are you more focused on career growth?",
        "Follow_Up": "Why do you want this balance?",
        "Expected_Answers": ["Work-life balance", "Career growth", "Both"],
        "Next_Step_Yes": "24",
        "Next_Step_No": "25"
    },
    {
        "ID": "24",
        "Intent": "Goals",
        "Question_Text": "Do you see yourself staying in one job for a long time, or are you looking for variety?",
        "Follow_Up": "What excites you about that?",
        "Expected_Answers": ["Long-term stability", "Variety"],
        "Next_Step_Yes": "25",
        "Next_Step_No": "26"
    },
    {
        "ID": "25",
        "Intent": "Goals",
        "Question_Text": "What kind of impact do you want your work to have on the world or society?",
        "Follow_Up": "Why is this important to you?",
        "Expected_Answers": ["Positive change", "Financial success", "Personal growth", "Other"],
        "Next_Step_Yes": "26",
        "Next_Step_No": "27"
    },
    {
        "ID": "26",
        "Intent": "Values",
        "Question_Text": "Do you value financial security over job satisfaction or the other way around?",
        "Follow_Up": "Why is this important to you?",
        "Expected_Answers": ["Financial security", "Job satisfaction", "Both"],
        "Next_Step_Yes": "27",
        "Next_Step_No": "28"
    },
    {
        "ID": "27",
        "Intent": "Values",
        "Question_Text": "Would you prefer a job that aligns with your personal values and purpose or one that offers greater opportunities for success?",
        "Follow_Up": "What drives this choice?",
        "Expected_Answers": ["Personal values", "Career success"],
        "Next_Step_Yes": "28",
        "Next_Step_No": "29"
    },
    {
        "ID": "28",
        "Intent": "Purpose",
        "Question_Text": "Do you see your work as a means to an end, or do you want it to reflect your passion and purpose?",
        "Follow_Up": "How do you envision that?",
        "Expected_Answers": ["Means to an end", "Passion & purpose"],
        "Next_Step_Yes": "29",
        "Next_Step_No": "30"
    },
    {
        "ID": "29",
        "Intent": "Flexibility",
        "Question_Text": "Would you prefer a job with flexible working hours or one that is more traditional?",
        "Follow_Up": "Why does this work better for you?",
        "Expected_Answers": ["Flexible hours", "Traditional hours"],
        "Next_Step_Yes": "30",
        "Next_Step_No": "0"
    },
    {
        "ID": "30",
        "Intent": "Location",
        "Question_Text": "Do you want to work remotely, in an office, or have a mix of both?",
        "Follow_Up": "What appeals to you about this option?",
        "Expected_Answers": ["Remote", "Office", "Hybrid"],
        "Next_Step_Yes": "0",
        "Next_Step_No": "0"
    }
]