def personal_additions(marketing_standard, feedback_standard, job_standard, support_standard): 
    #Marketing
    """ marketing_standard['?'] = 30
    marketing_standard['buy'] = 500
    marketing_standard['!'] = 30
    marketing_standard['exclusive'] = 1000
    marketing_standard['limited'] = 38
    marketing_standard['new'] = 36
    marketing_standard['free'] = 34
    marketing_standard['sale'] = 32
    marketing_standard['now'] = 30
    marketing_standard['special'] = 1000
    marketing_standard['offer'] = 1000
    marketing_standard['save'] = 24
    marketing_standard['discount'] = 1000
    marketing_standard['last'] = 20
    marketing_standard['chance'] = 18
    marketing_standard['hurry'] = 16
    marketing_standard['best'] = 14
    marketing_standard['amazing'] = 12
    marketing_standard['exciting'] = 10
    marketing_standard['unforgettable'] = 8
    marketing_standard['discover'] = 6
    marketing_standard['extra'] = 4
    marketing_standard['extraordinary'] = 2
    marketing_standard['announcement'] = 100
    marketing_standard['announce'] = 100
    marketing_standard['limited'] = 100 """
    #Feedback
    """  feedback_standard['thank you'] = 40
    feedback_standard['feedback'] = 100000
    feedback_standard['experience'] = 100000
    feedback_standard['quality'] = 34
    feedback_standard['service'] = 32
    feedback_standard['product'] = 30
    feedback_standard['satisfied'] = 28
    feedback_standard['dissatisfied'] = 26
    feedback_standard['improvement'] = 24
    feedback_standard['issue'] = 22
    feedback_standard['appreciate'] = 20
    feedback_standard['excellent'] = 18
    feedback_standard['recommend'] = 100000
    feedback_standard['helpful'] = 14
    feedback_standard['prompt'] = 12
    feedback_standard['responsive'] = 10
    feedback_standard['impressed'] = 8
    feedback_standard['reliable'] = 6
    feedback_standard['easy'] = 4
    feedback_standard['suggestions'] = 2 """

    #Customer Support
    """ support_standard["please"] = 100
    support_standard['help'] = 100
    support_standard['feedback'] = 40
    support_standard['thank'] = 38
    support_standard['thanks'] = 38
    support_standard['assistance'] = len(feedback_standard) /4
    support_standard['help'] = len(feedback_standard) /4
    support_standard['issue'] = len(feedback_standard) /4
    support_standard['problem'] = len(feedback_standard) /4
    support_standard['resolved'] = len(feedback_standard) /4
    support_standard['apologize'] = 26
    support_standard['understand'] = 24
    support_standard['solution'] = 22
    support_standard['support'] = len(feedback_standard) /2
    support_standard['escalate'] = 18
    support_standard['prompt'] = 16
    support_standard['response'] = 14
    support_standard['account'] = 12
    support_standard['information'] = 10
    support_standard['update'] = 8
    support_standard['appreciate'] = 6
    support_standard['satisfied'] = 2 
    
    job_standard['job'] = 100000
    job_standard['career'] = 100000
    job_standard['opportunity'] = 100000
    job_standard['opportunities'] = 100000
    job_standard['apply'] = 100000
    job_standard['position'] = 100000
    job_standard['positions'] = 100000
    job_standard['resume'] = 100000
    job_standard['interview'] = 100000
    job_standard['interviews'] = 100000
    job_standard['hiring'] = 100000
    job_standard['hired'] = 100000
    job_standard['recruiter'] = 100000
    job_standard['recruiters'] = 100000
    job_standard['recruiting'] = 100000
    job_standard['skills'] = 100000 """
    
    #job if we can spot all of these words in the email, we can assume it is a job offer
        
        
    
    return marketing_standard, feedback_standard, job_standard, support_standard

def micro_function(score,text,job_keywords):
    count = 0
    for word in job_keywords:
        if word in text:
            count += 1
            score *= 1.5
                
        

    return score

def score_bonuses(text,score,email_type):
    if email_type == "job":        
        job_keywords = ['job','career','opportunity','opportunities','apply','position','positions','resume','interview','interviews','hiring','hired','recruiter','recruiters','recruiting','skills']
        return micro_function(score,text,job_keywords)
        

    elif email_type == "marketing":
        job_keywords = ['?','buy','!','exclusive','limited','new','free','sale','now','special','offer','save','discount','last','chance','hurry','best','amazing','exciting','unforgettable','discover','extra','extraordinary','announcement','announce','limited']
        return micro_function(score,text,job_keywords)
    
    elif email_type == "feedback":
        job_keywords = ['thank','thanks','feedback','experience','quality','service','product','satisfied','dissatisfied','improvement','issue','appreciate','excellent','recommend','helpful','prompt','responsive','impressed','reliable','easy','suggestions']
        return micro_function(score,text,job_keywords)
    
    elif email_type == "customer support":
        job_keywords = ['please','help','feedback','thank','thanks','assistance','help','issue','problem','resolved','apologize','understand','solution','support','escalate','prompt','response','account','information','update','appreciate','satisfied']
        return micro_function(score,text,job_keywords)
    
    return score
    
    
        
    