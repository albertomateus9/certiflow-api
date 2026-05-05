from dataclasses import dataclass
from datetime import datetime
import hashlib

@dataclass
class StudentModel:
    id: str
    name: str
    registration_code: str

@dataclass
class AcademicEvent:
    id: str
    name: str
    workload_hours: int
    event_date: datetime

@dataclass
class CertificateEntity:
    id: str
    student_id: str
    event_id: str
    sha256_hash: str
    issue_date: datetime

    @staticmethod
    def generate_hash(student: StudentModel, event: AcademicEvent) -> str:
        """
        Gera a assinatura criptográfica baseada no aluno e no evento.
        """
        payload = f"{student.registration_code}-{event.id}"
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()
