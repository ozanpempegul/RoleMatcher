from sqlalchemy import Column, Integer, String, Boolean, Enum
from .base import Base
import enum


class Sites(enum.IntEnum):
    INDEED = 0
    LINKEDIN = 1
    ZIP_RECRUITER = 2
    GOOGLE = 3


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    site = Column(Enum(Sites), nullable=False)
    url = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    job_type = Column(String, nullable=True)
    is_remote = Column(Boolean, default=False)
    job_level = Column(String, nullable=True)
    description = Column(String, nullable=True)
