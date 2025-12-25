from datetime import datetime
from core.config import supabase

def get_or_create_skill_cursor(user_id: str, skill: str) -> int:
    res = supabase.table("user_skill_progress") \
        .select("current_sequence") \
        .eq("user_id", user_id) \
        .eq("skill", skill) \
        .execute()

    if res.data:
        return res.data[0]["current_sequence"]

    supabase.table("user_skill_progress").insert({
        "user_id": user_id,
        "skill": skill,
        "current_sequence": 1
    }).execute()

    return 1


def advance_skill_cursor(user_id: str, skill: str, next_seq: int):
    supabase.table("user_skill_progress") \
        .update({
            "current_sequence": next_seq,
            "updated_at": datetime.utcnow().isoformat()
        }) \
        .eq("user_id", user_id) \
        .eq("skill", skill) \
        .execute()
