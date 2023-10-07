import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.File.create(
  file=open("mydata.jsonl", "rb"),
  purpose='fine-tune'
)

openai.FineTuningJob.create(training_file="intralingual-fine-tune", model="gpt-3.5-turbo")
