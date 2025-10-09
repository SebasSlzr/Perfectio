from fastapi import APIRouter, HTTPException, status
from typing import List
from app.controllers import reminders_controller
from app.schemas.reminder_schema import ReminderCreate, ReminderUpdate, ReminderResponse

router = APIRouter(prefix="/reminders", tags=["Reminders"])

@router.get("/habits/{habit_id}/reminders", response_model=List[ReminderResponse])
def get_reminders(habit_id: int):
    reminders = reminders_controller.get_reminders_by_habit(habit_id)
    if not reminders:
        raise HTTPException(status_code=404, detail="No reminders found")
    return reminders

@router.post("/habits/{habit_id}/reminders", response_model=ReminderResponse, status_code=status.HTTP_201_CREATED)
def create_reminder(habit_id: int, data: ReminderCreate):
    return reminders_controller.create_reminder(habit_id, data)

@router.put("/{reminder_id}", response_model=ReminderResponse)
def update_reminder(reminder_id: int, data: ReminderUpdate):
    updated = reminders_controller.update_reminder(reminder_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return updated

@router.delete("/{reminder_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_reminder(reminder_id: int):
    deleted = reminders_controller.delete_reminder(reminder_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Reminder not found")
