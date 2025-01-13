from dataclasses import dataclass

from colorama import Back, Fore


@dataclass
class Document:
    title: str | None
    processed: bool | None


@dataclass
class Metadata:
    file: Document
    url: Document
    text: Document
    completion_time: float
    request_uuid: str


@dataclass
class TextCompletionResponse:
    body: str
    metadata: Metadata

    def __str__(self):
        attributes = "\n".join(
            f"{attr}={Fore.CYAN}{getattr(self, attr)}{Fore.RESET}"
            for attr in self.__dict__
        )
        return f"{Back.CYAN}{self.__class__.__name__}({Back.RESET}\n{attributes}\n)"


@dataclass
class OpenAIResponse:
    body: str
    prompt_tokens: int
    completion_tokens: int