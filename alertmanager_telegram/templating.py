from flask import render_template
from telegram.constants import MAX_MESSAGE_LENGTH

from alertmanager_telegram.logging import logger


def render(content):
    message = render_template("default.html", **content)
    while len(message) > MAX_MESSAGE_LENGTH and len(content["alerts"]) > 0:
        logger.debug("Truncating alerts list (with ellipsis)")
        content["alerts"].pop()
        content["ellipsis"] = True
        message = render_template("default.html", **content)

    if len(message) > MAX_MESSAGE_LENGTH:
        msg = "Message template is too long"
        logger.error(msg)
        return msg

    return message
