import os

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.MediCompass import InputModel, OutputModel

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
async def call_MediCompass(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build(
        name=NAME,
        llm=store.get(model.llm_type),
    )

    return OutputModel(
        output=chain.invoke({
            'input_context': f'''
                # About patient
                * Age: {model.age}
                * Gender: {model.gender}
                * Location: {model.location}

                # About Sickness
                * Symptoms: {model.symptoms}
                * Ohotos on sickness: {model.photo_url}
            ''',
        }),
    )
