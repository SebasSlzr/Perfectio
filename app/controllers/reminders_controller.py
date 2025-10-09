from typing import List, Optional
from app.schemas.reminder_schema import ReminderCreate, ReminderUpdate, ReminderResponse

_reminders: List[ReminderResponse] = []
_next_id = 1

def get_reminders_by_habit(habit_id: int) -> List[ReminderResponse]:
    return [r for r in _reminders if r.habit_id == habit_id]

def get_reminder(reminder_id: int) -> Optional[ReminderResponse]:
    for r in _reminders:
        if r.id == reminder_id:
            return r
    return None

def create_reminder(habit_id: int, data: ReminderCreate) -> ReminderResponse:
    global _next_id
    reminder = ReminderResponse(
        id=_next_id,
        habit_id=habit_id,
        title=data.title,
        description=data.description,
        date=data.date,
        shouldRepeat=data.shouldRepeat
    )
    _reminders.append(reminder)
    _next_id += 1
    return reminder

def update_reminder(reminder_id: int, data: ReminderUpdate) -> Optional[ReminderResponse]:
    reminder = get_reminder(reminder_id)
    if reminder is None:
        return None
    if data.title is not None:
        reminder.title = data.title
    if data.description is not None:
        reminder.description = data.description
    if data.date is not None:
        reminder.date = data.date
    if data.shouldRepeat is not None:
        reminder.shouldRepeat = data.shouldRepeat
    return reminder

def delete_reminder(reminder_id: int) -> bool:
    global _reminders
    original_len = len(_reminders)
    _reminders = [r for r in _reminders if r.id != reminder_id]
    return len(_reminders) < original_len
