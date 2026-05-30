def dfs(from_, graph, visited, dp):
    visited[from_] = True
    for to in graph[from_]:
        if not visited[to]:
            dfs(to, graph, visited, dp)
            dp[from_] += dp[to]
            dp[from_] %= 1000003

