"""
In a project, you have a list of required skills req_skills, and a list of people.
The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills,
there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person.
You may return the answer in any order.

It is guaranteed an answer exists.
"""
from typing import List
from collections import defaultdict

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:

        n = len(people)
        person_skillset = [set(people[person]) for person in range(n)]
        for person1 in range(n):
            for person2 in range(person1 + 1, n):
                if person1 != person2 and person_skillset[person1] > person_skillset[person2]:
                    person_skillset[person2].clear()

        persons_have_the_skill = defaultdict(set)
        for person, skills in enumerate(person_skillset):
            for skill in skills:
                persons_have_the_skill[skill].add(person)

        ans, skills_needed = [i for i in range(n)], set(req_skills)

        def bt(i, combo):
            nonlocal ans, skills_needed

            if len(combo) >= len(ans):
                return

            if not skills_needed:
                ans = list(combo)
                return

            if req_skills[i] not in skills_needed:
                return bt(i + 1, combo)

            for person in persons_have_the_skill[req_skills[i]]:
                new_skills = person_skillset[person] & skills_needed

                combo.append(person)
                skills_needed -= new_skills
                bt(i + 1, combo)
                combo.pop()
                skills_needed |= new_skills

        bt(0, [])
        return ans


if __name__ == '__main__':
    req_skills = ["java", "nodejs", "reactjs"]
    people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    sol = Solution()
    result = sol.smallestSufficientTeam(req_skills, people)
    print(result)