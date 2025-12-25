from core.config import supabase
from progress.service import get_or_create_skill_cursor

def fetch_next_lesson(user_id: str, skill: str):
    seq = get_or_create_skill_cursor(user_id, skill)

    res = supabase.table("lessons") \
        .select("id, title, content, xp, sequence") \
        .eq("skill", skill) \
        .eq("sequence", seq) \
        .execute()

    if not res.data:
        return None

    return res.data[0]
