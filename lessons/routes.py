from fastapi import APIRouter, Depends, HTTPException
from core.auth import verify_api_key
from lessons.service import fetch_next_lesson
from core.config import supabase
from datetime import datetime
from progress.service import advance_skill_cursor

router = APIRouter(prefix="/lessons", dependencies=[Depends(verify_api_key)])

@router.get("/next")
def next_lesson(user_id: str, skill: str):
    lesson = fetch_next_lesson(user_id, skill)
    if not lesson:
        return {"status": "done"}
    return lesson


@router.post("/complete")
def complete_lesson(payload: dict):
    user_id = payload["user_id"]
    lesson_id = payload["lesson_id"]

    lesson = supabase.table("lessons") \
        .select("skill, sequence, xp") \
        .eq("id", lesson_id) \
        .single() \
        .execute()

    supabase.table("user_progress").upsert({
        "user_id": user_id,
        "lesson_id": lesson_id,
        "status": "completed",
        "xp_earned": lesson.data["xp"],
        "completed_at": datetime.utcnow().isoformat()
    }).execute()

    advance_skill_cursor(
        user_id,
        lesson.data["skill"],
        lesson.data["sequence"] + 1
    )

    return {"status": "ok", "xp": lesson.data["xp"]}
