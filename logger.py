import json
from datetime import datetime
from decimal import Decimal
from typing import Any
import pendulum

from aiologger.formatters.json import (
    FILE_PATH_FIELDNAME,
    FUNCTION_NAME_FIELDNAME,
    LINE_NUMBER_FIELDNAME,
    LOGGED_AT_FIELDNAME,
    JsonFormatter,
)
from aiologger.loggers.json import JsonLogger
from pydantic import BaseModel


class ExtendedJSONEncoder(json.JSONEncoder):
    """JSON encoder for complex Python types."""

    def default(self, obj: Any) -> Any:
        if isinstance(obj, (datetime, pendulum.DateTime)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return str(obj)
        if isinstance(obj, BaseModel):
            return obj.model_dump()
        if isinstance(obj, set):
            return list(obj)
        if hasattr(obj, "to_dict"):
            return obj.to_dict()
        try:
            return super().default(obj)
        except TypeError:
            return str(obj)


class EnhancedJsonFormatter(JsonFormatter):
    """Formats log records into enriched JSON structure."""

    def __init__(self, *args: Any, pretty_print: bool = False, **kwargs: Any) -> None:
        self.pretty_print = pretty_print
        super().__init__(*args, **kwargs)

    def _process_log_record(self, record: Any) -> dict:
        base_msg = {
            "logged_at": pendulum.now("Asia/Kolkata").isoformat(),
            "level": record.levelname,
            "message": record.msg,
            "function_name": record.funcName,
            "file_path": record.pathname,
            "line_number": record.lineno,
        }

        if hasattr(record, "extra"):
            try:
                processed_extra = json.loads(
                    json.dumps(record.extra, cls=ExtendedJSONEncoder)
                )
                base_msg.update(processed_extra)
            except Exception as e:
                base_msg.update({
                    "extra_serialization_error": str(e),
                    "extra_raw": str(record.extra),
                })

        return base_msg

    def format(self, record: Any) -> str:
        try:
            record.msg = self._process_log_record(record)
            formatted = super().format(record)

            if self.pretty_print:
                return json.dumps(
                    json.loads(formatted),
                    indent=2,
                    ensure_ascii=False,
                    cls=ExtendedJSONEncoder,
                )
            return json.dumps(json.loads(formatted), cls=ExtendedJSONEncoder)
        except Exception as e:
            return json.dumps({
                "logged_at": pendulum.now("Asia/Kolkata").isoformat(),
                "level": "ERROR",
                "message": f"Logging error: {str(e)}",
                "original_message": str(record.msg),
            })


def get_logger(name: str = "backend_logger", level: str = "DEBUG", pretty_print: bool = False) -> JsonLogger:
    logger = JsonLogger.with_default_handlers(
        name=name,
        level=level,
        flatten=True,
        exclude_fields=[
            LINE_NUMBER_FIELDNAME,
            FUNCTION_NAME_FIELDNAME,
            FILE_PATH_FIELDNAME,
            LOGGED_AT_FIELDNAME,
        ]
    )

    console_handler = logger.handlers[0] 
    console_handler.formatter = EnhancedJsonFormatter(pretty_print=pretty_print)

    return logger



logger = get_logger(pretty_print=False)
