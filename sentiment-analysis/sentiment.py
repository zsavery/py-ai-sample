import transformers

def sentiment_analysis(text=None):
    sentiment_pipeline = transformers.pipeline(task="text-classification")
    if text:
        print(sentiment_pipeline(text))
        return

    print(sentiment_pipeline(input("Enter prompt: ")))
    