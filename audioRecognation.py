from transformers import pipeline 

classifier=pipeline("sentiment-analysis")

res=classifier('I am using right now hugging face and it is not working for me')

print(res)

