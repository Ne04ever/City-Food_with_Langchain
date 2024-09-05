from cohere_key import key
import os
os.environ['COHERE_API_KEY'] = key
from langchain.llms import Cohere
from langchain.chains import SequentialChain

llm_model = Cohere(max_tokens=256, temperature=0.75)
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate



def generate_city_food(place):
    template_prompt_name = PromptTemplate(
    input_variables=['place'], 
    template="name one city from {place}. give the name only"
)
    chain_name = LLMChain(llm=llm_model, prompt=template_prompt_name,output_key='city')

    template_prompt_item = PromptTemplate(
    input_variables=['city'], 
    template="Suggest me 5 foods from {city}. Return as a comma-separated list, with no numbering or additional text."
)
    chain_item = LLMChain(llm=llm_model, prompt=template_prompt_item,output_key='city_itme')



    chain = SequentialChain(chains=[chain_name,chain_item],
                       input_variables=['place'],
                       output_variables= ['city','city_itme'])

    response = chain.invoke({'place':place})
    return response


