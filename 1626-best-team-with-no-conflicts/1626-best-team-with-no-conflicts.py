class Solution:
    def bestTeamScore(self, scores, ages):
        n = len(ages)
        team = [(ages[i], scores[i]) for i in range(n)]

        team.sort(key=lambda x: (x[0], x[1]))

        answer = 0
        dp = [0] * n

        for i in range(n):
            dp[i] = team[i][1]
            answer = max(answer, dp[i])

        for i in range(n):
            for j in range(i-1, -1, -1):
                if team[i][1] >= team[j][1]:
                    dp[i] = max(dp[i], team[i][1] + dp[j])
            answer = max(answer, dp[i])

        return answer