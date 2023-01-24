import gradio as gr
from transformers import pipeline


model_checkpoint ="Umesh/biobert-finetuned-ncbi"
token_classifier = pipeline("token-classification", model=model_checkpoint, aggregation_strategy="simple")

def inference(text):
    output = token_classifier(text)
    for i in output:
      i['entity'] = i['entity_group']
      del i['entity_group']
    return {"text": text, "entities": output} 


examples = [
    ["Anyone can develop GBS, but people older than 50 are at greatest risk. About two-thirds of people with GBS were sick with diarrhea or respiratory illness days or weeks before developing symptoms"],
    ['COVID-19 is caused by a coronavirus called SARS-CoV-2. Older adults and people who have severe underlying medical conditions like heart or lung disease or diabetes seem to be at higher risk for developing more serious complications from COVID-19 illness.'],
    ["Headache, flushing, and upset stomach are common Viagra side effects. These effects are usually mild and often resolve on their own."],
    ['Sildenafil is also used in both men and women to treat the symptoms of pulmonary arterial hypertension. This is a type of high blood pressure that occurs between the heart and the lungs. ']
]


demo = gr.Interface(inference,
             gr.Textbox(placeholder="Enter sentence here..."), 
             gr.HighlightedText(),
             examples=examples,
             allow_flagging = False,
             title="Named Entity Recognition for Disease",
             description="The Demo uses BioBERT finetuned on NCBI Dataset and can be used to detect the name of diseases appearing in the given text")

demo.launch()