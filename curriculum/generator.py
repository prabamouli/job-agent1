import json
from core.config import client, supabase

def generate_curriculum_for_skill(skill: str):
    prompt = (
        f"Break the skill {skill} into exactly 10 subtopics.\n"
        'Return {"subtopics":["a","b"]}'
    )

    resp = client.responses.create(model="gpt-4.1-mini", input=prompt)
    subtopics = json.loads(resp.output_text)["subtopics"]

    for seq, sub in enumerate(subtopics, start=1):
        lesson_prompt = f"Create lesson for {sub}. Return JSON."
        lesson_resp = client.responses.create(
            model="gpt-4.1-mini",
            input=lesson_prompt
        )

        lesson_json = json.loads(lesson_resp.output_text)

        supabase.table("lessons").insert({
            "skill": skill,
            "subtopic": sub,
            "sequence": seq,
            "title": lesson_json["title"],
            "content": lesson_json,
            "xp": 15
        }).execute()
