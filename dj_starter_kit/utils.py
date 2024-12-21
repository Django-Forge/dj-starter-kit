def get_message(data: dict, success: bool, message: str) -> dict[dict, str, bool]:
    success = False
    return {"data": data, "success": success, "message": message}
