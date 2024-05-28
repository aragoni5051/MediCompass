import os

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.MediCompass_diagnosis import InputModel, OutputModel

# Configure API router
router = APIRouter(
    tags=['functions'],
)

# Configure metadata
NAME = os.path.basename(__file__)[:-3]

# Configure resources
store = LLMStore()

###############################################
#                   Actions                   #
###############################################

@router.post(f'/func/{NAME}')
async def call_MediCompass_diagnosis(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build(
        name=NAME,
        llm=store.get(model.llm_type),
    )

    

    output=chain.invoke({
            'input_context': f'''
                # About patient
                * Age: {model.age}
                * Gender: {model.gender}

                # About Symptoms
                * General Symptoms: {', '.join(model.symptoms.general_symptoms)}
                * Symptoms: {model.symptoms.symptoms}
                * When it began: {model.symptoms.symptom_date}
                * General underlying disease: {model.symptoms.general_underlying_disease}
                * Informations about the underlying disease: {model.symptoms.underlying_disease}
            ''',
        }).split('///')

    return OutputModel(
        disease_name=output[0],
        disease_description=output[1],
        recommended_specialty=output[2],
    )
