from typing import Literal, List, Optional, Set
from datetime import date
from pydantic import BaseModel, Field, FilePath
#import streamlit as st
#from enum import Enum


class InputModel(BaseModel):

    management: str = Field(
        description="사후 관리를 위한 질문을 입력해 주세요.",
        default="감기에 걸렸습니다",
    )
    llm_type: Literal['chatgpt'] = Field(
        alias='Large Language Model Type',
        description='사용할 LLM 종류',
        default='chatgpt',
    )


class OutputModel(BaseModel):
    suggestion: str = Field(
        description='사후 관리를 위한 추천'
    )
