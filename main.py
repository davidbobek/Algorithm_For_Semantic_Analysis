from data_processing import process
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

#plot the top 10 words in each list
def plot_top_10(sorted_dict:dict, email_type:str) -> None:
    x = []
    y = []
    selected = 0
    if len(sorted_dict) < 15:
        selected = len(sorted_dict)
    else:
        selected = 15
    for i in range(selected):
        x.append(sorted_dict[i][0])
        y.append(sorted_dict[i][1])
    plt.bar(x, y)
    plt.title('Top 10 words in ' + email_type + ' emails')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.show()

plot_top_10(sorted_marketing_word_counts, 'marketing')
plot_top_10(sorted_feedback_word_counts, 'feedback')
plot_top_10(sorted_job_word_counts, 'job')
plot_top_10(sorted_customer_support_word_counts, 'customer support')


