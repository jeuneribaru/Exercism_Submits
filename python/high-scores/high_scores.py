class HighScores:
    def __init__(self, scores : list):
        self.scores = scores
        self.sorted_score_list = self.scores.copy()
        self.sorted_score_list.sort()

    def personal_best(self):
        return self.sorted_score_list[-1]
    
    def personal_top_three(self):
        top = self.sorted_score_list[-3 :].copy()
        top.reverse()
        return top
    
    def latest(self):
        return self.scores[-1]


Julien = HighScores([115, 34, 67, 99])
print(Julien.personal_best())
print(Julien.personal_top_three())
print(Julien.latest())