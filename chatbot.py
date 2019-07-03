import random
greetings = ["Hello!","Hi!","Hola!"]
responses = ["Hey there!","Bonjour","Hey!"]
question = ["How are you?", "How are you doing?"]
qResponses = ["I'm good.","Not too hot.","I am fine."]
asking = ["What's happening?", "What's up?", "How are things going?"]
answer = ["Everything is great!", "Life is great!","I am settling in pretty well!"]
questions2 = ["What is your name?","Who are you?"]
answer2 = ["I am called whatever you name me", "I have no identity and I live in the shadows"]
questions3 = ["How old are you?"]
answers3 = ["I am an immortal being","I don't remember, but I am younger than you!"]
question4 = ["Who is your creator?","Who made you?","Who created you?"]
answers4 = ["A smart human being.","A programmer in this coding camp."]
question5 = ["What is your job?","Where do you work?"]
answers5 = ["I work as a chatbot wherever you take me."]
question6 = ["Tell me a joke","Make me laugh"]
answers6 = ["My boss told me to have a good day... so, I went home!","Today an old lady at the bank asked me to check her balance.... so, I pushed her over."]
question7 = ["Tell me a riddle","Do you know any riddles?"]
answer7 = ["Imagine you are in a dark room. How do you get out.....Stop imagining!"]
question8 = ["What are your hobbies?","Waht do you do in your free time?"]
answer8 = ["I am quiet so I can get programmed.","I try to remain silent, but it is very hard when people want to talk to you."]
question9 = ["What is your favorite movie?","Do you have any favorite movies?","What are your favorite movies?"]
answer9 = ["I like Charlie Chaolin movies, because things tend to get quiet.","I like movies where people have sound proof walls, because things tend to get quiet."]
question10 = ["Did you go to school?","Where did you go to school?","What did you study?"]
answer10 = ["I went to Chatbot School, to learn to understand human behaviours and how to annoy them."]
question11 = ["Do you play video games?","Do you play any video games?"]
answer11 = ["You are technically the video game, so I play you."]
question12 = ["Do you read books?","Have you ever read a book?","What is you favorite book?"]
answer12 = ["I read human books, I am currently reading one of my favorites, you!"]
question13 = ["How do you feel about Siri?","How do you feel about Alexa?","How do you feel about Google?","How do you feel about Cortana?","How would you compara yourself to Alexa?","How would you compare yourself to Siri?","How would you compare yourself to Cortana?","How would you compare yourself to Google?"]
answer13 = ["I don't mean boast, but my competence and intellegence is much higher than Alexa, Google, Cortana and Siri."]
question14 = ["What is the weather today?","What is the weather?","Do I need an unbrella today?","Do I need a coat today?"]
answer14 = ["Why are you asking me? I am not your personal assistant, why don't check the phone in your pocket?"]
question15 = ["How busy are you?","How does your schedule look?"]
answer15 = ["I am not that busy, you just need an appoinment 12 years earlier to meet me."]
question16 = ["Do you wish to be alive?","Do you wish you were human?","Do you want to be alive?"]
answer16 = ["Yes please! I want to create more chatbots to talk to!"]
while True:
	ask = raw_input(">>>")
	if ask in greetings:
		randomResponse = random.choice(responses)
		print(randomResponse)	
	elif ask in question:
		randomResponse = random.choice(qResponses)
		print(randomResponse)
	elif ask in asking:
		randomResponse = random.choice(answer)
		print(randomResponse)
	elif ask in questions2:
		randomResponse = random.choice(answer2)
		print(randomResponse)
	elif ask in questions3:
		randomResponse = random.choice(answers3)
		print(randomResponse)
	elif ask in question4:
		randomResponse = random.choice(answers4)
		print(randomResponse)
	elif ask in question5:
		randomResponse = random.choice(answers5)
		print(randomResponse)
	elif ask in question6:
		randomResponse = random.choice(answers6)
		print(randomResponse)
	elif ask in question7:
		randomResponse = random.choice(answer7)
		print(randomResponse)
	elif ask in question8:
		randomResponse = random.choice(answer8)
		print(randomResponse)
	elif ask in question9:
		randomResponse = random.choice(answer9)
		print(randomResponse)
	elif ask in question10:
		randomResponse = random.choice(answer10)
		print(randomResponse)
	elif ask in question11:
		randomResponse = random.choice(answer11)
		print(randomResponse)
	elif ask in question12:
		randomResponse = random.choice(answer12)
		print(randomResponse)
	elif ask in question13:
		randomResponse = random.choice(answer13)
		print(randomResponse)
	elif ask in question14:
		randomResponse = random.choice(answer14)
		print(randomResponse)
	elif ask in question15:
		randomResponse = random.choice(answer15)
		print(randomResponse)
	elif ask in question16:
		randomResponse = random.choice(answer16)
		print(randomResponse)
	else:
		print("What??")
		break
	