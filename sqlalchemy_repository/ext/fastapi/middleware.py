from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

from ...manager import DatabaseManager


class SQLAlchemyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp, db: DatabaseManager) -> None:
        super().__init__(app)
        self.db = db

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        with self.db.session_ctx():
            response = await call_next(request)
        return response
