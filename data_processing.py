#Gather text from the marketing emails and store them in a list
def process(fields: dict) -> dict:
    for field,var_list in fields.items():
        with open(field+'_email.txt', 'r') as f:
            #split the text into a list of emails by the delimiter 'Email X:'
            for email in f.read().split('Email '):
                var_list.append(email[3:])
                
            var_list.pop(0)
 


        #Convert formatted text into a list of words and get rid of /n and /t and other special characters 
        def convert_to_words(text: str) -> list:
        
            #remove /n and /t
            text = text.replace('\n', ' ')
            text = text.replace('\t', ' ')
            #list of words
            text = text.split(' ')
            #remove empty strings
            text = list(filter(None, text))

            return text
        
        for i in range(len(var_list)):
            var_list[i] = convert_to_words(var_list[i])

    return fields


        
        