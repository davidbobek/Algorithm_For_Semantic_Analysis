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
            text = text.lower()
            #remove /n and /t
            text = text.replace('\n', ' ')
            text = text.replace('\t', ' ')
            #list of words
            text = text.split(' ')
            #remove empty strings
            text = list(filter(None, text))

            #remove anything from this list
            filtered_words = ['Subject:','[Customer','Name]','[Your','Company]','[Company','Name],','Name]','[Customer','Name],','[Your','Company]','[Customer','Name],','[Your','Company]',"subject:",'[customer','name]','[your','company]','[company','name],','name]','[customer','name],','[your','company]','[customer','name],','[your','company]','the']

          
            for word in range(len(text)):
                
                if text[word] in filtered_words:
                    text[word] = ''
            #remove empty strings
            text = list(filter(None, text))
            
            return text
        
        for i in range(len(var_list)):
            var_list[i] = convert_to_words(var_list[i])

    return fields


        
        