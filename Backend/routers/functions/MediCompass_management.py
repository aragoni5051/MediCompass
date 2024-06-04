import os

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.MediCompass_management import InputModel, OutputModel

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
async def call_MediCompass_management(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build(
        name=NAME,
        llm=store.get(model.llm_type),
    )

    return OutputModel(
        suggestion=chain.invoke({
            'input_context': f'''
                #특이사항: {model.management}
            ''',
        }),
    )
