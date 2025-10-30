from sqlalchemy import Column, Integer, String, Boolean, Enum as SAEnum
from sqlalchemy.orm import relationship
from .base import Base
import enum


class Sites(enum.Enum):
    INDEED = "INDEED"
    LINKEDIN = "LINKEDIN"
    ZIP_RECRUITER = "ZIP_RECRUITER"
    GOOGLE = "GOOGLE"


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    # store enum as string for SQLite/postgres portability
    site = Column(SAEnum(Sites, native_enum=False, length=50), nullable=False)
    url = Column(String, nullable=False, unique=True)
    title = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    job_type = Column(String, nullable=True)
    is_remote = Column(Boolean, default=False)
    job_level = Column(String, nullable=True)
    description = Column(String, nullable=True)

    match_score = relationship("JobMatchScore", uselist=False, back_populates="job")