# ✅ Intuition:
# The problem is to merge accounts that share common emails.
# Two accounts belong to the same user if they have at least one common email.
# To solve this, we can model emails as nodes in a graph and connect them if they belong to the same account.
# Instead of building a full adjacency list, we use Union-Find (Disjoint Set Union) to group connected emails.
# Steps:
# 1. For each account, union all its emails with the first email (they belong to the same person).
# 2. Map each email to its root parent using find() function.
# 3. Group emails by root and prepend the user name.

from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Union-Find parent dictionary
        parent = {}
        
        # Map email -> user name
        email_to_name = {}

        # ✅ Find with path compression
        def find(x):
            # Recursively find root and compress path
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # ✅ Union two sets
        def union(x, y):
            parent[find(x)] = find(y)

        # ✅ Step 1: Build parent mapping and union emails in each account
        for account in accounts:
            name = account[0]
            # For every email in the account
            for email in account[1:]:
                # Initialize parent if not present
                if email not in parent:
                    parent[email] = email
                # Map email to name
                email_to_name[email] = name
                # Union first email with current email (connect them)
                union(account[1], email)
        
        # ✅ Step 2: Group emails by their root parent
        groups = {}
        for email in parent:
            root = find(email)  # Find the root representative
            if root not in groups:
                groups[root] = []
            groups[root].append(email)
        
        # ✅ Step 3: Build result (sort emails in each group and prepend name)
        result = []
        for root, emails in groups.items():
            result.append([email_to_name[root]] + sorted(emails))
        
        return result


# ✅ Time Complexity:
# Let N = total number of emails across all accounts
# - Union-Find operations: O(N * α(N)) ≈ O(N), where α is inverse Ackermann (almost constant)
# - Sorting each group: O(N log N) in the worst case (all emails in one group)
# Overall: O(N log N)

# ✅ Space Complexity:
# - parent dict: O(N)
# - email_to_name dict: O(N)
# - groups dict: O(N)
# Total: O(N)
