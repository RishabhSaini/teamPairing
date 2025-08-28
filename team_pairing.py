import random
from datetime import datetime

def generate_weekly_pairs(members):
    members_copy = members[:]
    random.shuffle(members_copy)
    pairs = []

    while len(members_copy) >= 2:
        person1 = members_copy.pop()
        person2 = members_copy.pop()
        pairs.append((person1, person2))

    leftover = members_copy[0] if members_copy else None
    return pairs, leftover

def read_team(file_path="team.txt"):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def write_to_markdown(pairs, leftover, file_path="index.md"):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    with open(file_path, "w") as f:
        f.write(f"# Weekly 1-on-1 Pairs\n")
        f.write(f"📅 **Week of {today}**\n\n")
        for p1, p2 in pairs:
            f.write(f"- {p1} 🤝 {p2}\n")
        if leftover:
            f.write(f"\n❗ _{leftover} has no match this week._\n")

if __name__ == "__main__":
    team = read_team()
    pairs, leftover = generate_weekly_pairs(team)
    write_to_markdown(pairs, leftover)
