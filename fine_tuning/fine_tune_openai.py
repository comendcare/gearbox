"""Fine tuning script for openai models"""
import os
import openai
openai.api_key = "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"
# response = openai.File.create(
#   file=open("../data/fine_tune.jsonl", "rb"),
#   purpose='fine-tune'
# )

# print(response)
# print(openai.File.delete(sid="file-bwUke2apOlqkhZUYbNxaj3BI"))
print(openai.File.list(limit=10))

# openai.FineTuningJob.create(training_file="file-M3U1oEY0FkbwGCUuMZU9tKnF", model="gpt-3.5-turbo")

# print(openai.FineTuningJob.cancel("ftjob-CPOaqHjG6fobJ6CgaZ3Lx5k5"))
print(openai.FineTuningJob.retrieve("ftjob-Rq2GW2KBMdPFkiddAHmXpll7"))
# print(openai.FineTuningJob.list(limit=10))
print(openai.FineTuningJob.list_events(id="ftjob-Rq2GW2KBMdPFkiddAHmXpll7", limit=10))

