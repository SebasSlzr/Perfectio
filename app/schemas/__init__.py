# app/schemas/__init__.py
from .auth_schema import AuthRegister, AuthLogin, AuthUser, AuthToken
from .user_schema import User, UserCreate, UserUpdate
from .habit_schema import Habit, HabitCreate, HabitUpdate
from .diary_schema import Diary, DiaryCreate, DiaryEntry, DiaryEntryCreate
from .goal_schemas import Goal, GoalCreate, GoalUpdate
from .reminder_schema import Reminder, ReminderCreate, ReminderUpdate
from .achievement_schema import Achievement, AchievementCreate
from .asisstant_schema import IAAssistant, IAAssistantCreate, ChatRequest, ChatResponse, Message
from .goal_habit_schemas import GoalHabit, GoalHabitCreate
from .user_achievement_schemas import UserAchievement, UserAchievementCreate