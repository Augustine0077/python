capitals = {"USA": "Washington, D.C.", 
            "France": "Paris",
              "Japan": "Tokyo",
              "India": "New Delhi"
            }

if capitals.get("India"):
    print("The capital exists.")
else:
    print("The capital does not exist.")
if capitals.get("Russia"):
    print("The capital exists.")
else:
    print("The capital does not exist.")