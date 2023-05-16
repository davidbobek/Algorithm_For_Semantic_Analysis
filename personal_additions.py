def personal_additions(marketing_standard, feedback_standard, job_standard, support_standard): 
    #Marketing
    marketing_standard['?'] = 30
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
    marketing_standard['limited'] = 100
    #Feedback
    feedback_standard['thank you'] = 40
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
    feedback_standard['suggestions'] = 2

    #Customer Support
    support_standard["please"] = 100
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
    job_standard['skills'] = 100000
    
    
    return marketing_standard, feedback_standard, job_standard, support_standard

"""
Hello
Thank you
Assistance
Help
Issue
Problem
Resolved
Apologize
Understand
Solution
Support
Escalate
Prompt
Response
Account
Information
Update
Appreciate
Feedback
Satisfied
"""