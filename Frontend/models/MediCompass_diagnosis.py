import os
from typing import Literal, List, Optional, Set
from datetime import date
from pydantic import BaseModel, Field, FilePath
#from streamlit_pydantic.types import FileContent



class Symptom(BaseModel):
    general_symptoms: Set[Literal["두통", "발열", "기침", "인후통", "피로", "근육통", "구토", "설사", "복통", "호흡 곤란", "콧물", "코막힘", "미각 상실", "후각 상실", "발진"]] = Field(
        description="현재 해당하는 증상을 선택해주세요.",
    )
    symptoms: str = Field(
        description='증상을 서술해주세요.',
        min_length=1,
        default="OO이 아파요"
    )
    symptom_date: int = Field(
        description='증상이 며칠 전에 발생했는지 입력해주세요.',
        default=3
    )
    general_underlying_disease: Set[Literal["고혈압", "심부전", "당뇨병", "만성 호흡기 질환", "만성 신장 질환", "치매"]] = Field(
        description="기저질환을 선택해 주세요.",
    )
    underlying_disease: str = Field(
        description='기저질환을 서술해주세요.',
        default="없음"
    )


class InputModel(BaseModel):
    

    age: int = Field(
        alias='Age',
        description='나이',
        default=20,
    )
    gender: Literal['male', 'female', 'other'] = Field(
        alias='Gender',
        description='성별',
        default='male',
    )
    symptoms: Symptom = Field(
    )
    # 이미지 처리 필요
    '''
    photos: Optional[FileContent] = Field(
        None,
        description='환부의 사진을 넣어주세요.',
        st_kwargs_type=["png", "jpg"],
    )
    '''
    llm_type: Literal['chatgpt'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    disease_name: str = Field(
        description='추정한 병명'
    )
    disease_description: str = Field(
        description='추정한 병에 대한 설명'
    )
    recommended_specialty: str = Field(
        description='추천 병원 전문 분야 (예: 이비인후과, 피부과 등)'
    )