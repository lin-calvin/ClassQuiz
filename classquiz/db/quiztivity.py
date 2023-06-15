#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from pydantic import BaseModel
import enum


class Pdf(BaseModel):
    url: str


class _MemoryCard(BaseModel):
    image: str | None
    text: str | None
    id: str


class Memory(BaseModel):
    cards: list[list[_MemoryCard]]


class Markdown(BaseModel):
    markdown: str


class _AbcdAnswer(BaseModel):
    answer: str
    correct: bool


class Abcd(BaseModel):
    question: str
    answers: list[_AbcdAnswer]


class QuizTivityTypes(str, enum.Enum):
    SLIDE = "SLIDE"
    PDF = "PDF"
    MEMORY = "MEMORY"
    MARKDOWN = "MARKDOWN"
    ABCD = "ABCD"


TYPE_CLASS_LIST = {
    QuizTivityTypes.PDF: type(Pdf),
    QuizTivityTypes.MEMORY: type(Memory),
    QuizTivityTypes.MARKDOWN: type(Markdown),
    QuizTivityTypes.ABCD: type(Abcd),
}


class QuizTivityPage(BaseModel):
    title: str | None
    type: QuizTivityTypes
    data: Pdf | Memory | Markdown | Abcd
