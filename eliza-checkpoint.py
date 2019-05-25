
# coding: utf-8

# In[1]:


#Meena Rapaka(G01101759), Siva Naga Lakshmi Karamsetty (G01099587), Ying Ke(G01000082)

#The program designed below is Eliza, it is a basic chatbot which will respond to user,from a predefined set
#of instructions.
#The program starts by asking the user's name, which we will feed as input then you start interacting with eliza.
#Eliza would answer to your questions, based on predefined set of instructions.
#For bonus point, we included the timer function from the below paper.
# https://www.csee.umbc.edu/courses/331/papers/eliza.html

#example: 
#a.word spotting: if you pass input "i want to die", eliza will respond " Are you sure, whay you want to die?".
#b.sentence transformation:"I feel happy", eliza will respond "Why do you feel happy" or "Do you really feel 
#happy" 
#C.pattern matching: if you type sorry, it will match the response_dialog from sorry and return to user.

#Algorithm of Eliza
#step-1: Accept a input as string
#step-2: Analyze the string to obtain a pattern
#step-3: returns a response after a pattern match
#step-4: return the response in the form of a string
#step-5: lopp iterates untill we quit/bye.


#imports the packages re for regurlar expression, random for generating random response and timer for the class to 
# run after a certain amount of time
import re
import random
from threading import Timer


# List of patterns and corresponding responses.
Response_Dialog = [
    [r'[I|i] need (.*)',
     ["Why do you need {0}?",
      "Would it really help you to get {0}?",
      "Are you sure you need {0}?"
     ]],
    
    [r'[I|i] feel(.*)',
     ['Why do you feel {0}?',
      'Do you really feel {0}?',
      'I do not understand what you feel{0}?',
      "Do you believe it is normal to feel like that?"
     ]],

 
    [r'[W|w]hy don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Do you really want me to {0}?"
     ]],
 
    [r'[W|w]hy can\'?t [I|i] ([^\?]*)\??',
     ["Do you think you should be able to {0}?",
      "If you could {0}, what would you do?",
      "I don't know -- why can't you {0}?",
      "Have you really tried?"]],
 
    [r'[I|i] can\'?t (.*)',
     ["How do you know you can't {0}?",
      "Perhaps you could {0} if you tried.",
      "What would it take for you to {0}?"
     ]],
      
    [r'Can you (.*)',
     ["Could you do me a favor?",
      "Can you be able to {0}?"
     ]],

 
    [r'[I|i] am (.*)',
     ["Did you come to me because you are {0}?",
      "How long have you been {0}?",
      "How do you feel about being {0}?"
     ]],
 
    [r'[I|i]\'?m (.*)',
     ["How does being {0} make you feel?",
      "Do you enjoy being {0}?",
      "Why do you think you're {0}?"
     ]],
 
    [r'[A|a]re you ([^\?]*)\??',
     ["Why does it matter whether I am {0}?",
      "I may be {0} -- what do you think?"
     ]],
 
    [r'[W|w]hat (.*)',
     ["Why do you ask?",
      "What do you think?"
     ]],
 
    [r'[H|h]ow (.*)',
     ["How was your day?",
      "Perhaps you can answer your own question.",
      "What is it you're really asking?",
      "You look bad, Dint you get enough sleep?"
     ]],
 
    [r'[B|b]ecause (.*)',
     ["Is the reason real?",
      "Is this reason valid",
      "What other reasons come to mind?",
      "Does that reason apply to anything else?",
      "If {0}, what else must be true?"
     ]],
 
    [r'(.*) sorry (.*)',
     ["There is no need for a apology ",
      "What are you feeling sorry about?"
     ]],
 
    [r'[I|i] think (.*)',
     ["Do you doubt {0}?",
      "Do you really think so?",
       "What is the reason that you think {0}?"
     ]],
 
    [r'(.*) friend (.*)',
     ["Tell me more about your friends.",
      "When you think of a friend, what comes to mind?",
      "Why don't you tell me about a childhood friend?"
     ]],
 
    [r'[Y|y]es',
     ["You seem quite sure.",
      "OK, but can you elaborate about it?"
     ]],
 
    [r'(.*) computer(.*)',
     ["Are you really talking about me?",
      "Does it seem strange to talk to a computer?",
      "Do you feel threatened by computers?"
     ]],
 
    [r'[I|i]s it (.*)',
     ["Do you think it is {0}?",
      "Perhaps it's {0} -- what do you think?",
      "If it were {0}, what would you do?",
      "It could well be that {0}."
     ]],
 
    [r'[I|i]t is (.*)',
     ["You seem very certain.",
      "If I told you that it probably isn't {0}, what would you feel?"
     ]],
 
    [r'[C|c]an you ([^\?]*)\??',
     ["What makes you think I can't {0}?",
      "If I could {0}, then what?",
      "Why do you ask if I can {0}?"
     ]],
 
    [r'[Y|y]ou are (.*)',
     ["Why do you think I am {0}?",
      "Does it please you to think that I'm {0}?",
      "Perhaps you would like me to be {0}.",
      "Perhaps you're really talking about yourself?"
     ]],
 
    [r'[Y|y]ou\'?re (.*)',
     ["Why do you say I am {0}?",
      "Why do you think I am {0}?",
      "Are we talking about you, or me?"]],
 
    [r'[I|i] don\'?t (.*)',
     ["Don't you really {0}?",
      "Why don't you {0}?"
      ]],
 
    [r'[I|i] have (.*)',
     ["What do you think about having {0}",
      "{0},a lot of people are having it."
    ]],
 
    [r'[I|i]s there (.*)',
     ["I am not sure about {0}",
      "What is your opinion ?"
    ]],
    
    [r'[Y|y]ou (.*)',
     ["We should talk about you,not me.",
      "Why do you say that about me?",
      "Why are you interested in {0}?",
      "Why do you care whether I {0}?"
     ]],
 
    [r'[W|w]hy (.*)',
     ["Oh! Why do you think {0}?",
      "Why don’t you tell me the reason {0}?"
      ]],
 
    [r'[I|i] want (.*)',
     ["How much does it mean to you if you got {0}?",
      "are you sure, Why do you want {0}?"
    ]],
    
    [r'[q|Q]uit',
     ["Thank you for talking to me",
      "Good-bye, Have a nice day!",
      "See you soon, It was pleasure talking to you."
    ]],
 
    [r'(.*)',
     ["Hmm...lets talk about you..So, Tell me more about yourself.",
      "Pardon me, shall we talk about you?",
      "Let us discuss more about it.",
      "Come, come, elucidate your thoughts.",
      "Why do you say that?",
      "I see.",
      "Interesting!",
      "How does that make you feel?",
      "Why do you feel so?"
     ]],
    
    ]
#Defining a dictionary which reflection characters to their corresponding values.

Reflections = {
  "am"   : "are",
  "was"  : "were",
  "i"    : "you",
  "i'd"  : "you would",
  "i've"  : "you have",
  "i'll"  : "you will",
  "my"  : "your",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "yours"  : "mine",
  "you"  : "me",
  "me"  : "you",
  "I will"  : "you will"
}









# In[2]:


# Defining the function reflect(), which will accept input and matches its responses with reflections().
def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in Reflections:
            tokens[i] = Reflections[token]
    return ' '.join(tokens)


# In[3]:


# Definfing the function Response(), which matches the input string with pattern/regex with response_dialog.
def Response(statement):
    for pattern, responses in Response_Dialog:
        match = re.match(pattern, statement.rstrip(".!"))
        
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])


# In[4]:


# Defining the fuction input_name(), which will check whether the user is still hanging around the chatter bot.

def input_name():
        timeout = 10 # Returns the response, if the user is inactive for 10 seconds.
        t = Timer(timeout, print, ['Waiting for Your response.........'] )
        t.start()
        name = input()
        t.cancel()
        return name
    


# In[5]:


# Defining the fuction input_statement(),which will check whether the user is still hanging around when you are 
#halfway through the conversation.

def input_statement():
    timeout = 15# Returns the response, if the user is inactive for 15 seconds.
    t = Timer(timeout, print, ['Knock, Knock.....are you still there?'])
    t.start()
    statement = input()
    t.cancel()
    return statement


# In[6]:


#Definig the main function

def main():
    print('Therapist\n------')
    print('Talk to the program by typing in plain English, using normal upper-')
    print('and lower-case letters and punctuation.Enter "bye" when done.')
    print('='*72)
    print('\n')
    print("Hey,I am Eliza.May I know your name please?")
    name=input_name()# input is passed as string.(just pass name as input)
    
    logic=re.match(r"([A-Za-z]+\s[A-Za-z].)|([A-Za-z]+)",name) #checks whether the passed input string matches with 
    #given regular expression.


    if(logic==None):
        logic=False
    else:
        logic=True
    

   #the below while loop will run if the user input is numbers, alphanumerics or any white spaces. 
    while ( logic == False):  
        if name.isnumeric():
            print ( 'Numbers are for Robots!!....Can you please tell your name?')
            
        elif(name==' ' or name ==''): 
            print ( 'So Shall i address you as Mr/Ms Silent ?\n Lets start again....what is your name?')
        #if we just pass the blank input, the above response is generated.
        else:
            print("Oops that didn't sound correct,Can you please tell your name again?")
        name=input()

        
       #checks whether the passed input string matches with 
       #given regular expression. 
        logic=re.match(r"([A-Za-z]+\s[A-Za-z].)|([A-Za-z]+)",name)
        
        if(logic==None):
            logic=False
        else:
            logic=True
        
        
# this loop will run as long as true exists.
    while ( logic==True):
        print ('Hello ' + name + ', Please tell me what’s been bothering you.')
        break

        
        
    while True:
        
        statement=input_statement()
        if statement.lower()== "bye":#if the user ends conversation with 'bye' the below string is passed.
            print('It was nice talking to you.Good Bye')
            break
        else:
            print(Response(statement))
 

if __name__ == "__main__":
    main()
    
    #end

