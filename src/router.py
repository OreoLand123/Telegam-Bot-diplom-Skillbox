from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from start_dialog.dialog import start_dialog
from main_dialog.dialog import main_dialog
from result_dialog.dialog import result_dialog
from start_dialog.state import StartDialog
from help_dialog.dialog import help_dialog
from history_dialog.dialog import history_dialog
from model import session, User

router = Router()
router.include_routers(start_dialog, main_dialog, result_dialog, help_dialog, history_dialog)


@router.message(Command("start"))
async def start(message: Message, dialog_manager: DialogManager):
    user_data = User(tg_id=message.from_user.id)
    if not session.query(User).where(User.tg_id == message.from_user.id).all()  :
        session.add(user_data)
        session.commit()
        session.flush()
    await dialog_manager.start(StartDialog.main, mode=StartMode.RESET_STACK)