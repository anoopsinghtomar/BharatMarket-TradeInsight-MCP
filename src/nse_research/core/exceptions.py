class NSEResearchError(Exception):
    """Base exception for the application."""


class MCPConnectionError(NSEResearchError):
    """Raised when an NSE MCP endpoint cannot be reached."""


class DataValidationError(NSEResearchError):
    """Raised when a source response fails validation."""


class ToolNotFoundError(NSEResearchError):
    """Raised when a requested tool is absent from the discovered catalogue."""
