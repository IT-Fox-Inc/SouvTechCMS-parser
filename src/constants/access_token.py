from datetime import datetime

from pydantic import BaseModel


class AuthToken(BaseModel):
    access_token: str
    refresh_token: str
    expires_at: datetime
