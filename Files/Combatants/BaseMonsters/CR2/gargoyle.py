from ....combatant import Combatant, MakeHit, R, Attack

class Gargoyle(Combatant):
    def __init__(self, team):
        super().__init__("Gargoyle", 15, 52, 0, team, [Attack("Bite",lambda r: r+4, MakeHit(lambda: R(1,6)+2), MakeHit(lambda: R(2,6)+2)), Attack("Claws",lambda r: r+4, MakeHit(lambda: R(1,6)+2), MakeHit(lambda: R(2,6)+2))])
        self.AddSaves(2, 0, 3, -2, 0, -2)

    def Damage(self, amount):
        return super().Damage(int(amount/2))

    def Act(self, others):
        for atk in ["Claws", "Bite"]:
            targets = list(sorted(list(filter(lambda c: c.hp>0 and c.team != self.team, others)), key=lambda c: c.hp))
            if len(targets)>0:
                self.AttackWith(targets[0], self.attacks[atk])