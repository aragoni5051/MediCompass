import os

from fastapi import APIRouter

from llm.chat import build
from llm.store import LLMStore
from models.interview_simulator import InputModel, OutputModel

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
async def call_acrostic_generator(model: InputModel) -> OutputModel:
    # Create a LLM chain
    chain = build(
        name=NAME,
        llm=store.get(model.llm_type),
    )

    return OutputModel(
        output=chain.invoke({
            'input_context': f'''
                # About Company
                * Company Name: {model.target_company}
                * Desired Job: {model.target_job}
                * Expertisement: {model.expertisement}

                # Environments
                * Target Language: {model.language}
            ''',
        }),
    )
