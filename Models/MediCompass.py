from typing import List, Literal
from pydantic import BaseModel, Field, FilePath
from datetime import date


class Symptom(BaseModel):
    description: str = Field(
        description='증상에 대한 서술을 입력해주세요.',
        min_length=1,
    )
    symptom_date: date = Field(
        description='증상이 발생한 날짜를 입력해주세요.',
    )


class InputModel(BaseModel):
    age: int = Field(
        description='환자의 나이를 입력해주세요.',
    )
    gender: Literal['male', 'female', 'other'] = Field(
        description='환자의 성별을 입력해주세요. (male, female, other 중 하나)',
    )
    symptoms: List[Symptom] = Field(
        description='환자의 증상을 입력해주세요. 여러 증상이 있을 경우 리스트로 입력해주세요.',
    )
    photo_urls: List[FilePath] = Field(
        description='환부의 사진 파일 경로를 입력해주세요',
    )
    location: str = Field(
        description='환자의 위치 정보를 입력해주세요.',
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
    nearby_hospitals: List[str] = Field(
        description='주변 병원 리스트'
    )