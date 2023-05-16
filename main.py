from data_processing import process
from personal_additions import personal_additions
import matplotlib.pyplot as plt
marketing_mails_list = []   
feeback_mails_list = []
job_mails_list = [] 
customer_support_mails_list = []

fields = {'marketing': marketing_mails_list, 'feedback': feeback_mails_list, 'job': job_mails_list, 'customer_support': customer_support_mails_list}



data = process(fields)

marketing_emails = data['marketing']    
feedback_emails = data['feedback']
job_emails = data['job']
customer_support_emails = data['customer_support']


#count occurences of words in each list and store in a dictionary
def count_words(email_type: list) -> dict:
    word_counts = {}    
    for email in email_type:
        for word in email:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts

marketing_word_counts = count_words(marketing_emails)
feedback_word_counts = count_words(feedback_emails)
job_word_counts = count_words(job_emails)
customer_support_word_counts = count_words(customer_support_emails)

#sort the dictionary by value
def sort_dict(dictionary: dict) -> list:
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_dict

sorted_marketing_word_counts = sort_dict(marketing_word_counts)
sorted_feedback_word_counts = sort_dict(feedback_word_counts)
sorted_job_word_counts = sort_dict(job_word_counts)
sorted_customer_support_word_counts = sort_dict(customer_support_word_counts)

#plot the top 25 words in each list
def plot_top_25(sorted_dict:dict, email_type:str) -> None:
    x = []
    y = []
    final_dict = {}
    selected = 0
    if len(sorted_dict) < 25:
        selected = len(sorted_dict)
    else:
        selected = 25
    for i in range(selected):
        x.append(sorted_dict[i][0])
        y.append(sorted_dict[i][1])
        final_dict[sorted_dict[i][0]] = sorted_dict[i][1]
    plt.bar(x, y)
    plt.title('Top 25 words in ' + email_type + ' emails')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()
    return final_dict

marketing_standard = plot_top_25(sorted_marketing_word_counts, 'marketing')
feedback_standard = plot_top_25(sorted_feedback_word_counts, 'feedback')
job_standard = plot_top_25(sorted_job_word_counts, 'job')
support_standard = plot_top_25(sorted_customer_support_word_counts, 'customer support')

#Personal additions
#marketing_standard, feedback_standard, job_standard, support_standard = personal_additions(marketing_standard, feedback_standard, job_standard, support_standard)



user_input = input('Enter your email: ')
user_input = user_input.lower()
user_input = user_input.split()

#compare the user input to the top 25 words in each list
def compare(user_input:list, standard:dict,email_type:str) -> int:
    score = 0
    for word in user_input:
        if word in standard:
            score += standard[word]
    return score

results = []
for standard in [marketing_standard, feedback_standard, support_standard,job_standard ]:
    email_type = ''
    if standard == marketing_standard:
        email_type = 'marketing'
    elif standard == feedback_standard:
        email_type = 'feedback'
    elif standard == job_standard:
        email_type = 'job'
    elif standard == support_standard:
        email_type = 'customer support'
    score = compare(user_input, standard, email_type)
    results.append((email_type, score))
print(results)
print('Your email is most similar to the ' + max(results, key=lambda x: x[1])[0] + ' emails.')

#Insights:
#The top 25 words in the marketing emails are mostly words that are used to describe the product or service being marketed.

#The top 25 words in the feedback email are mostly words reflecting our customers' satisfaction with our product or service.

#The top 25 words in the job emails are mostly words that are used to describe the job being offered.

#The top 25 words in the customer support emails are mostly words that are used to describe the problem the customer is having with our product or service.

#Try it out:
#Marketing email

"""
Sales Industry Application Subject: Results-Driven Sales Professional Seeking New Challenges Dear [Hiring Manager's Name], I hope this email finds you well. I am writing to express my keen interest in joining your sales team at [Company Name]. With a proven track record of exceeding sales targets and building strong client relationships, I am confident in my ability to drive revenue growth and contribute to your company's success. Please find attached my resume, which highlights my sales achievements and demonstrates my expertise in consultative selling and negotiation. I would greatly appreciate the opportunity to discuss how my skills align with your organization's sales objectives. Thank you for considering my application. Warm regards, [Your Name] [Your Contact Information] Feel free to tailor this template to suit your specific industry or job application. Good luck with your job search!
"""

#Feedback email
"""
I hope this email finds you well. I wanted to take a moment to express my sincere appreciation for the exceptional service you provided during my recent experience with your company. From the moment I engaged with your team, I was impressed by the level of professionalism and attentiveness I received. Your knowledge and expertise were evident, and you went above and beyond to address all my inquiries and concerns. Your dedication to ensuring a positive customer experience truly stood out. Not only did you meet my expectations, but you also exceeded them in every aspect. Your prompt response time, clear communication, and willingness to go the extra mile made a significant impact on my overall satisfaction. It is evident that you take great pride in your work, and your commitment to excellence is highly commendable. I believe that exceptional service should be acknowledged, and I wanted to express my gratitude for the outstanding support you provided. You truly made a positive difference in my experience, and I wanted to let you know that your efforts did not go unnoticed. Once again, thank you for your exemplary service. Your dedication to customer satisfaction sets a remarkable standard, and I will not hesitate to recommend your company to others based on the exceptional experience I had. Wishing you continued success and satisfaction in your work. Warm regards,
"""