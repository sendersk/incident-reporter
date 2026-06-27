from pydantic import BaseModel


class ApiConfig(BaseModel):
    url: str


class StorageConfig(BaseModel):
    file: str


class ReportConfig(BaseModel):
    markdown: str
    html: str


class AppConfig(BaseModel):
    api: ApiConfig
    storage: StorageConfig
    reports: ReportConfig