class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}




        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)


        parent = {}
        email_to_name = {}


        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(account[1], email)
        
        groups = {}

        for email in parent:
            root = find(email)
            if root not in groups:
                groups[root] = []
            groups[root].append(email)
        
        result = []

        for root, emails in groups.items():
            result.append([email_to_name[root]] + sorted(emails))
        return result
        