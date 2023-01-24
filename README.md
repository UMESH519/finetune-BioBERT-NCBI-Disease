# finetune-BioBERT-NCBI-Disease
The Repository contains the code for finetuning of BioBERT on the NCBI Disease Dataset. The model has been deployed on Huggingface Spaces using Gradio

## Data
NCBI Dataset: This dataset contains the disease name and concept annotations of the NCBI disease corpus, a collection of 793 PubMed abstracts fully annotated at the mention and concept level to serve as a research resource for the biomedical natural language processing community. </br>

An example of an instance of the dataset:</br>
{
  'tokens': ['Identification', 'of', 'APC2', ',', 'a', 'homologue', 'of', 'the', 'adenomatous', 'polyposis', 'coli', 'tumour', 'suppressor', '.'],</br>
  'ner_tags': [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 0, 0],</br>
  'id': '0'</br>
  }</br>
  
Credits: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3951655/
  
  
## Training Results:
  
<img width="813" alt="Screen Shot 2023-01-23 at 7 49 59 PM" src="https://user-images.githubusercontent.com/63723023/214196585-68822037-e57c-4115-9fff-f932bcc27b2f.png">


## Demo 

![](huggingface_space.gif)

Demo Link : https://huggingface.co/spaces/Umesh/BioBERT-Named-Entity-Recognition

