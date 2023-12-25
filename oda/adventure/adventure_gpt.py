from openai import OpenAI

client = OpenAI()


def adventure_maker(ch_age, ch_class, ch_race):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a DnD Master, skilled in explaining complex programming concepts with creative flair.",
            },
            {
                "role": "user",
                "content": f"Make my Story. I'm {ch_age}, {ch_class} and {ch_race}",
            },
        ],
    )
    story = completion.choices[0].message
    return story
