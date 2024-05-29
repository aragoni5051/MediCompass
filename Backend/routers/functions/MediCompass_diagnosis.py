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
                # 환자 정보
                * 나이: {model.age}
                * 성별: {model.gender}

                # 병에 대한 정보
                * 보편적 증상들: {', '.join(model.symptoms.general_symptoms)}
                * 증상에 대한 설명: {model.symptoms.symptoms}
                * 나타난 일자: {model.symptoms.symptom_date}일전
                * 기저 질환: {model.symptoms.general_underlying_disease}
                * 기저 질환에 대한 정보: {model.symptoms.underlying_disease}
            ''',
        }).split('///')

    return OutputModel(
        disease_name=output[0],
        disease_description=output[1],
        recommended_specialty=output[2],
    )
